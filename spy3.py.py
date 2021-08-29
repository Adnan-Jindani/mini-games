#imports
from guizero import App, Text, PushButton
from random import choice

#Function
def choose_name():
    #print("The button was pressed")
    first_names = ["Virat", "Samrat", "Pakhi", "Saee", "Bhawani", "Mohit"]
    last_names = ["Joshi", "Deshpande", "Chavan", "Singh"]
    spy_name = choice(first_names) + " " + choice(last_names)
    print(spy_name)
    name.value = spy_name
    
#App
app = App("TOP SECRET")

#WIDGETS
title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text = "Tell me!")
button.bg = "red"
button.text_size = 50
name = Text(app, "")

#display
app.display()