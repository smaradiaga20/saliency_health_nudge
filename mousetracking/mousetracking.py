from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, ExtraModel,
    Currency as c, currency_range
)
from django.db.models import BigIntegerField
#from django.

class MouseTrackingGroup(BaseGroup):
    def live_event(self, id_in_group, payload):
        player = self.get_player_by_id(id_in_group)
        timestamp = payload['timestamp']
        region = payload['region']
        action = payload['action']
        stimulus = payload['stimulus']
        mouse_event = MouseEvent.objects.create(player=player, timestamp=timestamp, region=region, action=action, stimulus=stimulus)
        mouse_event.save()

    class Meta:
        abstract=True


class MouseTrackingPlayer(BasePlayer):
    def mouse_events(self):
        return MouseEvent.objects.filter(player=self)

    class Meta:
        abstract=True

class MouseEvent(ExtraModel):
    #player = models.Link(MouseTrackingPlayer)
    #player = ForeignKey('mousetracking.Player')
    player = models.Link('mousetracking.Player')
    stimulus = models.StringField()
    region = models.IntegerField()
    action = models.StringField()
    timestamp = BigIntegerField()


def custom_export(players):
    yield ['session','participant_code','round_number', 'stimulus','region','action', 'timestamp']
    for p in players:
        for m in p.mouse_events():
            yield [p.session.code, p.participant.code, p.round_number, m.stimulus, m.region, m.action, m.timestamp]
