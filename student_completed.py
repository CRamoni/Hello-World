
class Student(object):

    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades

    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        print ("The average for student " + self.name + " is " + str(average))

    def check_male(self):
                if Student =="Male":     
                    return True
                else:
                    return False
                
mike = Student(20, "Philani Sithole", "Male",[64,65])

sarah = Student(19, "Sarah Jones", "Female",[82,58])

kabelo = Student(31, "Kabelo Brown","Male",[85,85])


studentList = [mike,sarah,kabelo]

for list in range(len(studentList)):
    print("The gender provided is",studentList[list].check_male(),studentList[list].compute_average()) 


