import os
import datetime

def main():
    #print(os.getcwd())
    # x = datetime.date(2021, 1, 9)
    # mondayDiff = x.weekday()
    # x = x + datetime.timedelta(days=-mondayDiff)
    # print(x.strftime("%d/%m/%Y"))

    c = CalendarCalculator("06/01/2021","28/2/2021", "-")
    f = FolderCreator(os.getcwd(), ["Hello", "Hello2"], c.calculateWeekList())
    
    print("Creating Directories...")
    f.createDirectoryStructure()
    print("Directories Created!")


class CalendarCalculator:
    def __init__(self, semesterStartDate, semesterEndDate, dateDelimiter):
        self.semesterStartDate = self.findMostRecentMonday(self.convertToDateObject(semesterStartDate))
        self.semesterEndDate = self.findMostRecentMonday(self.convertToDateObject(semesterEndDate))
        self.dateDelimiter = dateDelimiter

    def convertToDateObject(self, stringValue):
        splitString = stringValue.split("/")
        return datetime.date(int(splitString[2]), int(splitString[1]), int(splitString[0]))

    def findMostRecentMonday(self, date):
        mondayDifference = date.weekday()
        return date + datetime.timedelta(days=-mondayDifference)

    def calculateWeekList(self):
        currentSemesterDate = self.semesterStartDate
        oneWeek = datetime.timedelta(days=7)
        weekList = []

        while(currentSemesterDate <= self.semesterEndDate):
            weekList.append(currentSemesterDate.strftime("%d" + self.dateDelimiter + "%m" + self.dateDelimiter + "%Y"))
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

            os.mkdir(courseDir)
            weekCount = 1
            for week in self.weekList:
                folderName = "Week " + str(weekCount) + " (" + week + ")"
                os.mkdir(courseDir + "\\" + folderName)
                weekCount += 1
            
            os.mkdir(extraDir)
            open(extraDir + "\\Notes.txt", "w")
            open(extraDir + "\\Zoom.txt", "w")


if __name__ == "__main__":
    main()