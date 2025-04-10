# Pokemon Battle Game

## Purpose

Simple command line based Pokemon Battle Game pair programmed with Mansurual Karim (github.com/mansk).

Demonstrates use of Object Orientated Programming (OOP).

For this sprint, head to Northcoder's L2C app:

https://l2c.northcoders.com/courses/de2-fun/pokemon-battler

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

4. To execute the full range of checks (security tests, PEP8 compliance, and the test suite), run:

   ```sh
   make run-checks
   ```

Test coverage for the key source code is over 90%, however, there are no tests for the file "src/simple_script.py", which is used to execute the command line game.  There are also no tests for the script "src/pokemon_data.py", as this is simply the game data and does not contain any methods or functions.

# To do

1. Add Makefile for setting up dev environment, running security checks, unit tests, and ensuring PEP8 compliance.
2. Doc strings.
3. README.
4. CI/CD.
5. Refactor (e.g. move data into CSV and then modify code to import to a pandas dataframe).