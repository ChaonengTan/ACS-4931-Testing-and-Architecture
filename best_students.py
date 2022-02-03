# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

# TODO: Use 'extract method' refactoring technique to improve this code.
# TODO: If required, use 'replace temp variable with query' technique to make it easier to extract methods.

class Employer:
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        passed_students = []
        for s in self.students:
            if s.get_gpa() > 2.5:
                passed_students.append(s)

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')
        # Send congrat emails to them.
        for s in passed_students:
            s.send_congrat_email()
        # Find the top 10% of them and send their contact to the top employers
        passed_students.sort(key=lambda s: s.get_gpa())
        index = int(0.9 * len(passed_students))
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(passed_students[index:])

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()
