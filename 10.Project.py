class Student():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname 
        self.TNumber = tnumber 
        self.Scores = scores
    def RunningAverage(self):
        totalscore = 0.0
        totalcount = 0
        for i in range(len(self.Scores)):
            if self.Scores[i].strip() != "":
                totalcount += 1
                totalscore += float(self.Scores[i])
        return totalscore / totalcount
    def TotalAverage(self):
        totalscore = 0.0
        for i in range (len(self.Scores)):
            if self.Scores[i].strip() != "":
                totalscore += float(self.Scores[i])
        return totalscore / len(self.Scores)
    def LetterGrade(self):
        totalAverage = self.TotalAverage()
        if totalAverage >= 90:
            return "A"
        if totalAverage >= 80:
            return "B"
        if totalAverage >= 70:
            return "C"
        if totalAverage >= 60:
            return "D"
        return "F"
studentsfile = open("10.Project Student Scores.txt")
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("Name","Name","Number", "Average", "Average", "Grade"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("-"*12,"-"*12,"-"*12,"-"*12,"-"*12,"-"*12))
x = studentsfile.readline()
while x != "":
    y = x.split(",")
    Student1 = Student(y[0].strip(), y[1].strip(), y[2].strip(),y[3:])
    print("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12s}".format(Student1.FirstName, Student1.LastName, Student1.TNumber, Student1.RunningAverage(), Student1.TotalAverage(),Student1.LetterGrade()))
    x = studentsfile.readline()
studentsfile.close()