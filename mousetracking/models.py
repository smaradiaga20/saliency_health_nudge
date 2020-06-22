from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, ExtraModel,
    Currency as c, currency_range
)
<<<<<<< HEAD
import json
=======
>>>>>>> 4bc3b9eb19b7063c1f07aa282c3ed5e7e45f7086

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
<<<<<<< HEAD
        player = self.get_player_by__id(id_in_group)
        json_object = json.decode(payload)
        timestamp = json_object['timestamp']
        region = json_object['region']
        mouse_event = MouseEvent.objects.create(player=player, timestamp=timestamp, region=region)
        mouse_event.save()
=======
        player = self.get_player_by_id(id_in_group)
        timestamp = payload['timestamp']
        region = payload['region']
        action = payload['action']
        mouse_event = MouseEvent.objects.create(player=player, timestamp=timestamp, region=region, action=action)
        mouse_event.save()
        return {id_in_group: "created mouse_event %d" % mouse_event.id}
>>>>>>> 4bc3b9eb19b7063c1f07aa282c3ed5e7e45f7086
    

class Player(BasePlayer):
    stimulus = models.StringField()
    def mouse_events(self):
        return MouseEvent.objects.filter(player=self)


class MouseEvent(ExtraModel):
    player = models.Link(Player)
    region = models.IntegerField()
    timestamp = models.IntegerField()
<<<<<<< HEAD


def custom_export(players):
    yield ['session','participant_code','stimulus','region','timestamp']
    for p in players:
        for m in p.mouse_events():
            yield [p.session.code, p.participant.code, p.stimulus, m.region, m.timestamp]
=======
    action = models.StringField()


def custom_export(players):
    yield ['session','participant_code','stimulus','region','action', 'timestamp']
    for p in players:
        for m in p.mouse_events():
            yield [p.session.code, p.participant.code, p.stimulus, m.region, m.action, m.timestamp]
>>>>>>> 4bc3b9eb19b7063c1f07aa282c3ed5e7e45f7086
