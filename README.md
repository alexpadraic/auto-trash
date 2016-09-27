# AutoTrash
Automate your trash

### Team Members

Alexander Pellas, Julian Bertini, Raj Desai, Simon Nim


### Project Description

Our problem was a daunting one - how can we solve the problem of humans having to segregate trash into garbage, compost, and recycling without messing it up?

We bring you AutoTrash - a trash can that takes the decision-making out of the user's hands.

To start, we knew we would need a raspberry pi to control the entire process, the correct sensors and motors to suit our needs, the right design, a way of distinguishing objects from eachother, and a Python script to tie everything together. We had no experience with any of the tech, and only 8 days to present.

The final product uses an arduino infrared sensor to detect an object has been placed in the staging area. Once triggered, the script then tells the camera to take a picture of the object, this image is then run through a Tensorflow model to try to recognize the object, and then will run the motor to either recycle or compost the object.


### DEMO

See demo video here: https://youtu.be/AzB-CW20QYA