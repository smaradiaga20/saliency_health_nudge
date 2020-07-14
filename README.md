# Usage

## Stimuli

All stimulus images should be places in the `mousetracking/static/mousetracking/` folder.  See STIMULI.md for requirements on the stimuli.

## mousetracking/models.py

This file determines what data you record besides the mousetracking data.  The main section of the code to pay attention to is the block starting `def Player(MouseTrackingPlayer):`.  This currently has two slots for stimuli to be presented - stimulus and stimulus_2, as well as a choice field - choice.   If you need to have different numbers of rows or columns per stimuli, you should create new IntegerFields in this section. 

The `creating_session(self)` method above runs when setting up the experiment.  This is where you should set the stimuli for each round, you can do this simply as is done in the example just looping through an array of stimulus names set in Constants, or if more complexity is needed for example with differing numbers of rows/columns by stimulus, you could read in a csv and use that to set the fields on player. In this example, the stimulus field must be filled with exactly the same as the name of the whole file (without the .jpg)

## mousetracking/templates/mousetracking

The **`{% track_mouse %}`** template tag is used to present a stimulus and record mouse events occuring on that stimulus. The arguments are as follows: `{% track_mouse stimulus_name num_columns num_rows %}`
 * **stimulus_name** should be a string containing the name of the stimulus, without the .jpg at the end
 * **num_columns** should be an integer
 * **num_rows** should be an integer
Any of these arguments can be hard coded into the template (as num_columns and num_rows are in the example - each being set to 3) or a variable of an appropriate type can be used in their place (as player.stimulus is used to give the stimulus_name argument).

**Grid.html**  This template simply presents the stimulus set and records mouse interactions. There is no decision variable on this page.

**Choice.html** This template presents two stimuli side by side, demonstrating the auto-resizing feature of the track_mouse template tag.  If larger stimuli are needed for comparrison, changing this file to display the stimuli each on their own rows can be done by changing the `col-5` classes to `col-12`.  (This page, and otree templates in general, use the bootstrap library for formatting. 

Choice.html also shows the use of the `{% formfield %}` template tag to create a dropdown.  If you would prefer this choice to be radio buttons, changing models.py so that `choice = ChoiceField(widget=widgets.RadioSelect())` will make that happen automatically.

## mousetracking/pages.py

This file is used to set the parameters for the templates. If you need a participant to make some kind of choice selection, it should be included in the page definition here. For example, in the `Choice` page, the dv is 'choice', so we set `form_model = 'player'` and `form_fields = ['choice']`.

The Choice page also demonstrates building the options for a choice field programatically - `def choice_choices(self):` gets the two stimuli defined on the player model and populates the dropdown with those values. 

If you need time pressure for a page, that should be set here too - including a line in the page definition like `timeout_seconds = 10` will create a timer on the page and force the participant to respond within 10 seconds otherwise a blank response will be saved before the participant is moved on to the next trial.
