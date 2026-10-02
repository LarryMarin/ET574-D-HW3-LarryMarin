# list of three students named Jon, Kim and Lee

# function to print ‘Hi name’ for each student in the list
# def print_greetings(students):
#     for student in students:
#         print(f"Hi {student}")
#     print(f"Total number of students: {len(students)}")

# # call the function
# students = ["Jon", "Kim", "Lee"]
# students.append("Sara")
# students.append("Miko")
# # change Jon to John
#students[1] = 'John'
#Copiloit gave me the following code to change Jon to John
# students[0] = 'John'
# print_greetings(students)

#Task E
# Create two empty lists
# students = []
# gpas = []

# # Store data for 25 students
# for i in range(25):
#     name = input(f"Enter student {i + 1}'s name: ")
#     gpa = float(input(f"Enter {name}'s GPA: "))

#     students.append(name)
#     gpas.append(gpa)

# # Display student information
# print("\nStudent Records")
# print("--------------------")

# for i in range(25):
#     print(f"Student: {students[i]}, GPA: {gpas[i]}")

#Task F-1Test an updated prompt including detailed instructions and output indicators using dashes, bullets or other separators to separate the details of the request:


# studentNames = []
# studentGPAs = []

# Read student data from the file
# with open("students.txt", "r") as file:
#     for line in file:
#         name, gpa = line.strip().split(",")
#         studentNames.append(name)
#         studentGPAs.append(float(gpa))

# # Calculate the average GPA
# averageGPA = sum(studentGPAs) / len(studentGPAs)

# print(f"Average GPA: {averageGPA:.2f}")

# # Print students above the average GPA
# print("\nStudents above average:")
# for i in range(len(studentNames)):
#     if studentGPAs[i] > averageGPA:
#         print(f"{studentNames[i]}: {studentGPAs[i]:.2f}")

# # Predict scholarship recipients
# print("\nPredicted scholarship recipients:")
# for i in range(len(studentNames)):
#     if studentGPAs[i] >= 3.5:
#         print(f"{studentNames[i]}: {studentGPAs[i]:.2f}")

#Task F-2 Test an updated prompt with context and more instructions specifying code complexity:

# Create two empty lists
# students = []
# gpas = []

# # Read student data from the file
# file = open("students.txt", "r")

# for line in file:
#     data = line.strip().split(",")

#     studentName = data[0]
#     studentGPA = float(data[1])

#     students.append(studentName)
#     gpas.append(studentGPA)

# file.close()

# # Calculate the average GPA
# totalGPA = sum(gpas)
# averageGPA = totalGPA / len(gpas)

# print("Average GPA:", round(averageGPA, 2))

# # Print students above the average GPA
# print("\nStudents above average:")

# for i in range(len(students)):
#     if gpas[i] > averageGPA:
#         print(students[i], "-", gpas[i])

# # Predict scholarship eligibility
# # Assume a GPA of 3.5 or higher qualifies
# print("\nStudents predicted to earn a scholarship:")

# for i in range(len(students)):
#     if gpas[i] >= 3.5:
#         print(students[i], "-", gpas[i])

#Task F-3 Test the updated prompt with input data to process and more information about the GPA range:

# Store student names and GPAs in two lists
# students = ["Jon", "Kim", "Lee", "Sara", "Miko",
#             "Lin", "Toby", "Ben", "Mark", "Xia"]

# gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
#         2.10, 2.89, 2.75, 2.34, 3.53]

# # Calculate the total GPA
# totalGPA = 0

# for gpa in gpas:
#     totalGPA = totalGPA + gpa

# # Calculate the average GPA
# averageGPA = totalGPA / len(gpas)

# print("Average GPA:", round(averageGPA, 2))

# # Print students who are above average
# print("\nStudents above average:")

# for i in range(len(students)):
#     if gpas[i] > averageGPA:
#         print(students[i], gpas[i])

# # Predict students who qualify for a scholarship
# print("\nPotential scholarship students:")

# for i in range(len(students)):
#     if gpas[i] >= 3.5:
#         print(students[i], gpas[i])

#Task G Few-Shot prompting:

#Task G-1:

