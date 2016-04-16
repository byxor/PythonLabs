from collections import namedtuple

Student = namedtuple("Student", ["firstname", "surname", "id"])

def show_student(s):
	print("{:>11} {}".format("First name:", s.firstname))
	print("{:>11} {}".format("Surname:", s.surname))
	print("{:>11} {}".format("ID:", s.id))
