#INF601 - Advanced Programming in Python
#Eric Worsham
#Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

def bmiandoutcome():
    bmidata = list(data['BMI'])
    outcomedata = list(data['Outcome'])

    # This plots the graph
    plt.plot(outcomedata, bmidata)

    # Set our labels for the graph
    plt.xlabel("Diagnosis")
    plt.ylabel("BMI")
    plt.title("Correlation between High BMI and Positive Diabetic Diagnosis")

    # Saves plot

    savefile = "charts/bmi_outcome.png"
    plt.savefig(savefile)

    # Show the graph
    plt.show()

def bloodpressureoutcome():
    bpdata = list(data['BloodPressure'])
    outcomedata = list(data['Outcome'])

    # This plots the graph
    plt.plot(outcomedata, bpdata)

    # Set our labels for the graph
    plt.xlabel("Diagnosis")
    plt.ylabel("Blood Pressure")
    plt.title("Correlation between High Blood Pressure and Positive Diabetic Diagnosis")

    # Saves plot

    savefile = "charts/bp_outcome.png"
    plt.savefig(savefile)

    # Show the graph
    plt.show()

def obesebmiwithbp():
    obese_bmi = list(data['BMI'][(data['BMI'] >= 30)])
    obese_bmi_bp = list(data['BloodPressure'][(data['BMI'] >= 30)])

    # This plots the graph
    plt.scatter(obese_bmi, obese_bmi_bp)

    #Using Log Scale to try and remove outlier skewing
    plt.xscale('log')
    plt.yscale('log')

    # Set our labels for the graph
    plt.xlabel("BMI for those with a BMI >= 30")
    plt.ylabel("Blood Pressure for BMI >= 30")
    plt.title("Blood Pressure of those with a BMI of 30 or More")

    # Saves plot

    savefile = "charts/bp_correlation_bmi.png"
    plt.savefig(savefile)

    # Show the graph
    plt.show()

data = pd.read_csv('diabetes.csv')

# Create our charts folders
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

bmiandoutcome()

bloodpressureoutcome()

obesebmiwithbp()