# Store student names and GPAs in two lists
# students = ["Jon", "Kim", "Lee", "Sara", "Miko",
#             "Lin", "Toby", "Ben", "Mark", "Xia"]

# gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
#         2.10, 2.89, 2.75, 2.34, 3.53]

# # Calculate the average GPA
# totalGpa = sum(gpas)
# averageGpa = totalGpa / len(gpas)

# print("Average GPA:", round(averageGpa, 2))

# # Print students with above-average GPAs
# print("\nStudents with above-average GPAs:")

# for i in range(len(students)):
#     if gpas[i] > averageGpa:
#         print(students[i], gpas[i])

# # Known scholarship recipients and their GPAs
# scholarshipGpas = [2.75, 2.90, 3.15, 3.75]

# # Use the lowest known scholarship GPA as the cutoff
# scholarshipCutoff = min(scholarshipGpas)

# # Predict which students may earn a scholarship
# print("\nPredicted scholarship recipients:")

# for i in range(len(students)):
#     if gpas[i] >= scholarshipCutoff:
#         print(students[i], gpas[i])

#Task H Avoiding Parsing Errors


# Store student names and GPAs in two lists
# students = ["Jon", "Kim", "Lee", "Sara", "Miko",
#             "Lin", "Toby", "Ben", "Mark", "Xia"]

# gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
#         2.10, 2.89, 2.75, 2.34, 3.53]

# # Calculate the average GPA
# totalGPA = sum(gpas)
# averageGPA = totalGPA / len(gpas)

# print("Average GPA:", round(averageGPA, 2))

# # Print students who are above average
# print("\nStudents above average:")

# for i in range(len(students)):
#     if gpas[i] > averageGPA:
#         print(students[i], gpas[i])

# # Predict scholarship recipients
# print("\nPredicted scholarship recipients:")

# for i in range(len(students)):
#     if gpas[i] >= 2.75:
#         print(students[i], gpas[i])

#Task I-1

# Store student information in a dictionary
# students = {
#     "Jon": {"GPA": 3.25, "Major": "Math"},
#     "Kim": {"GPA": 2.25, "Major": "Biology"},
#     "Lee": {"GPA": 2.30, "Major": "Math"},
#     "Sara": {"GPA": 4.00, "Major": "Math"},
#     "Miko": {"GPA": 1.90, "Major": "Math"},
#     "Lin": {"GPA": 2.10, "Major": "Biology"},
#     "Toby": {"GPA": 2.89, "Major": "Biology"},
#     "Ben": {"GPA": 2.75, "Major": "Math"},
#     "Mark": {"GPA": 2.34, "Major": "Math"},
#     "Xia": {"GPA": 3.53, "Major": "Biology"}
# }

# # Calculate the total GPA
# totalGPA = 0

# for name in students:
#     totalGPA += students[name]["GPA"]

# # Calculate the average GPA
# averageGPA = totalGPA / len(students)

# print("Average GPA:", round(averageGPA, 2))

# # Print students above the average GPA
# print("\nStudents above average:")

# for name in students:
#     if students[name]["GPA"] > averageGPA:
#         print(name, students[name]["Major"],
#               students[name]["GPA"])

# # Predict scholarship eligibility
# print("\nScholarship predictions:")

# for name in students:
#     gpa = students[name]["GPA"]
#     major = students[name]["Major"]

#     if major == "Biology" or gpa >= 3.5:
#         print(name, "earned a scholarship")
#     else:
#         print(name, "did not earn a scholarship")

#Task I-2:

# students = {
#     "Jon": {"GPA": 3.25, "Major": "Math"},
#     "Kim": {"GPA": 2.25, "Major": "Biology"},
#     "Lee": {"GPA": 2.30, "Major": "Math"},
#     "Sara": {"GPA": 4.00, "Major": "Math"},
#     "Miko": {"GPA": 1.90, "Major": "Math"},
#     "Lin": {"GPA": 2.10, "Major": "Biology"},
#     "Toby": {"GPA": 2.89, "Major": "Biology"},
#     "Ben": {"GPA": 2.75, "Major": "Math"},
#     "Mark": {"GPA": 2.34, "Major": "Math"},
#     "Xia": {"GPA": 3.53, "Major": "Biology"}
# }

