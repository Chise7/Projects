from datetime import date
import re

def startup():
    today = date.today() #Gets todays date
    print("<----------------------------------------------------------------------------->")
    print("\nWelome to Schedule Mk2!\n")
    print("Today is ",end = '')
    print(today)
    file = open("Scheduler/Schedule.txt","r")
    schedule = file.readlines()
    file.close()
    return(schedule)

def todaysTasks(scheduleLines):
    today= str(date.today())
    hasDay = False
    for line in scheduleLines:
        if(re.search(today,line) != None):
            todaysline = line
            hasDay = True
    if(hasDay):
        print("Today's Tasks:")
        tasks = todaysline.split(':')
        for i in range(1,len(tasks)):
            print(str(i)+". ",end="")
            print(tasks[i])
    else:
        print("There Are No Tasks Today!")
    return
            
def addTasks(scheduleLines, givenDate = 0):
    # spaceStopper = re.compile(r"^\:\s$")
    monthsList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    nonvalidMonth = True
    dayExist = False
    tasksAdd = input("What tasks would you like to add? (Please separate tasks with a comma): ")
    tasksList = tasksAdd.split(',')
    if(givenDate == 0):
        while(nonvalidMonth):
            dateAdd = (input("What date do you want to add these tasks to?(Month, Day): ")).split(',')
            if(dateAdd[0] not in monthsList):
                print("Error! Non-Valid Month!")
            else:
                nonvalidMonth = False
        validDate = dayConv(dateAdd)
    else:
        validDate = givenDate
    for i in range(len(scheduleLines)):
        # re.sub(spaceStopper,":",scheduleLines[i])
        if(re.search(validDate,scheduleLines[i]) != None):
            for task in tasksList:
                scheduleLines[i] = scheduleLines[i] + ':' + task
            dayExist = True
            daysTasks = scheduleLines[i].split(":")
            print("Tasks for "+validDate+":")
            for i in range(len(daysTasks[1:])):
                print(str(i)+". "+daysTasks[i])
    if(not dayExist):
        newDay = validDate
        for task in tasksList:
            newDay += ":"+task
        scheduleLines.append("\n"+newDay)
        print("Tasks for "+validDate+":")
        for i in range(len(tasksList)):
            print(str(i+1)+". "+tasksList[i])
    return(scheduleLines)

def viewOther(scheduleLines):
    monthsList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    nonvalidMonth = True
    dayExist = False
    while(nonvalidMonth):
        datefind = (input("What date do you want to see?(Month, Day): ")).split(',')
        if(datefind[0] not in monthsList):
            print("Error! Non-Valid Month!")
        else:
            nonvalidMonth = False
    validDate = dayConv(datefind)
    for day in scheduleLines:
        if(re.search(validDate,day) != None):
            tasksList = day.split(":")
            print("Tasks For ",end="")
            print(validDate+":")
            for i in range(1,len(tasksList)):
                print(str(i)+". ",end="")
                print(tasksList[i])
            dayExist = True
    if(not dayExist):
        print("No Tasks for this Day!")
        addExtra = input("Would you like to add tasks?[Y/N]: ")
        if(addExtra == "Y"):
            scheduleLines = addTasks(scheduleLines, validDate)
    return(scheduleLines)

def closeDown(scheduleLines):
    print("Have a Nice Day!\n")
    print("<----------------------------------------------------------------------------->")
    file = open("Scheduler/Schedule.txt","w")
    file.writelines(scheduleLines)
    file.close()
    
def dayConv(monthDay): #Converts [Month, Day] to useable format
    year = str(date.today().year)
    day = int(monthDay[1])
    if(day < 10):
        realDay = "0"+str(day)
    else:
        realDay = monthDay[1].strip()
    if(monthDay[0]== "January"):
        convDate = "01-"+realDay
    if(monthDay[0]== "February"):
        convDate = "02-"+realDay
    if(monthDay[0]== "March"):
        convDate = "03-"+realDay
    if(monthDay[0]== "April"):
        convDate = "04-"+realDay
    if(monthDay[0]== "May"):
        convDate = "05-"+realDay
    if(monthDay[0]== "June"):
        convDate = "06-"+realDay
    if(monthDay[0]== "July"):
        convDate = "07-"+realDay
    if(monthDay[0]== "August"):
        convDate = "08-"+realDay
    if(monthDay[0]== "September"):
        convDate = "09-"+realDay
    if(monthDay[0]== "October"):
        convDate = "10-"+realDay
    if(monthDay[0]== "November"):
        convDate = "11-"+realDay
    if(monthDay[0]== "December"):
        convDate = "12-"+realDay
    convDate = year +"-"+ convDate
    return(convDate)

def main():
    schedule = startup() #Bootup function to welcome user
    try: 
        action = input("How Can I help you? Type TODAY for todays tasks, ADD to add a task, VIEW to view another day's tasks, or EXIT to close.")
    finally: 
        while(action != "EXIT"): ##CLoses App when user selects exit
            if(action == "ADD"):
                schedule = addTasks(schedule) #Adds Tasks
            if(action == "VIEW"):
                schedule = viewOther(schedule) #Displays Other Tasks
            if(action == "TODAY"):
                todaysTasks(schedule) #Displays Today's Tasks
            if(action != "EXIT" and action !="ADD" and action != "VIEW" and action != "TODAY"):
                print("Uh Oh! We didnt quit get that, please try again.") #Error Handling
            action = input("How else can I help you? Type TODAY for todays tasks, ADD to add a task, VIEW to view another day's tasks, or EXIT to close.")
        closeDown(schedule)#Closes out app
    return


if __name__ == "__main__":
    main()
    


