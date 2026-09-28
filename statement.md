## Project Statement

## Problem statement

Managing student grades manually can be time-consuming and can make it difficult to add, find, update , or remove student records. A simple command-line based system us needed to organize student names and their grades in an easy and efficient way.

The **Student's Grade Management System** is a Python based application that provides basic operations for managing student grade records. It stores student names and grades in a dictionary and allows user to perform different operations through and interactive menu.

## Scope of the Project 

The project focuses on developing a simple, menu-driven student grade management system that runs through the command line.

The scope includes :

- Adding a new student along with their grade.
- Searching for and displaying a student's grade.
- Updating the grade of an existing student.
- Deleting a student record.
- Displaying all currently stored students and their grades.
- Providing an option to exit the application safely.
- Handling invalid menu choices and students that do not exist in the records.

The current version stores data temporarily in memory using a python dictionary. Therefore, student records are lost when the program is terminated. Database storage, authentication, graphical interfaces, and permenant file storage are outside the scope of the current version.

## Target Users 

The primary target users are :

- **Students** - for learning and praciticing basic student-record management concepts.
- **Teachers/Faculty** - for demostrating a simple method of managing student grades.
- **Beginners in Python** - for understanding dictionaries, functions, loops, conditional statements, user input and basic CRUD operations.
- **Academic project evaluators** - for evaluating the implementation of a simple command-line Python application. 

## High-Level Features 

### 1. Add Student
Allows the user to enter a student's name and grade and add the information to the system.

### 2. Get Student
Allows the user to search for a student by name and display their stored grade.

### 3. Update Student
Allows the user to change the grade of an existing student.

### 4. Delete Student
Allows the user to remove a student's record from the system.

### 5. Display All Student
Displays all student names and their corresponding grades currently stored in the system.

### 6. Interactive Menu
Provides a simple numbered menu through which users can select the required operation.

### 7. Input validation
Displays appropriate messages when a user enters an invalid menu option or attempts to access a student who is not present in the records.

### 8. Command-line Execution
The application is designed to run directly in a terminal/command prompt without requiring a graphical user interface.

### 9. In-Memory Data Management
Uses a Python dictionary to temporarily store student names and grades while the program is running.