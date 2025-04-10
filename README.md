# Pokemon Battle Game

## Purpose

Simple command line based Pokemon Battle Game pair programmed with Mansurual Karim (github.com/mansk). Built using Object Orientated Programming (OOP). Two player game to be run on a single machine, who take it turn to select a pokemon that are then pitted against one another.

## Prerequisites

1. Python v3.11.1
2. Make installed on your local machine. Search online for instructions relevant to your operating system.

## Initial setup

1. Fork and clone this repo.
2. From the root directory, run the below command:
   
   ```sh
   make requirements
   ```
   
   This will create a virtual environment with the necessary dependencies (compiled from the file "requirements.in" and then installed from "requirements.txt").

3. Next, run:
   
   ```sh
   make dev-setup
   ```

   This will install "bandit" and "safety" to do security tests, as well as "black" to ensure code is PEP8 compliant, and finally "coverage" to check test coverage.  Note that you will need a safety account (you should be prompted to register or login when first attempting to run the test suite, as detailed in stage 4 below).

4. (Optional) To execute the full range of checks (security tests, PEP8 compliance, and the test suite), run:

   ```sh
   make run-checks
   ```

Test coverage for the key source code is over 90%, however, there are no tests for the file "src/simple_script.py", which is used to execute the command line game.  There are also no tests for the script "src/pokemon_data.py", as this is simply the game data and does not contain any methods or functions.

## Playing the game

Having followed the initial setup instructions above, simply run the below command:

```sh
make battle
```

Then follow the command line prompts to pit two players and their pokemon against each other!

## Future developments

1. Add Doc strings.
2. CI/CD.
3. Optimise reading of pokemon data (e.g. transfer to a CSV file and read in to a pandas dataframe).
4. Modify game to exit after 3 unsuccessful attempts (e.g. to a catch a pokemon that doesn't exist).
5. Add ability to catch multiple pokemon, with chance to be unsuccessful.
6. See further extensions at:
https://l2c.northcoders.com/courses/de2-fun/pokemon-battler