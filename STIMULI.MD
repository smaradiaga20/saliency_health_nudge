# Stimuli Requirements
To work with the code, the stimuli must meet the following requirements:
 * each stimulus should have a single image that shows the whole stimulus (this will be blurred by the code), as well as separate images for each part
 * all images should be saved as jpg files
 * all rows must contain the same number of images
 * every image in an individual row must be exactly the same height
 * try to have no full images smaller than 900px wide, otherwise they will be scaled up by the code and look bad.  Larger images should scale down fine.
 * follow the following naming conventions:
    * stimulus_name.jpg for the whole stimulus image for blurring
	* stimulus_name_01.jpg, stimulus_name_02.jpg, stimulus_name_03.jpg, etc for each part, counting from top left across rows then down columns:
```
stim_01.jpg  |  stim_02.jpg  |  stim_03.jpg
--------------------------------------------
stim_04.jpg  |  stim_05.jpg  |  stim_06.jpg
--------------------------------------------
stim_07.jpg  |  stim_08.jpg  |  stim_09.jpg

```

## Suggested Process for Slicing and Naming Stimuli

The naming conventions are taken from the defaults that photoshop produces. I don't have Photoshop myself, so cannot give you a fully joined-up step by step guide.  However, I found a couple of tutorials that walk through the necessary steps:

**How to make guides**

https://www.youtube.com/watch?v=ZRkk-q-L654

**Create slices from guides (see steps 1 and 2 only)**

https://www.webucator.com/how-to/how-work-with-type-adobe-photoshop.cfm#:~:text=Go%20to%20the%20Toolbar%20%2C%20click,that%20need%20to%20be%20excluded.

Then to save the files, go to the File menu > Export > Save for Web (Legacy) and choose [images only] as the "format" option, and [all slices] in the "slices" option. Assuming you start with a jpg for the whole stimulus image, it should produce the slices with the necessary suffixes automatically. It will also guarantee the rows are the correct heights. 
