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
    stimulus_list = [['example menu','1,21',]]

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.stimulus = Constants.stimulus_list[(p.round_number - 1)][0]
            p.exclude_options = Constants.stimulus_list[(p.round_number - 1)][1]

class Group(MouseTrackingGroup):
    pass
    

class Player(MouseTrackingPlayer):
    stimulus = models.StringField()
    choice = models.StringField(widget=widgets.HiddenInput)
    exclude_options = models.StringField()
