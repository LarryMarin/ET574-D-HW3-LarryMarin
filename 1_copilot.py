# list of three students named Jon, Kim and Lee

# function to print ‘Hi name’ for each student in the list
def print_greetings(students):
    for student in students:
        print(f"Hi {student}")

# call the function
students = ["Jon", "Kim", "Lee"]
print_greetings(students)