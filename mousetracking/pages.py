from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.contrib.staticfiles.templatetags.staticfiles import static


class MyPage(Page):
    pass

class Grid(Page):
    live_method = 'live_event'
    def vars_for_template(self):
        images = []
        for i in range(1,10):
            image = {'path': static("mousetracking/chickenkiev/SQ%d.png" % i), 'brnext': False}
            if (i % 3) == 0:
                image['brnext']= True
            images.append(image)
        return { 'images': images}

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Grid
]
