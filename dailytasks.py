import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime
import csv
import time
from time import sleep

root = tk.Tk()
root.title("Daily Tasks")
root.geometry('550x450')

name_t = tk.StringVar()
comms = tk.StringVar()
filename = "tester.csv"

teams = [
    "24x7",
    "Store Support",
]

tasks_247 = [
    "Alerts Queue",
    "PRTG Alerts",
    "Cradlepoint Check"
    ]

tasks_ss = [
    "Store Poller",
    "Failed MPOS Orders",
    "Missing Stores NA",
    "Missing Stores EU",
    "Till Integrity",
    "Repolls",
    "AP Alerts",
    "Grafana",
    "Mobile Replacement Report",
    ]

def remove_result():
    result.config(text = "Click to Submit")

def pick_tasks(e):
    if teamCombo.get() == "24x7":
        taskCombo.config(value=tasks_247)
        taskCombo.current()
    if teamCombo.get() == "Store Support":
        taskCombo.config(value=tasks_ss)
        taskCombo.current()


def submit():

    entries = []
    #Get input name from entry field
    entries.append(name_t.get())
    
    #Get Store Team from dropdown
    entries.append(teamCombo.get())
    
    #Get Task from dropdown
    entries.append(taskCombo.get())

    #Get Comments text
    entries.append(comments.get("1.0", tk.END+"-1c"))

    #Get current time of submission
    current_time = datetime.datetime.now()
    entries.append(current_time)

    print("The current time is ", current_time)

    #Write the user input to a csv file
    with open('DailyTaskLog.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(entries)

    #with open('DailyTaskLog.csv', 'w') as f:
            #for ent in entries:
                #print(ent, file=f)

    #Set fields to blank after button is pressed
    name_t.set("")
    teamCombo.set("")
    taskCombo.set("")
    comments.delete("1.0", END)

    #Submission Success
    result.config(text = "Submission Completed")

    root.after(5000, remove_result)

#Title
title = ttk.Label(root, text = "Daily Tasks Sign-Off", font = ("Times New Roman", 15))
title.grid(row=0, column=1, padx=10, pady=10)

#Name Entry
nameLabel = ttk.Label(root, text = "Enter Name:", font = ("Times New Roman", 10))
nameLabel.grid(row=1, column=0, padx=10, pady=10)
nameEntry = tk.Entry(root, textvariable = name_t).grid(row = 1, column = 1)

#Selecting team
teamsLabel = ttk.Label(root, text = "Select Team:", font = ("Times New Roman", 10))
teamsLabel.grid(row=2, column=0, padx=10, pady=10)
teamCombo = ttk.Combobox(root, value = teams)
teamCombo.grid(column=1,row=2, pady=10)
teamCombo.current()
teamCombo.bind("<<ComboboxSelected>>", pick_tasks)

#Selecting Task
taskLabel = ttk.Label(root, text = "Choose Task:", font = ("Times New Roman", 10))
taskLabel.grid(row=3, column=0, padx=10, pady=10)
taskCombo = ttk.Combobox(root, value = [""])
taskCombo.grid(column=1,row=3, pady=10)
taskCombo.current()

#Comment Section
commentsLabel = ttk.Label(root, text = "Comments:", font = ("Times New Roman", 10))
commentsLabel.grid(row=4, column=0, padx=10, pady=10)
comments = Text(root, font = ("Times New Roman", 10), height = 10, width = 60)
comments.grid(row=4, column=1, pady=10)
#comments = tk.Entry(root, textvariable = comms, height = 10, width = 60).grid(row = 4, column = 1, pady=10)

#Submit Button
submitButton = ttk.Button(root, text="Submit", command = submit)
submitButton.grid(row=5, column = 1, pady=10)

#Submission Label
result = ttk.Label(root, text = "Click to Submit", font = ("Times New Roman", 10))
result.grid(row=6, column=1, padx = 10, pady = 10)

root.mainloop()
