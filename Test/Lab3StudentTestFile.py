import unittest
from Lab3_27919701 import *
# You must import your script name (ex: Lab3_12345678), no file extension,
# followed by import *
# example: from Lab3_12345678 import *
# You must also add LAB3TEST_OUTPUT_11111.txt and LAB3TEST_OUTPUT_22222.txt
# in the same folder as your running script


class Lab3StudentTest(unittest.TestCase):
    #Tests the Assignment Class
    def test1(self):
        a1 = Assignment('Description 1234', 9, 10)
        self.assertEqual( a1.getDescription(), 'Description 1234')
        self.assertEqual( a1.getScore(), 9)
        self.assertEqual( a1.getTotal(), 10)
        a1.changeScore(8)
        self.assertEqual( a1.getScore(), 8)

    #Tests the CategoryAssignment Class
    def test2(self):
        c1 = CategoryAssignment('Description ABC', 'Lab', 15, 18)
        self.assertEqual( c1.getDescription(), 'Description ABC')
        self.assertEqual( c1.getCategory(), 'Lab')
        self.assertEqual( c1.getScore(), 15)
        self.assertEqual( c1.getTotal(), 18)

    #Tests the Student Class
    def test3(self):
        s1 = Student(12345)
        a1 = Assignment('Assignment 1', 6, 10)
        a2 = Assignment('Assignment 2', 4, 12)
        s1.addAssignment(a1)
        s1.addAssignment(a2)
        self.assertEqual(s1.getScore('Assignment 1'), 6)
        self.assertEqual(s1.getId(), 12345)
        s1.changeScore('Assignment 2', 9)
        self.assertEqual(s1.getScore('Assignment 2'), 9)
        s1.removeScore('Assignment 2')

    #Tests the Gradebook Class
    def test4(self):
        g1 = Gradebook()
        s1 = Student(12345)
        a1 = Assignment('Lab 1', 15, 15)
        g1.addStudent(s1)
        g1.addAssignment(12345, a1)
        self.assertEqual(g1.search(12345), s1)
        g1.dropStudent(12345)

    #Tests the TotalPointsGradebook Class
    def test5(self):
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
        g1.writeGradebookRecord(11111, '11111.txt')
        self.assertEqual(g1.classAverage(), 80.625)
        xFile = open('11111.txt', 'r')
        yFile = open('LAB3TEST_OUTPUT_11111.txt', 'r')
        for line in xFile:
            self.assertEqual( yFile.readline(), line)
        xFile.close()
        yFile.close()
        g1.writeGradebookRecord(12345, 'nf.txt')
        zFile = open('nf.txt', 'r')
        self.assertEqual(zFile.readline(), 'Student Not Found')
        zFile.close()
        
    #Tests the CategoryGradebook Class
    def test6(self):
        g1 = CategoryGradebook()
        g1.addCategory('Labs', 30)
        g1.addCategory('Midterm', 30)
        self.assertEqual(g1.isBalanced(), False)
        g1.addCategory('Final', 40)
        self.assertEqual(g1.isBalanced(), True)
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
        g1.addAssignment(22222, s2Fin)
        self.assertEqual(g1.classAverage(), 82.825)
        g1.writeGradebookRecord(22222, '22222.txt')
        xFile = open('22222.txt', 'r')
        yFile = open('LAB3TEST_OUTPUT_22222.txt', 'r')
        for line in xFile:
            self.assertEqual( yFile.readline(), line)
        xFile.close()
        yFile.close()
        g1.writeGradebookRecord(12345, 'nf.txt')
        zFile = open('nf.txt', 'r')
        self.assertEqual(zFile.readline(), 'Student Not Found')
        zFile.close()
    
    
        

if __name__ == "__main__":
    unittest.main()
