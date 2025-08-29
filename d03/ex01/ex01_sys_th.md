
# Module 03 - Piscine Python for Data Science
## Intro to Python: d03/Package management and virtual environment


## Exercise ex01 - Installing Package
### Files to turn in:
####		- 'pies_bars.sh'
####		- 'file with the data'
####		- 'virtual environment folder'

### System Thinking:

#### Purpose: What is the system trying to achieve?
	- Install 'termgraph' as the first package, on virtual environment, previously created.
	- Recreate the example visualization exactly.
	- Create a shell script 'pies_bars.sh' that contains only the part of making the graph without activation

#### Elements: What are the parts that make up  the system?
	- Virtual environment
	- 'termgraph' a package that will draw the visualization.
	- a file that contains the data to be visualize. 
	- a shell script that will make the visualization.

#### Interconnections: How do elements interact with each other?
	- Use the data file that will be drawned using termgraph
	- the command used on drawing the graph using the data file will be put to the 'pies_bar.sh'
	- the command used for drawing the graph using the data file 
			will be put in 'pies_bars.sh'

#### Inputs/Outputs: What goes in, and what comes out?
	-Input: Activate the environment.
	-Input: Install termgraph using pip
	-Input: Create a data file that contains the data to be drawn.
	-Input: Draw the graph using the command 'termgraph <datafile> --color {color,color}' from the terminal
	-Output: It will show the graph on the terminal
	-Input: Create a shell script named 'pies_bars.sh' and put the command used to draw the graph
	-Input: Deactivate the environment.

#### Feedback/Adaptation: How does the system respond to failure or success?
	-Success: Prints the graph, if the environment is active, and the shell script 'pies_bars.sh' is executed
	-Failure: If 'termgraph' is not installed and activated.
		Data file problem:
			- if the file is empty.
			- if the file only has categories without labels and numeric data
			- if the file only has labels
	-Both: Can execute without activation by using the binary file of termgraph by
	       using an absolute path. It will fail if executed on other machine (portability issue).
			  
---

### Flow:

##### Notes: 
		- The shell script 'pies_bars.sh' only contains the command to draw the graph.
		- The data file should be the same as the data on the example given.
		- The color of the graph should be different from the given example.
		- Only 'pies_bars.sh', data file and the virtual environment should be submitted.
		- The purpose of pies_bars.sh isn’t to execute the graph immediately (since the venv activation is excluded), but rather to record the exact command you’d run when inside the venv.


1. **Set up**:
	- Copy the virtual environment folder from previous exercise.
		- command: 'cp ../ex00/<env_name> .'
		           (assuming your current directory is ex01)
	
	- Check if successfully copied:
		- command: 'ls'
					it shows the list of file or folder inside the current directory.


2. **Activate the virtual environment**:
	- Activate:
		- command: 'source <env_name>/bin/activate'
	
	- Check if activated:
		- command: 'echo $VIRTUAL_ENV'
			-active: if it show a path.
			-notactive: if the terminal is empty.


3. **Install 'termgrap'**:
	- Install using pip/pip3:
		- command: 'pip install termgraph'
		           or 'pip3 install termgraph'

	- Verify the installation:
		- command: 'which termgraph'
		  it will show the absolutepath of termgraph installed in your virtual environment.


4. **Create a data file**:
	- Create data file:
		- command: 'code <filename>.dat' <- Vscode.
	      You can use your prefered editor.
	
	- Copy the data on the example given:
		```
		@Pies,Bars
		2007,73.32,70.52
		2008,81.23,93.00
		2009,181.43,135.10
		2010,110.21,95.00
		2011,93.97,90.45

		```
	- Save it


5. **Draw the graph**:
	- Draw the graph using termgraph and the datafile with colors.
		- command:
		```shell
		termgraph <datafile> --color {blue,magenta}
		```

	- Run command on the command line.
	- Visually verify if the graph is the same as the given example except the color
	- If not there is a problem with the data file.


6. **Deactivate the current environment**:
	- Deactivate:
		- command: 'deactivate'

	- Check if the status of environment:
		- command: 'echo $VIRTUAL_ENV'
			-active: if it show a path.
			-notactive: if the terminal is empty.


7. **Create 'pies_bar.sh' shell script**:
	- pies_bar.sh
	```bash
	#!/bin/bash

	termgraph PBset.dat --color {blue,magenta}
	```

	- add execute permission on 'pies_bar.sh'
		- command: 'chmod u+x pies_bar.sh'


8. **Submission**:
	- Submit 'pies_bar.sh' shell script, data file and the folder of the virtual environment.


