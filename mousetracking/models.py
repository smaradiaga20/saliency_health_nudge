from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, ExtraModel,
    Currency as c, currency_range
)
import json

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


class Group(BaseGroup):
    def live_event(self, id_in_group, payload):
        player = self.get_player_by__id(id_in_group)
        json_object = json.decode(payload)
        timestamp = json_object['timestamp']
        region = json_object['region']
        mouse_event = MouseEvent.objects.create(player=player, timestamp=timestamp, region=region)
        mouse_event.save()
    

class Player(BasePlayer):
    stimulus = models.StringField()
    def mouse_events(self):
        return MouseEvent.objects.filter(player=self)


class MouseEvent(ExtraModel):
    player = models.Link(Player)
    region = models.IntegerField()
    timestamp = models.IntegerField()


def custom_export(players):
    yield ['session','participant_code','stimulus','region','timestamp']
    for p in players:
        for m in p.mouse_events():
            yield [p.session.code, p.participant.code, p.stimulus, m.region, m.timestamp]
