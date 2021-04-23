# Contributing to the drawing game
I see that you are intrested in contributing to this game, how exciting!!!! 
As an open source project we are glad to have any form of community support. 
This includes issues on our issue tracker as well as code contributions. 
This guide will get you up and running with the project.

**NOTE:** This project was developed for the Open Source Software course at RPI. While I would like to continue working on it, I dont want to make any promeses.
The good news is the code is 100% open source under the MIT license so you are free to fork the project if I am slow to respond.


# Running the program
Start by cloning the repo `git clone https://github.com/elihschiff/drawing-game.git`
## Server
Run these commands:
```bash
$ pip install -r requirements.txt
$ cd server
$ python server.py
```
If you are a beginner, I would highly recoment you install and use nodemon to run the server. 
Nodemon is designed to restart node servers when any of the server files are changed however it can also be used for python with a few tricks.
To install and use nodemon, skip the 3rd line above and instead run:
```bash
# npm install -g nodemon
$ nodemon --exec python server.py
```

## Client
Now that you have the server running, open of `client/index.html` in a web browser. 
If you want to test 2 or more players, you may run into issues if you use the same web browser.
This is because the app uses local storage which is the same for all instances of a website in the same browser.
You have 2 options:
1. Open up your second instance of index.html in a new browser or in an incogneto window
2. Install a program like this https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/ which allows you to have tabs that are isolated from eachother.
This is the prefered method as it allows for unlimited instances (aka players)

Unfortunatly, nodemon cannot work for the front end. That means at this time, you must refresh all the front end clients if you make changes to the front end.
