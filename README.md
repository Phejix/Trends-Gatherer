#Google Trends v2

##Introduction
A command line tool which calls the unofficial Python Google Trends API for a set period of time.
Currently supports up to 5 keywords at a time and will call between two date ranges (furthest back appears to be 3 years)
to pull search volume data from trends. Results are currently delivered at the minute level but this could be changed to support hours or potentially days or weeks if necessary.

##Installation
Install a virtual environment (if unfamiliar with virtual environments see below).

Drag all contents of GoogleTrends_V2 into the directory that the virtual environment is in.

Open the command line or Powershell in that directory (you can shift right click, "open Powershell" for a shortcut)

Start your virtual environment (see virtual enviornments section below if unfamiliar)

Type

    pip install -r requirements.txt

and press Enter.

Python will now install the required packages to the virtual environment.

Once it is complete you are ready to run the program.

##Running The Program
Open the command line or Powershell in the directory where you installed the tool.

Open a virtual environment (if it is not already open)

Type

    python googletrends.py x

where 'x' is a single keyword.

For keywords of more than one word (such as "car insurance"), wrap the terms inside of double quotes.

    python googletrends.py "car insurance"

Press Enter to run and follow the instructions for entering the required dates.

If more than one keyword is needed simply add them after the first one, separated by a single space.

You can have a maximum of 5 (per the API's requirements)

Example:

    python googletrends.py dinosaurs tyrannosaurus stegasaurus

Will gather me the data of all three of those keywords compared against one another.

##Dates
Dates are entered in the format YYYY-MM-DD HH and you will be instructed once you have completed the steps above.

##Output
Currently the program will output to a csv in the directory you are running the program in.

##Virtual Environments
To install a virtual environment navigate on the command line or Powershell to the directory you want to run your code from.

Type in

    python -m venv .venv

Press Enter.

A new line will appear when the installation is complete and you will see a folder called .venv in your directory.

To start the virtual environment:

Navigate on the command line or Powershell to the directory you installed your virtual environment.

Type in

    .venv/Scripts/activate

Press Enter.

If successful a curly bracket will appear on the left most side of your directory looking like this:

    (.venv) C:/Path/To/Your/Code...

