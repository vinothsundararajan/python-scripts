#!/usr/bin/python
import os
from time import strftime
from win10toast import ToastNotifier
toaster = ToastNotifier()

#Reminder file location (Windows)
reminderFile = 'C:\\Vinoth\\Python\\GitHub\\python-scripts\\reminder\\taskreminder'

#Reminder file location (linux)
#reminderFile = '/mnt/python/python-scripts/taskreminder'

#function 

def taskReminder():
    fileDetails = open(reminderFile,'r')
    #currentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())#----------------- if we want GMT time zone.
    currentTime = strftime("%Y-%m-%d&%H:%M")              #----------------- 2019-12-12&16:07:29
    print (currentTime)
    flag = 0
    for task in fileDetails:
        print (task)
        if currentTime in task:
            flag = 1
            print (task)
            task = task.split(' ')
            print (task[1])
            toaster.show_toast("ALERT: Task Reminder:" " " + currentTime + " ",
                               'Hey Vinoth, This is just reminder alert to complete your task'" " + task[1] + " " + task[2] + 'thanks',
                               duration = 30,
                               icon_path = "taskreminder.ico",
                               threaded = True)
    else:
        flag = 0
#main function to describe all global variable and special functions.
if __name__ == "__main__":
    taskReminder()