from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()

@register.simple_tag
def track_mouse(stimulus_name,num_rows,num_columns, exclude_rows="0", image_format="jpg"):
    #produce the html, possibly with also the necessary css and javascript so its all self contained
    num_slices = num_rows * num_columns
    whole_stimulus_path = static("mousetracking/%s.%s" %  (stimulus_name, image_format))
    
    exclusions = [int(i) for i in exclude_rows.split(',')]

    slices = []
    for i in range(1,num_slices + 1):
        part = static("mousetracking/%s_%02d.%s" % (stimulus_name, i, image_format))
        slices.append(part)
    
    html = format_html("""
    <div class="mousetracking-stimulus" id="{}">
        <image class="image blurred" src="{}"/>
        <div class="image-parts">
            <div class="image-row {}" data-option={}>
            """, stimulus_name, whole_stimulus_path, "" if 1 in exclusions else "row-option",1) 
    
    for i, part in enumerate(slices, 1):
        html += format_html("""
                <div class="image-cell">
                    <img src="{}" class="region" id="{}" data-stimulus="{}" />
                </div>
        """, part, i, stimulus_name,(i//num_columns)+1)
        
        if i % num_columns == 0:
            if ((i //num_columns) + 1) < num_rows:
                html += format_html("""
                    </div>
                    <div class="image-row {} " data-option={}> 
                """, "" if ((i//num_columns) + 1 ) in exclusions else "row-option", (i//num_columns) + 1)
    
    html += mark_safe("""
                </div>
            </div>
        </div>""")
    return html
