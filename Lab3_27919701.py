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

    def __repr__(self):
        return "Test for AssignmentClass-> assignmentName:%s ScoreList:%s Total:%s" % (self._description, self._score, self._total)



class CategoryAssignment(Assignment):
    def __init__(self, description, category, score, total):
        super(Assignment, self).__init__()
        self._description = description
        self._category = category
        self._score = score
        self._total = total

    def getCategory(self):
        return self._category

    def __repr__(self):
        return "Test for CategoryAssignment Class --> Category: %s  Description: %s  Score: %s Total: %s" %(self._category, self._description, self._score, self._total)


class Student:
    def __init__(self,idNumber): #for every student, an empty dictionary for all the assignments as the key names will be created
        self._idNumber = idNumber
        self._assignmentScoreList = []

    def getId(self):
        return int(self._idNumber)

    def getScore(self, assignmentName):
        for assignment in self._assignmentScoreList:
            if assignment._description == assignmentName:
                return float(assignment._score)

    def getScores(self):  
        return self._assignmentScoreList

    def addAssignment(self,assignment):
        self._assignmentScoreList.append(assignment)


    def changeScore(self, assignmentName, score):
        for assignment in self._assignmentScoreList:
            if assignment._description == assignmentName:
                assignment._score = score
                return        

    def removeScore(self, assignmentName):  
        for assignment in self._assignmentScoreList:
            if assignment._description == assignmentName:
                self._assignmentScoreList.remove(assignment)
                return
            else:
                pass   

    def getAssignmentScoreList(self):
        return self._assignmentScoreList

    def __repr__(self):
        return "Test for StudentClass-> StudentID:%s AssignmentScoreList:%s " % (self._idNumber, self._assignmentScoreList)


class Gradebook():
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
                return

    def search(self, idNum):
        for student in self._students:
            idNumber = student.getId()
            if idNumber == idNum:
                return student 

    def addAssignment(self, idNum, score:Assignment):
        for student in self._students:
            idNumber = student.getId()
            if student._idNumber == idNum:
                #print("ID matched")
                for x,assignment in enumerate(student._assignmentScoreList):
                    if score._description == assignment._description:
                        student._assignmentScoreList[x] = score
                        return

                student._assignmentScoreList.append(score)
            else:
                pass
                #print('ID not matched.')
                #print('student object after: ', student)

                 
    def __repr__(self):
        return "Test for GradebookClass-> EntireList of StudentObjects --> %s" %(self._students)

                
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

            #print('avg is: ',avg)
            #output.append(avg)
        return avg * 100
    
    def writeGradebookRecord(self, idNum, fileName):
        outfile = open(fileName, 'w')
        scores = []
        totals = []
        for student in self._students:
            idNumber = student.getId()
            if idNumber == idNum:
                #print('student found in gradebook')
                outfile.write(str(idNumber))
                outfile.write("\n")
                for assignment in student._assignmentScoreList:  ####
                    #print('assignment:', assignment)
                    des = assignment.getDescription()
                    outfile.write(des)
                    outfile.write("\n")
                    s = assignment.getScore()
                    scores.append(float(s))
                    t = assignment.getTotal()
                    totals.append(float(t))
                    outfile.write(str(int(s))+'/'+str(int(t)))
                    outfile.write("\n")
                
                numerator = int(sum(scores))
                denominator = int(sum(totals))
                outfile.write('Total: '+str(numerator)+'/'+str(denominator))
                outfile.write("\n")
                percentage = (numerator / denominator)*100
                outfile.write('Percentage: '+str(percentage))
                return
            
            else:
                outfile.write('Student Not Found')  

        outfile.close() 



'''g1 = TotalPointsGradebook()
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
g1.writeGradebookRecord(22222, '22222.txt')'''


