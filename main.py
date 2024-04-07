# Impor the flask libary that allows for hosing a document on a local server
from flask import Flask

# This is a class for each skill, containing the name, level, and descrption
class Skill:
    def __init__(self, name, level, desc):
        self.name = name
        self.level = level
        self.desc = desc

# This is a list of all of the skill object
all_skills = [
    Skill("Python", 1, "The basics of python"),
    Skill("Variables", 1, "Creating variables"),
    Skill("Functions", 1, "Creating functions"),
    Skill("Modules", 2, "Using modules and libraies"),
    Skill("Flask", 3, "Hosting a webpage using flask"), 
    Skill("JSON", 2, "Working with JSON"),
    Skill("Pygame", 4, "Creating games using pygame"),
    Skill("SQLite3", 2, "Working with datbases"),
    Skill("Classes", 3, "Creating classes"),
    Skill("OOP", 4, "Object Oriented Programming"),
    ]
# Create a webapp with the flask class using the name of the project
web_app = Flask(__name__)

# Set the default route
@web_app.route("/")
# Function for the home page
def home_page():
    # Initialize the document string
    document = "<br><br><h1>Preston C. Python Camp</h1><br>"
    # Array of the opening information
    opening = [
        "Welcome to Preston C. Python Camp",
        "<br> this camp is to help you understand how to code in Python,",
        "we will be going over many things such as functions, libarries, classes, object orentated programing, and much more!",
        "This 5 week class will help you get in the mindset of a coder, and help you improve.",
        "No matter your skill or experience this camp is for you, and will assist you no matter what!"
        ]
    # For each line of the opening, append to the document
    for line in opening:
        document += line
    # Create the skills section
    skills = "<br><br><h2>Skills</h2>"
    # For each skill, appened the respective infomraiton to the skills section
    for skill in all_skills:
        skills += f"<h3>{skill.name}</h3>"
        skills += f"<br>Level: {skill.level}"
        skills += f"<br>Description: {skill.desc}"
    # Return the document and skills section
    return document + skills

# Run the web app
if __name__ == "__main__":
    web_app.run()
    