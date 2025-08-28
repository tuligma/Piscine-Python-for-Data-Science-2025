
# Module 03 - Piscine Python for Data Science
## Intro to Python: d03/Package management and virtual environment


## Exercise ex00

### System Thinking:

#### Purpose: What is the system trying to achieve?
	- Create a Python virtual environment
	- Run python3 from the terminal to print the environment name
	- Create a script that prints the location of the environment
	- Understand why you get KeyError if the environment is deactivated.

#### Elements: What are the parts that make up  the system?
	- Virtual environment
	- os library to print the name of the current active environment
	- venv.py script that prints the environment name and location
	- Terminal commands: create-venv -> activate -> deactivate - run script

#### Interconnections: How do elements interact with each other?
	- The shell automatically sets 'VIRTUAL_ENV' when the environment is activated
	- to print the name of you have to use os.environ['VIRTUAL_ENV'] on python3 from the terminal
	- When the environment is deactivated it will raise a KeyError because 'VIRTUAL_ENV' is not set.

#### Inputs/Outputs: What goes in, and what comes out?
	-Input: Activate the environment.
	-Input: Run python3 from the terminal
	-Input: import os and execute 'os.environ['VIRTUAL_ENV'].split('/')[-1]'
	-Output: prints the name of the current active virtual environment from the terminal
	-Input: execute the 'venv.py' script
	-Output: prints the location of the current active virtual environment
	-Input: deactivate the environment.
	-Input: execute the venv.py again.
	-Output: KeyError will be raised be cause the 'VIRTUAL_ENV' is not set if environment is deactivated

#### Feedback/Adaptation: How does the system respond to failure or success?
	-Success: Prints the name and path of the environment
	-Failure: If 'VIRTUAL_ENV' is not set due to deactived environment.
		-> Not considered failure due to pointing why it gives KeyError when
		   the environment is deactivated. 


Flow:

1. Set up:
	- Install 'virtualenv' if not installed.
		- command: 'pip install virtualenv'

	- Check if package 'virtualenv' is installed:
		- command: 'pip show virtualenv'

2. Create a new environment:
	- Create environment:
	  - command: 'virtualenv <env_name>'
	
	- Check the created environment
		- command: 'ls'
		- check a folder that has a name of your newly created environment

3. Activate the virtual environment:
	- Activate:
		- command: 'source <env_name>/bin/activate'
	
	- Check if activated:
		- command: 'echo $VIRTUAL_ENV'
			-active: if it show a path.
			-notactive: if the terminal is empty.

4. Run Python3 and print the name of environment:
	- Run Python3 from the terminal:
		- command: 'python3'
	
	- Import os module:
		- command: 'import os'
	
	- Print the name of the current active environment:
		- command: 'os.environ['VIRTUAL_ENV'].split('/')[-1]'
	
	- Verify if the name of the environment show on the terminal.

	- Exit python3 from terminal:
		- command: 'exit()' or press 'CTRL + D'

5. Create a python script that prints a custom message:
	- venv.py
		```python
		#!/usr/bin/env python3
		
		import os
		print(f"Your current virtual env is {os.environ['VIRTUAL_ENV']}")
		```
	
	- add execute permission to 'venv.py'
		- command: 'chmod u+x venv.py'
	
	- Execute 'venv.py'
		- command: './venv.py'
	
	- Visually check the terminal if it prints the custom message.

6. Deactivate the current environment:
	- Deactivate:
		- command: 'deactivate'

	- Check if the status of environment:
		- command: 'echo $VIRTUAL_ENV'
			-active: if it show a path.
			-notactive: if the terminal is empty.

7. Run 'veny.py' script again:
	- Execute 'venv.py'
		- command: './venv.py'

	- Visually verify if it triggers the error KeyError
	- KeyError happens 'VIRTUAL_ENV' is not set 
	  because the virtual environment is not active.

8. Submission:
	- Submit 'venv.py' script and the folder of the virtual environment.
	  
