class Assignment:
    def __init__(self, description, score, total):
        self._description = description
        self._score = score
        self._total = total

    def getDescription(self):
        return self._description

    def getScore(self): 
        return float(self._score)

    def getTotal(self):
        return float(self._total)

    def changeScore(self, newscore):
        self._score = newscore
        #return self._score


class CategoryAssignment(Assignment):
    def __init__(self, description, category, score, total):
        super(Assignment, self).__init__()
        self._description = description
        self._category = category
        self._score = score
        self._total = total

    def getCategory(self):
        return self._category


class Student:
    def __init__(self,idNumber,assignmentScoreList = {}):
        self._idNumber = idNumber
        self._assignmentScoreList = assignmentScoreList

    def getId(self):
        return int(self._idNumber)

    def getScore(self, assignmentName):
        return int(self._assignmentScoreList[assignmentName])

    def getScores(self):  ## Return what? Just the scores of all assignments? I
        return self._assignmentScoreList

    def addAssignment(self,assignment):
        des = assignment.getDescription()
        score = assignment.getScore()
        self._assignmentScoreList[des] = score

    def changeScore(self, assignmentName, score):
        if assignmentName in self._assignmentScoreList:
            self._assignmentScoreList[assignmentName] = score
        else:
            pass

    def removeScore(self, assignmentName):  ## Remove the key altogether?
        #Or just set the score for that assignment to perhaps ''(an empty string)?
        if assignmentName in self._assignmentScoreList:
            del self._assignmentScoreList[assignmentName]
        else:
            pass

    def getAssignmentScoreList(self):
        return self._assignmentScoreList


class Gradebook:
    def __init__(self):
        self._students = []

    def addStudent(self, student:Student):
        if student not in self._students:
            self._students.append(student)

    def dropStudent(self,idNum):
        for student in self._students:
            idNumber = student.getId()
            if idNumber == idNum:
                self._students.remove(student)

    def search(self, idNum):
        for student in self._students:
            print(student)
            idNumber = student.getId()
            if idNumber == idNum:
                return str(student)  #returns the location in memory, and not the var

    def addAssignment(self, idNum, score:Assignment):
        for student in self._students:
            idNumber = student.getId()
            if idNumber == idNum:
                for assignment in student._assignmentScoreList:
                    des = assignment.getDescription()
                    if des == score._description:
                        student._assignmentScoreList[des] = score
                        return 

                
class TotalPointsGradebook(Gradebook):
    def __init__(self):
        super(Gradebook, self).__init__()
        self._score = 0
        self._total = 0
        self._students = []

    def classAverage(self):
        output = []
        for student in self._students:
            for assignment in student._assignmentScoreList:
                s = assignment.getScore()
                t = assignment.getTotal()
                self._score += s
                self._total += t
            avg = float(self._score / self._total)
            output.append(avg)
        return sum(output) / len(output)


    def writeGradebookRecord(self, idNum, fileName):
        outfile = open(fileName, 'w')
        scores = []
        totals = []
        for student in self._students:
            idNumber = student.getId()
            if idNumber == idNum:
                print('student found in gradebook')
                outfile.write(str(idNumber))
                outfile.write("\n")
                for assignment in student._assignmentScoreList:  ####
                    print('assignment:', assignment)
                    des = student._assignmentScoreList[assignment].getDescription()
                    outfile.write(des)
                    outfile.write("\n")
                    print('des is:', des)
                    s = assignment.getScore()
                    print('score is: ', s)
                    scores.append(float(s))
                    print('scores: ', scores)
                    t = assignment.getTotal()
                    totals.append(float(t))
                    print('totals: ', totals)
                    outfile.write(str(s)+'/'+str(t))
                
                numerator = sum(scores)
                denominator = sum(totals)
                outfile.write('Total: '+str(numerator)+'/'+str(denominator))
                outfile.write("\n")
                #percentage = (numerator / denominator)*100
                #outfile.write('Percentage: ',percentage)
            
            else:
                outfile.write('Student Not Found')

        outfile.close()  



g1 = TotalPointsGradebook()
s1 = Student(11111)
a1 = Assignment('Midterm', 28, 30)
a2 = Assignment('Final', 46, 50)
g1.addStudent(s1)
g1.addAssignment(11111, a1)
g1.addAssignment(11111, a2)
s2 = Student(22222)
a3 = Assignment('Midterm', 21, 30)
a4 = Assignment('Final', 34, 50)
g1.addStudent(s2)
g1.addAssignment(22222, a3)
g1.addAssignment(22222, a4)
print('Done')
g1.writeGradebookRecord(11111, '11111.txt')

'''g1 = Gradebook()
s1 = Student(12345)
a1 = Assignment('Lab 1', 15, 15)
g1.addStudent(s1)
g1.addAssignment(12345, a1) '''            
        
        

