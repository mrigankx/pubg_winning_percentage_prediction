# Pubg winning percentage prediction model

Foobar is a Python library for dealing with word pluralization.

## Problem Statement

In a PUBG game, up to 100 players start in each match (matchId). Players (Id) can be on teams (groupId) which get ranked at the end of the game (winPlacePerc) based on how many other teams are still alive when they are eliminated. During the game, players can pick up different amunitions, revive downed-but-not-dead (knocked) teammates, drive vehicles, swim, run, shoot, and experience all of the consequences -- such as falling too far or running themselves over and eliminating themselves.

The team at PUBG has made official game data available for the public to explore and scavenge outside of "The Blue Circle." This workshop is not an official or affiliated PUBG site. Its based on the data collected by Kaggle and made available through the PUBG Developer API.

We are provided with a large number of anonymized PUBG game stats, formatted so that each row contains one player's post-game stats. The data comes from matches of all types: solos, duos, squads, and custom; there is no guarantee of there being 100 players per match, nor at most 4 player per group.

## Goal

Perform the PUBG data analysis and answer the following questions:

1) Does killing more people increases the chance of winning the game?

2) How do we catch the fraudsters in the game?

3) Can we predict the winning percentage of a player in the game?

## How to run?
1) Clone the repository to local machine.
2) Navigate to master-branch and run 
```
python app.py
```
