from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()

@register.simple_tag
def track_mouse(stimulus_name,num_rows,num_columns):
    #produce the html, possibly with also the necessary css and javascript so its all self contained
    num_slices = num_rows * num_columns
    whole_stimulus_path = static("mousetracking/%s/whole.jpg" %  stimulus_name)
    
    slices = []
    for i in range(1,num_slices + 1):
        part = static("mousetracking/%s/%d.jpg" % (stimulus_name, i))
        slices.append(part)
    
    html = format_html("""
    <div class="mousetracking-stimulus" id="{}">
        <image class="image blurred" src="{}"/>
        <div class="image-parts">
            <div class="image-row">
            """, stimulus_name, whole_stimulus_path)
    
    for i, part in enumerate(slices, 1):
        html += format_html("""
                <div class="image-cell">
                    <img src="{}" class="region" id="{}" />
                </div>
        """, part, i)
        
        if i % num_columns == 0:
            html += mark_safe("""
                </div>
                <div class="image-row">
            """)
    
    
    html += mark_safe('''
                </div>
            </div>
        </div>''')
    
    html += format_html("""
    <script type="text/javascript">
    
    jQuery(document).on('mouseover','.region', 
        function(e){{
            liveSend({{'region': e.currentTarget.id, 'action': 'enter', 'timestamp': Date.now()}});
       }});                                                                                
    jQuery(document).on('mouseout','#{} .region',
        function(e){{                                                                       
            liveSend({{'region': e.currentTarget.id, 'action': 'exit', 'timestamp': Date.now()}});
        }});                                                                                  
    function liveRecv(payload){{ console.log(payload)}};
    </script>""", stimulus_name)
    
    return html
