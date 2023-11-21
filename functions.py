# author: @Luca Stöhr, 2011.2023
# Version: 0.1
# script Intent: providing background functionality for main.py
''' 
#################################################################
Structure:
 - work: time per week, fixed slots or flexible time, location,
 priority, max time per day
 - sport: time per week, fixed slots or flexible time, location,
 priority, max time per day
 - sleep: time, location?, priority
 - orga/cleaning: time per week, occurence, priority
 - activity: one time or multiple times, time, location, priority
 - leasure: filling empty space, priority
 - all: preperation, processing, structuring, partner, export
#################################################################
'''

class User:

    def __init__(self, name):
        self.name = name
        self.sleep = self.Sleep()
        self.breakfast = self.Breakfast()
        self.dinner = self.Dinner()
        self.work = []
        self.sport = []
        self.orga_clean = []
        self.activity = []

    class Work:
        priority = 1
        maxh_day = 8
        preperation = 0.5
        processing = 0.5
        def __init__(self, title, duration, location, fixed_slot=False):
            self.title = title
            self.duration = duration
            self.location = location
            if fixed_slot:
                self.day, self.start_t = set_slot()
                self.end_t = self.start_t + self.duration

    class Sport:
        priority = 4
        maxh_day = 2
        days_row = 2
        preperation = 0.5
        processing = 0.5
        def __init__(self, sport, duration, location, fixed_slot=False):
            self.sport = sport
            self.duration = duration
            self.location = location
            if fixed_slot:
                self.day, self.start_t = set_slot()
                self.end_t = self.start_t + self.duration

    class Orga_Clean:
        priority = 3
        def __init__(self, task, duration, periodicity, fixed_days=False):
            self.task = task
            self.duration = duration
            self.periodicity = periodicity
            if fixed_days:
                self.day, self.days = set_days()
                # self.last_day = self.day + self.days
    
    class Activity:
        priotity = 2
        def __init__(self, activity, time, day, duration, one_event=True):
            self.activity = activity
            self.time = time
            self.day = day
            self.duration = duration
            if not one_event:
                self.periodicity = input("Please input Periodicity:")
                print(self.periodicity)

    class Sleep:
        daily = True
        priority = 2
        duration = 8
        start_t = (22, 24)
        preperation = 0.75
        processing = 0.25

    class Breakfast:
        daily = True
        priority = 2
        duration = 0.5

    class Dinner:
        daily = True
        priority = 2
        duration = 0.5
        start_t = (19, 21)


def set_slot():
    day = input("Day:")
    print(day)
    start_t = input("Start Time:")
    print(start_t)
    return day, start_t

def set_days():
    day = input("Day:")
    print(day)
    days = input("How many days, do you have:")
    print(days)
    return day, days

