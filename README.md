# SAISandbox
"Semi" artificial intelligence sandbox

# Challenge

Decide which team is the winning team and then just implement the code so that your team wins! Best solutions win the ticket for Star Wars preview on 14th December at Finnkino Tennispalatsi!

# Deadline

Deadline for the challenge is on 7th December 2016

# How to apply?

Fill your contact information to Google Form and fork this repoistory. Create pull request after you've finalized your code before deadline. You will be contacted on 8th December 2016.

# Factions

BrownRebelScumbagWithLaser aka Brown

WhiteManWithLazer aka White

# Rules

You can only modify challenge.py from this repository. Change the winning team of your choice by changing value of `WINNER` variable using enums defined `TEAMS` (WHITE or BROWN).

The run method from chosen team will be run on every loop on the main loop.

The team that should lose will stay put for the whole game.

# Methods

You can check the methods from models.py for more information. Basic methods that you can use are:

* move_left
* move_right
* move_up
* move_down
* shoot

All of the move methods will return False if there is an obstacle.

# Setup

1. Install git
2. Install python 2.7.x
3. Install python pip
4. Install pygame
5. Clone repository
6. run command `cd SAISandbox ; pip install -r requirements.txt`

# Run game

Use following command `python game.py` and the game will automatically end after one of the teams is dead. The game will print to terminal "You win" or "You lose" depending if the team you decided to win actually won.