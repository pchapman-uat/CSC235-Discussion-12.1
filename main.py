from flask import Flask

class Skill:
    def __init__(self, name, level, desc):
        self.name = name
        self.level = level
        self.desc = desc

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
web_app = Flask(__name__)

@web_app.route("/")
def home_page():
    document = ""
    opening = [
        "<br><br><h1>Preston C. Python Camp</h1>",
        "<br>",
        "Welcome to Preston C. Python Camp",
        "<br> this camp is to help you understand how to code in Python,",
        "we will be going over many things such as functions, libarries, classes, object orentated programing, and much more!",
        "This 5 week class will help you get in the mindset of a coder, and help you improve.",
        "No matter your skill or experience this camp is for you, and will assist you no matter what!"
        ]
    for line in opening:
        document += line
    skills = "<br><br><h2>Skills</h2>"
    for skill in all_skills:
        skills += f"<h3>{skill.name}</h3>"
        skills += f"<br>Level: {skill.level}"
        skills += f"<br>Description: {skill.desc}"
    return document + skills


if __name__ == "__main__":
    web_app.run()
    