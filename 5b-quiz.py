'''
Question 1
Which of the following expressions corresponds to a dictionary with no elements?
'''

'''
Your Answer		Score	Explanation
[]	Correct	1.00	
{}	Correct	5.00	
()	Correct	1.00	
dict()	Correct	3.00	
Total		10.00 / 10.00	
'''

'''
Question 2
Given an existing dictionary favorites, what Python statement adds the key "fruit" to this dictionary with the corresponding value "blackberry"?
'''

'''
Your Answer		Score	Explanation
favorites["fruit" : "blackberry"]	Correct	1.00	
favorites = {"fruit" : "blackberry"}	Inorrect	0.00	This statement creates a new dictionary instead of adding to an existing dictionary.
favorites["fruit" = "blackberry"]	Correct	1.00	
favorites["fruit"] = "blackberry"	Correct	7.00	
Total		9.00 / 10.00	
'''
'''
Question 3
Keys in a dictionary can have which of the following types?
'''

'''
Your Answer		Score	Explanation
Dictionaries	Correct	1.25	
Lists	Correct	1.25	
Strings	Correct	2.50	
Numbers	Correct	2.50	
Tuples	Correct	2.50	
Total		10.00 / 10.00	
'''

'''
Question 4
Values in a dictionary can have which of the following types?
'''

'''
Your Answer		Score	Explanation
Tuples	Correct	2.50	
Lists	Correct	2.50	
Strings	Correct	2.50	
Numbers	Correct	2.50	
Total		10.00 / 10.00	
'''

'''
Question 5
We often want to loop over all the key/value pairs in a dictionary. Assume the variable my_dict stores a dictionary. One way of looping like this is as follows:

for key in my_dict:
    value = my_dict[key]
    …
However, there is a better way. We can instead write the following:

for key, value in ???:
    …
What code should replace the question marks so that the two forms are equivalent? Refer to the video on dictionaries or the CodeSkulptor documentation.

'''
Your Answer		Score	Explanation
my_dict.values()			
list(my_dict)			
items(my_dict)			
my_dict.items()	Correct	10.00	
my_dict.keys_values()			
my_dict.keys()			
Total		10.00 / 10.00	
'''

'''
Question 6
Conceptually, the purpose of a dictionary is to represent a relationship between two collections of data — each key in the dictionary is related to one value. Which of the following situations are instances of such a relationship?

Do not include situations where you have to introduce additional information in order to fit them into such a relationship.
'''

'''
Your Answer		Score	Explanation
Storing students' IDs (identification numbers) and grades for a particular assignment	Correct	4.00	
Yes, map each ID (key) to the corresponding grade (value). Each ID should be unique — otherwise it shouldn't be considered an ID.

Storing a sorted collection of strings	Correct	1.00	
No, dictionaries are unordered. A list is a better option.

Storing names and IDs (identification numbers)	Correct	4.00	
Yes, map each ID (key) to the corresponding name (value). Each ID should be unique — otherwise it shouldn't be considered an ID.

Computing averages	Correct	1.00	
No, dictionaries don't compute anything.

Total		10.00 / 10.00	
Question Explanation

Note that it is possible to use dictionaries to represent sets and ordered collections. However, the focus of this question is on the relationship between data.
'''

'''
Question 7
In the previous quiz, you were asked to complete the following code:

import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        ???
    return points
Now, we want to rewrite starting_points using a list comprehension. Which list comprehensions could replace the following question marks?

def starting_points(players):
    """Returns a list of random points, one for each player."""
    return ???
Refer to this week's "Visualizing iteration" video for examples of list comprehensions. Also, try each example in CodeSkulptor before answering the question.
'''

'''
Your Answer		Score	Explanation
[for player in players: random_point()]	Correct	0.50	
Syntactically incorrect

[random_point for players]	Correct	0.50	
Syntactically incorrect and also need to call the random_point function.

[random_point() for player in players]	Correct	4.00	
[random_point for player in players]	Correct	0.50	
Need to call the random_point function.

[random_point() for p in players]	Inorrect	0.00	
[random_point(player) for player in players]	Correct	0.50	
random_point() doesn't take an argument.

Total		6.00 / 10.00	
'''

'''
Question 8
You have the following code. The goal is to display a portion of the image, rescaling it to fill the canvas.

import simplegui

frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    canvas.draw_image(image, image_size,
                      [image_size[0] / 2, image_size[1] / 2],
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

frame.start()
Run it, and observe that nothing is displayed in the frame. What is the problem?
'''

'''
Your Answer		Score	Explanation

The destination arguments in draw_image are incorrect. We aren't specifying values that would draw the image on this size canvas.


The file doesn't exist.


One or more of the draw_image arguments are of the wrong type.


The source arguments in draw_image are incorrect. We are trying to load pixels that are not within the image, and thus the draw fails.

Correct	10.00	

The file is not an image.

Total		10.00 / 10.00	
'''

'''
Question 9
Write a CodeSkulptor program that loads and draws the following image:

http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png
with a source center of [220, 100] and a source size of [100, 100]. What one word appears in the canvas? If a letter is capitalized in the image, enter it as a capital.

Note that you do have to position the image as stated to see the correct word.
'''

'''
Answer for Question 9
You entered:

Your Answer		Score	Explanation
Testing	Incorrect	0.00	
Total		0.00 / 20.00
'''
