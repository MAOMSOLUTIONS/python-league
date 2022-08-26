# :: Span League Score ::

User and Technical documentation


# Index
									
* User documentation							
* Technical documentation					
* Append – Requirements			


# User Documentation

This is a command-line application developed in Python that covers the requirements described in the appendix. The compressed test.zip file is delivered. You must unzip the file; from there it will display the test folder with the following files:

![image](https://user-images.githubusercontent.com/2306656/186985312-8d035d15-892b-4e64-92d5-6b6ca240a286.png)


* Test folder, there are the test case files.
* Env folder, there is the generated environment for Python (py -m venv env).
* Readme file is the instructions file.
* Spanleague.py file contains the Python program, see the technical description of each module below.


# Execution.
To run the program, it is recommended to activate the python environment.

![image](https://user-images.githubusercontent.com/2306656/186985713-3bdc0447-90bd-4084-848e-10108720066d.png)

![image](https://user-images.githubusercontent.com/2306656/186985725-15613aa9-9332-46c5-8b9f-a6c08b54da3c.png)

Run the program in Python.
![image](https://user-images.githubusercontent.com/2306656/186985751-391dcf76-7cc7-46e7-9a67-df7055fbe705.png)

It displays a menu with the next options:
![image](https://user-images.githubusercontent.com/2306656/186985810-8db1629c-19e5-44f7-860e-3b77392e58bf.png)

* 0.- Exit the application
* 1.- Show the results
* 2.- Load a data file

# Capture from the command line.
In the case of capturing the score, type directly on the command line and enter.

![image](https://user-images.githubusercontent.com/2306656/186985865-6b0b319e-dadf-4f43-86a8-5d771bad058e.png)

The application will validate if there are no duplicate teams or if the marker is a non-integer data, for example:

![image](https://user-images.githubusercontent.com/2306656/186985891-47c628b6-efa6-4153-b10f-94bac5288550.png)
![image](https://user-images.githubusercontent.com/2306656/186985901-2930ca88-e3cb-4595-bbfe-de31e325b0c4.png)

In any case: valid or incorrect, the application redisplays the line with the menu to be able to capture more information, for example:

![image](https://user-images.githubusercontent.com/2306656/186985937-952755c8-ea26-4e97-b615-7148b571cc7a.png)

At any time by capturing option ”1” you can view the results

![image](https://user-images.githubusercontent.com/2306656/186985965-9c49c8e3-3490-4632-9622-43412fa026ae.png)

# Load from a file.
To load the data from a file, option “2” must be captured in the menu
![image](https://user-images.githubusercontent.com/2306656/186986043-236c4035-cf47-4545-b830-64924e20ab0d.png)
Get the path and name of the file.
![image](https://user-images.githubusercontent.com/2306656/186986267-f2a77f37-1065-4f5d-a43f-ec5cce7df77b.png)

If the file is correct, the application will generate two output files:
![image](https://user-images.githubusercontent.com/2306656/186986296-314d93d1-078f-41ab-ba16-ff2e29d9c943.png)

* Results, which contains the results-
![image](https://user-images.githubusercontent.com/2306656/186986329-7c0f7e5b-26b2-4464-a70c-370313c1a40e.png)
* Log, where are the possible identified errors
![image](https://user-images.githubusercontent.com/2306656/186986367-89a03d5a-0ac7-4cc9-a699-e2d0fdf0bc91.png)

# Exit application.
To exit the application, you must capture the option "0" from the command line-
![image](https://user-images.githubusercontent.com/2306656/186986409-1b1ba6fa-bf08-4b80-a29a-88d93457ff1e.png)

# Test files.
In the data folder there are three test files, which can be executed and are the cases analyzed

![image](https://user-images.githubusercontent.com/2306656/186986442-6b98c041-c1bd-4bc1-b35d-113c342218f2.png)


# Technical Documentation
The application is inside the spanleague.py file. It was developed using functions and without any additional library other than the one in the environment. The application is divided into the following functions:
![image](https://user-images.githubusercontent.com/2306656/186986642-a4e1813b-9b08-42e4-8672-9cf95549e857.png)
Format the result to present it this way:		
		* 1. Destroyers, 6 pts
		* 2. Lions, 3 pts
		* 3. Rogues, 3 pts
		* 4. Snakes, 3 pts
![image](https://user-images.githubusercontent.com/2306656/186986684-8c522aee-2f5a-4bfb-a19c-32a3cea54ace.png)
Find the team and update the data with the points.

![image](https://user-images.githubusercontent.com/2306656/186986718-815781f3-ad5e-49b3-9082-050ff66ac740.png)
Calculate the point allocation based on the following rules.
* If team1 1 score > Team2 3 3 points are added to the winning team, zero to the losing team.
* If there is a tie, 1 point is assigned to each team.

![image](https://user-images.githubusercontent.com/2306656/186986851-a6b35d1d-5f32-451e-b8c2-584fda38dc22.png)
Validates the data and displays or sends it to a file.
* The teams are different.
* The score is integer.

![image](https://user-images.githubusercontent.com/2306656/186986893-58a30607-1375-4f60-8847-0ffb2faac9f7.png)
Create and write the data in the defined file (Results or error log).

![image](https://user-images.githubusercontent.com/2306656/186986919-83d5bf27-f01d-4ba7-8db4-fff05b40bb22.png)
Reads the data from the bookmarks file and from there generates the results and error log files.

![image](https://user-images.githubusercontent.com/2306656/186986942-0edba9f6-1e02-49f6-b7e6-e5a45e08fa32.png)
Open the bookmark data file and call the read from file function, additionally handle read from file exceptions.

Main function
Manages the main menu waiting for data capture, file selection or display of results.

# Append - Requirements
Read the problem statement, code a working solution (valid input and output will be provided) and supporting tests using a language of your choice. Be prepared to explain your solution during a review.

# The Problem
We want you to create a production ready, maintainable, testable command-line application that
will calculate the ranking table for a league.

# Input/output
The input and output will be text. Either using stdin/stdout or taking filenames on the command
line is fine.
The input contains results of games, one per line. See “Sample input” for details.
The output should be ordered from most to least points, following the format specified in
“Expected output”.
You can expect that the input will be well-formed. There is no need to add special handling for
malformed input files.

# The rules
In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points.
If two or more teams have the same number of points, they should have the same rank and be
printed in alphabetical order (as in the tie for 3rd place in the sample data).

# Guidelines
This should be implemented in a language with which you are familiar. We would prefer that
you use python, java, Golang, or Scala, if you are comfortable doing so. If none of these are
comfortable, please choose a language that is both comfortable for you and suited to the task
like, node, ruby, or C.
If you use other libraries installed by a common package manager (ruby gems/bundler, npm,
pip), it is not necessary to commit the installed packages.
We write automated tests, and we would like you to do so as well.
If there are any complicated setup steps necessary to run your solution, please document them.

# Platform support
This will be run in a unix-ish environment (OS X). If you choose to use a compiled language,
please keep this in mind. Please use platform-agnostic constructs where possible (line-endings
and file-path-separators are two problematic areas).


Sample input:
![image](https://user-images.githubusercontent.com/2306656/186987057-eb637c3d-7cdb-4fbb-a65f-953eeffba0ed.png)

Expected output:

![image](https://user-images.githubusercontent.com/2306656/186987087-540a6d98-7d32-411c-9355-adcb0bfb74a5.png)













