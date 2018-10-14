# SDHACKS2018

A program created for the SD Hacks 2018 Hackathon in less than 36 hours by Eric Ke, Nathan Zhao, and Ray Sakanoue using Python.

The application uses the camera to take pictures of the user's hands as input, and uses the Clarifai API to identify the image using computer vision.  The sign language gestures are taken, stored, deciphered, and then printed out as text to another window.

For the convenience of the users, we have already trained the model through the Clarifai API.  If you wish to train it again, simply run the "main.py" file with the "testing" variable set to true.

To begin using the app, run the "fusion.py" file; a camera window will show up, along with an output window.  Place your hand so that the sign language gesture you are making fills up the entire camera window, and then press the SPACEBAR to take a picture.  The application will then decipher it and print the letter to the output window, along to a .txt file named "output.txt".  After you have finished signing your message, press the ESC key to exit the app.

Technologies Used include: Python, Clarifai API, and Open CV
