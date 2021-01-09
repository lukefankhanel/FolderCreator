import os
import datetime

def main():
    #print(os.getcwd())
    x = datetime.date(2021, 1, 9)
    mondayDiff = x.weekday()
    x = x + datetime.timedelta(days=-mondayDiff)
    print(x.strftime("%d/%m/%Y"))


class CalendarCalculator:
    def __init__(self, semesterStartDate, semesterEndDate, dateDelimiter):
        pass

    def convertToDateObject(self, stringValue):
        pass

    def findMostRecentMonday(self, date):
        pass

    def calculateWeekList(self):
        pass

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