from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.contrib.staticfiles.templatetags.staticfiles import static


class MyPage(Page):
    pass

'''
class Grid(Page):
    live_method = 'live_event'
    def vars_for_template(self):
        images = []
        test_regions = [
                        {'top': 0, 'right': 620, 'bottom': 420,'left': 0},
                        {'top': 0, 'right': 1240, 'bottom': 420,'left': 621},
                        {'top': 0, 'right': 1771, 'bottom': 420,'left': 1241},
                        {'top': 421, 'right': 620, 'bottom': 810,'left': 0},
                        {'top': 421, 'right': 1240, 'bottom': 810,'left': 621},
                        {'top': 421, 'right': 1771, 'bottom': 810,'left': 1241},
                        {'top': 811, 'right': 620, 'bottom': 1187,'left': 0},
                        {'top': 811, 'right': 1240, 'bottom': 1187,'left': 621},
                        {'top': 811, 'right': 1771, 'bottom': 1187,'left': 1241},
                        ]

        for i,test_region in enumerate(test_regions):
            image = {'path': static("mousetracking/chickenkiev/original.jpg"), 'brnext': False}
            image.update(test_region)
            if (i % 3) == 0:
                image['brnext']= True
            images.append(image)
        return { 'image': {'path': static("mousetracking/chickenkiev/original.jpg"),},
                 'regions': images,}
'''
class Grid(Page):
    live_method = 'live_event'
    def vars_for_template(self):
        images = []
        for i in range(0,3):
            for j in range(0,3):
                image = {'path': static("mousetracking/chickenkiev/%d-%d.jpg" % (j,i,)), 'brnext': False}
                if j == 2:
                    image['brnext']= True
                images.append(image)
        return { 'whole_image': {'path': static("mousetracking/chickenkiev/original.jpg"),},
                 'images': images,}

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Grid
]
