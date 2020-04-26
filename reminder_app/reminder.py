#!/usr/bin/python

import time
import os
from win10toast import ToastNotifier
toaster = ToastNotifier()

# For Windows:
birthdayFile = 'C:\\Vinoth\\Python\\python-scripts\\reminder\\reminderfile.txt'
# For Linux:
#birthdayFile = '/mnt/python-scripts/reminder/reminderfile.txt'
#
def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
#       print (line.split(' '))
        if today in line:
            flag = 1
            line = line.split(' ')
            #print (line[2] + ' ' + line[1])
            toaster.show_toast("BIRTHDAY REMINDER TODAY",
                               'This is reminder to wish'" " + line[1] + " " + line[2] + 'as his birthday today',
                               duration = 5,
                               icon_path = "reminder.ico",
                               threaded = True)
    if flag == 0:
        toaster.show_toast("No Birthday Today",
                           "Kindly Ignore this note",
                           icon_path = "reminder.ico",
                           duration = 10,
                           threaded = True)
if __name__ == '__main__':
    checkTodaysBirthdays()