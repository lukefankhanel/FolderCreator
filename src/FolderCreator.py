import os
import datetime

def main():
    dateDelimiter = "-"
    courseString = input("What is the list of courses? (Separated by a \",\"):")
    startString = input("What is the semester start date? (Of the format: dd/mm/yyyy):")
    endString = input("What is the semester end date? (Of the format: dd/mm/yyyy):")
    breakWeeks = input("Are there any break weeks in the semester? "
    + "(Of the format: dd/mm/year, dd/mm/yyyy, etc. - Press enter if none):")

    courseList = courseString.split(",")
    breakList = breakWeeks.split(",")
    
    c = CalendarCalculator(startString, endString, breakList, dateDelimiter)
    f = FolderCreator(os.getcwd(), courseList, c.calculateWeekList())
    
    print("Creating Directories...")
    f.createDirectoryStructure()
    print("Directories Created!")



class CalendarCalculator:
    def __init__(self, semesterStartDate, semesterEndDate, breakWeeks, dateDelimiter):
        self.semesterStartDate = self.findMostRecentMonday(self.convertToDateObject(semesterStartDate))
        self.semesterEndDate = self.findMostRecentMonday(self.convertToDateObject(semesterEndDate))
        self.dateDelimiter = dateDelimiter

        if breakWeeks[0] == "":
            self.breakWeeks = []
        else:    
            self.breakWeeks = self.convertDateWeeks(breakWeeks)
        

    def convertToDateObject(self, stringValue):
        splitString = stringValue.split("/")
        return datetime.date(int(splitString[2]), int(splitString[1]), int(splitString[0]))

    def findMostRecentMonday(self, date):
        mondayDifference = date.weekday()
        return date + datetime.timedelta(days=-mondayDifference)

    def convertDateWeeks(self, stringList):
        breakList = []
        for week in stringList:
            breakList.append(self.findMostRecentMonday(self.convertToDateObject(week)))
        return breakList

    def calculateWeekList(self):
        currentSemesterDate = self.semesterStartDate
        oneWeek = datetime.timedelta(days=7)
        weekList = []

        while(currentSemesterDate <= self.semesterEndDate):
            if currentSemesterDate not in self.breakWeeks:
                weekList.append(currentSemesterDate.strftime("%d" + self.dateDelimiter + "%b" + self.dateDelimiter + "%Y"))
            currentSemesterDate += oneWeek
        return weekList

class FolderCreator:
    def __init__(self, targetDir, courseList, weekList):
        self.targetDir = targetDir
        self.courseList = courseList
        self.weekList = weekList

    def createDirectoryStructure(self):
        for name in self.courseList:
            courseDir = self.targetDir + "\\" + name
            extraDir = courseDir + "\\" + "Extra"

            try:
                os.mkdir(courseDir)
                weekCount = 1
                for week in self.weekList:
                    folderName = "Week " + str(weekCount) + " (" + week + ")"
                    os.mkdir(courseDir + "\\" + folderName)
                    weekCount += 1
                
                os.mkdir(extraDir)
                open(extraDir + "\\Notes.txt", "w")
                open(extraDir + "\\Zoom.txt", "w")
            except Exception as e:
                print("Error: " + e)
            


if __name__ == "__main__":
    main()