class CategoryGradebook(Gradebook):
    def __init__(self):
        super(Gradebook, self).__init__()
        self._gradeWeights = {} #for adding categories and their weights
        self._students = []

    def addCategory(self, description, weight):
        self._description = description
        self._gradeWeights[self._description] = weight
        return

    def isBalanced(self):
        output = []
        for x in self._gradeWeights:
            output.append(self._gradeWeights[x])
        if sum(output) == 100:
            return True
        else:
            return False

    def writeGradebookRecord(self, idNum, fileName):
        outfile = open(fileName, 'w')
        dummy = []
        result = {}
        for student in self._students:
            idNumber = student.getId()
            if idNumber == idNum:
                #print('student found in gradebook')
                outfile.write(str(idNumber))
                outfile.write("\n")

                categories = self._gradeWeights.keys()
                print('categories are: ', categories)
                output = {}
                for category in self._gradeWeights:
                    output[category] = [],[]
                    result[category] = []
                    for assignment in student._assignmentScoreList:
                        if assignment.getCategory() == category:
                            #print('yay')
                            output[category][0].append(assignment._score)
                            output[category][1].append(assignment._total)
                            #print('output for assignment is: ', output)
                            
                            outfile.write(category + ': '+assignment._description)
                            outfile.write("\n")
                            #print('score: ', assignment._score)
                            #print('total: ',assignment._total)
                            
                            r = str(int(assignment._score))+'/'+str(int(assignment._total))
                            #print('string is: ',r)
                            outfile.write(r)
                            outfile.write("\n")
                            
                            
                        scores = sum(output[category][0])
                        totals = sum(output[category][1])
                        #print('scores: ', scores)
                        #print('totals: ', totals)
                    result[category].append(scores)
                    result[category].append(totals)
                    #print('result for assignment is: ', result)
                    avg = (result[category][0] / result[category][1])
                    
                    a = str(category+': '+str(avg*100))
                    dummy.append(a)
                    
                    result[category] = avg * self._gradeWeights[category]
                    print('final percentage for the category is:', result)
                    
                for line in dummy:
                    outfile.write(line)
                    outfile.write('\n')
                    
                finalPercentage = sum(result.values())
                print('final: ', finalPercentage)
                outfile.write('Percentage: '+str(finalPercentage))
                                  
                            
            else:
                outfile.write('Student Not Found')
        outfile.close()

    def classAverage(self): #According to the prompt, this method was a part of total points gradebook. But have added heree
        output = []
        self._score = 0
        self._total = 0
        for student in self._students:
            for assignment in student._assignmentScoreList:
                s = assignment.getScore()
                t = assignment.getTotal()
                self._score += s
                self._total += t
                #print('score and total:')
                #print(s,' ',t)
            avg = float(self._score / self._total)

            
        return avg * 100
                    

'''g1 = CategoryGradebook()
g1.addCategory('Labs', 30)
g1.addCategory('Midterm', 30)
g1.addCategory('Final', 40)

s1 = Student(11111)
s2 = Student(22222)

s1Lab1 = CategoryAssignment('Lab 1', 'Labs', 15, 20)
s2Lab1 = CategoryAssignment('Lab 1', 'Labs', 17, 20)
s1Lab2 = CategoryAssignment('Lab 2', 'Labs', 14, 20)
s2Lab2 = CategoryAssignment('Lab 2', 'Labs', 16, 20)
s1Mid = CategoryAssignment('Midterm', 'Midterm', 29, 32)
s2Mid = CategoryAssignment('Midterm', 'Midterm', 23, 32)
s1Fin = CategoryAssignment('Final Exam', 'Final', 42, 50)
s2Fin = CategoryAssignment('Final Exam', 'Final', 46, 50)

g1.addStudent(s1)
g1.addStudent(s2)
g1.addAssignment(11111, s1Lab1)
g1.addAssignment(11111, s1Lab2)
g1.addAssignment(11111, s1Mid)
g1.addAssignment(11111, s1Fin)
g1.addAssignment(22222, s2Lab1)
g1.addAssignment(22222, s2Lab2)
g1.addAssignment(22222, s2Mid)
g1.addAssignment(22222, s2Fin)'''     
            
