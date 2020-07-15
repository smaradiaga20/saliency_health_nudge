from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.contrib.staticfiles.templatetags.staticfiles import static


class Grid(Page):
    live_method = 'live_event'
    form_model = 'player'
    form_fields = ['choice']

page_sequence = [
    Grid,
]
