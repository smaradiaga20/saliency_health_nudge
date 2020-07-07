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
    num_rounds = 2
    stimulus_list = ['chicken_kiev','Pepperoni_Pizza_Color_Left',]

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.stimulus = Constants.stimulus_list[(p.round_number - 1) % 2]
            p.stimulus_2 = Constants.stimulus_list[p.round_number % 2]

class Group(MouseTrackingGroup):
    pass
    

class Player(MouseTrackingPlayer):
    stimulus = models.StringField()
    stimulus_2 = models.StringField()
    choice = models.StringField()
