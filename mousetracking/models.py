from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, ExtraModel,
    Currency as c, currency_range
)

from .mousetracking import MouseTrackingGroup, MouseTrackingPlayer, MouseEvent, custom_export

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mousetracking'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.stimulus = "chicken kiev"


class Group(MouseTrackingGroup):
    pass
    

class Player(MouseTrackingPlayer):
    stimulus = models.StringField()
