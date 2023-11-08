class Student():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname 
        self.TNumber = tnumber 
        self.Grades = scores
inputfile = open("10.Project Student Scores.tx")
x = inputfile.readline()
def RunningAverage(self):
    y = x.split(',')
    runningaverage = self.Grades // num_grades
    return runningaverage
def TotalAverage(self):
    totalaverage = self.Grades // num_grades
    return totalaverage
def LetterGrade(self):
    TotalAverage >= 90:
    print("A")
    TotalAverage >= 80 < 90:
    print("B")
    TotalAverage >= 70 < 80:
    print("C")
    TotalAverage >= 60 < 70:
    print("D")
    TotalAvergae < 60:
    print ("F")
print(RunningAverage.__format__,(""))
print(TotalAverage.__format__,(""))
print(LetterGrade.__format__,(""))