# # Calculate average GPA
# totalGPA = 0

# for name in students:
#     totalGPA += students[name]["GPA"]

# averageGPA = totalGPA / len(students)

# print(f"Average GPA: {averageGPA:.2f}")

# # Print above-average students
# print("\nAbove-average students:")

# for name in students:
#     if students[name]["GPA"] > averageGPA:
#         print(name, students[name]["Major"], students[name]["GPA"])

# # Determine scholarship eligibility
# print("\nScholarship results:")

# for name in students:
#     gpa = students[name]["GPA"]
#     major = students[name]["Major"]

#     if major == "Biology" or (major == "Math" and gpa >= 3.50):
#         print(name, "earned a scholarship")
#     else:
#         print(name, "did not earn a scholarship")

#Task J

import csv

# Create a dictionary to store student information
students = {}

# Read student information from the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        studentName = row["Student"]
        major = row["Major"]
        gpa = float(row["GPA"])

        # Check that GPA is between 0.0 and 4.0
        if 0.0 <= gpa <= 4.0:
            students[studentName] = {
                "major": major,
                "gpa": gpa
            }

# Calculate the total GPA
totalGPA = 0

for student in students:
    totalGPA += students[student]["gpa"]

# Calculate the average GPA
averageGPA = totalGPA / len(students)

print(f"Average GPA: {averageGPA:.2f}")

# Display students with above-average GPAs
print("\nStudents with above-average GPAs:")

for student, information in students.items():
    if information["gpa"] > averageGPA:
        print(
            f"{student} - {information['major']} - "
            f"GPA: {information['gpa']:.2f}"
        )

# Predict scholarship eligibility
print("\nScholarship predictions:")

for student, information in students.items():
    major = information["major"]
    gpa = information["gpa"]

    if major.lower() == "biology" or gpa >= 3.5:
        print(f"{student} - Earns a scholarship")
    else:
        print(f"{student} - Does not earn a scholarship")

#Task K: Using AI to translate code

# import java.io.IOException;
# import java.nio.file.Files;
# import java.nio.file.Paths;
# import java.util.HashMap;
# import java.util.List;

# public class StudentGPA {
#     public static void main(String[] args) throws IOException {

#         HashMap<String, String> majors = new HashMap<>();
#         HashMap<String, Double> gpas = new HashMap<>();

#         // Read all lines from the CSV file
#         List<String> lines = Files.readAllLines(
#             Paths.get("students.csv")
#         );

#         // Start at 1 to skip the header
#         for (int i = 1; i < lines.size(); i++) {
#             String[] data = lines.get(i).split(",");

#             String studentName = data[0];
#             String major = data[1];
#             double gpa = Double.parseDouble(data[2]);

#             if (gpa >= 0.0 && gpa <= 4.0) {
#                 majors.put(studentName, major);
#                 gpas.put(studentName, gpa);
#             }
#         }

#         // Calculate average GPA
#         double totalGPA = 0.0;

#         for (String student : gpas.keySet()) {
#             totalGPA += gpas.get(student);
#         }

#         double averageGPA = totalGPA / gpas.size();

#         System.out.printf("Average GPA: %.2f%n", averageGPA);

#         // Print above-average students
#         System.out.println("\nStudents with above-average GPAs:");

#         for (String student : gpas.keySet()) {
#             double gpa = gpas.get(student);

#             if (gpa > averageGPA) {
#                 System.out.printf(
#                     "%s - %s - GPA: %.2f%n",
#                     student, majors.get(student), gpa
#                 );
#             }
#         }

#         // Predict scholarship eligibility
#         System.out.println("\nScholarship predictions:");

#         for (String student : gpas.keySet()) {
#             String major = majors.get(student);
#             double gpa = gpas.get(student);

#             if (major.equalsIgnoreCase("Biology") || gpa >= 3.5) {
#                 System.out.println(student + " - Earns a scholarship");
#             } else {
#                 System.out.println(student + " - Does not earn a scholarship");
#             }
#         }
#     }
# }






