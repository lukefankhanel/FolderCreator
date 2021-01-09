import os
import datetime

def main():
    #print(os.getcwd())
    # x = datetime.date(2021, 1, 9)
    # mondayDiff = x.weekday()
    # x = x + datetime.timedelta(days=-mondayDiff)
    # print(x.strftime("%d/%m/%Y"))

    c = CalendarCalculator("06/01/2021","28/2/2021", "-")
    # print(c.semesterStartDate.strftime("%d/%m/%Y"))
    wlist = c.calculateWeekList()

    print(wlist)


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
        pass

    def createDirectoryStructure(self):
        pass

    def createFolder(self):
        pass

    def createTextFile(self):
        pass


if __name__ == "__main__":
    main()