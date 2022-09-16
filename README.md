# pds_assignment2
Assignment 2 for the class CS60013 : Programming and Data Structures is due on **XY, October 2022** at **23:59**. The assignment is worth 10% of the total marks for the course. Assignment submission is done via GitHub.

---
### Assignment 2 : Topics
        1. Recursion
        2. Sequences [Lists, Tuples, Strings, Dictionaries, Sets]
        3. Iteration and Comprehensions
        4. Classes and Objects
        5. Complexity Analysis

---

## Task Allocation

| Student Identifier                            | Tasks Allotted                |
|:---------------------------------------------:|:-----------------------------:|
| KAVINPURI@KGPIAN.IITKGP.AC.IN                 | Task 2, Task 5 |
| SOUMITAGURIAPHD22@KGPIAN.IITKGP.AC.IN         | Task 2, Task 5 |
| NAJAFARA.FATHIMA@KGPIAN.IITKGP.AC.IN          | Task 2, Task 5, Task 7 |
| POOJA.JAIN@KGPIAN.IITKGP.AC.IN                | Task 2, Task 5, Task 7 |
| MAMTA.RANI@KGPIAN.IITKGP.AC.IN                | Task 2, Task 5 |
| BHANUMEENA27@KGPIAN.IITKGP.AC.IN              | Task 3, Task 6 |
| DR.RAMKUMARKRISHNADHAS@KGPIAN.IITKGP.AC.IN    | Task 3, Task 6, Task 7 |
| DRREFLEXPATEL94@KGPIAN.IITKGP.AC.IN           | Task 3, Task 6 |
| KAMLESHTONY10@KGPIAN.IITKGP.AC.IN             | Task 3, Task 6, Task 7 |
| DRPRABHUKALYAN@KGPIAN.IITKGP.AC.IN            | Task 3, Task 6 |
| AMARMAJHI@KGPIAN.IITKGP.AC.IN                 | Task 1, Task 4 |
| samriddha.das2000@kgpian.iitkgp.ac.in         | Task 1, Task 4 |
| SAURABHCHAUDHARI97@KGPIAN.IITKGP.AC.IN        | Task 1, Task 4, Task 7 |
| SATHISHBT@KGPIAN.IITKGP.AC.IN                 | Task 1, Task 4 |



---                     
## Tasks

### Task 1 : Recursive file text search
        1. The task is to recursively search for all emails in a given directory tree.
        2. The emails should be returned as a list of strings in alphabetically sorted order.
        3. Complete the function `get_emails_recursive` in `recursive_text_search.py` file.

        Directory tree : data/emails
        Output : Return a list of emails in alphabetically sorted order


### Task 2 : Recursive math expression evaluation
        1. The task is to recursively evaluate a math expression given as a string.
        2. Complete the function `evaluate_math_expression` in `recursive_math_expression.py` file.
        3. Math expression will only contain +, -, *, /, ^, (, ) and integers.
        4. All the math operations are to be performed as per the order of precedence (PEMDAS) or (BODMAS).

        Example 1 :
            Input : "2+3*4"
            Output : 
            Reasoning : 2+3*4 => 2+12 => 14

        Example 2 :
            Input : "2+3*4^2"
            Output : 50
            Reasoning : 2+3*4^2 => 2+3*16 => 2+48 => 50


### Task 4 : Object Oriented Programming for Hospital Management System(HMS)
        1. The task is to implement a the classes `Hospital`, `Patient` and `Doctor` in `hpd_classes.py` file.
        2. The Hospital class should have the following attributes and methods:
                a. `name` : Name of the hospital
                b. `doctors` : List of doctor objects in the hospital
                c. `patients` : List of patient objects in the hospital
                d. `add_doctor` : Add a doctor to the hospital
                e. `add_patient` : Add a patient to the hospital
                f. `get_doctor` : Get a doctor from the hospital
                g. `get_patient` : Get a patient from the hospital
                h. `get_doctors` : Get all the doctors from the hospital
                i. `get_patients` : Get all the patients from the hospital
                j. `get_doctors_count` : Get the number of doctors in the hospital
                k. `get_patients_count` : Get the number of patients in the hospital
        3. The Patient class should have the following attributes and methods:
                a. `id` : Auto generated ID 
                b. `name` : Name of the patient
                c. `age` : Age of the patient
                d. `gender` : Sex of the patient
        4. The Doctor class should have the following attributes and methods:
                a. `id` : Auto generated ID
                b. `name` : Name of the doctor
                c. `specialization` : Specialization of the doctor
                d. `patients` : List of patients assigned to the doctor
                e. `add_patient` : Add a patient to the doctor
                f. `get_patient` : Get a patient from the doctor
                g. `get_patients` : Get all the patients from the doctor
                h. `get_patients_count` : Get the number of patients assigned to the doctor
        5. The `id` attribute of the Patient and Doctor class should be auto generated.


### Task 5 : Object Oriented Programming for Agriculture Management System(AMS)
        1. The task is to implement a the classes `Farm`, `Crop`, `Farmer` and `CropType` in `ams_classes.py` file.
        2. The Farm class should have the following attributes and methods:
                a. `name` : Name of the farm
                b. `crops` : List of crop objects in the farm
                c. `farmers` : List of farmer objects in the farm
                d. `add_crop` : Add a crop to the farm
                e. `add_farmer` : Add a farmer to the farm
                f. `get_crop` : Get a crop from the farm
                g. `get_farmer` : Get a farmer from the farm
                h. `get_crops` : Get all the crops from the farm
                i. `get_farmers` : Get all the farmers from the farm
                j. `get_crops_count` : Get the number of crops in the farm
                k. `get_farmers_count` : Get the number of farmers in the farm
        3. The Crop class should have the following attributes and methods:
                a. `id` : Auto generated ID 
                b. `name` : Name of the crop
                c. `type` : Type of the crop
                d. `farmers` : List of farmers assigned to the crop
                e. `add_farmer` : Add a farmer to the crop
                f. `get_farmer` : Get a farmer from the crop
                g. `get_farmers` : Get all the farmers from the crop
                h. `get_farmers_count` : Get the number of farmers assigned to the crop
        4. The Farmer class should have the following attributes and methods:
                a. `id` : Auto generated ID
                b. `name` : Name of the farmer
                c. `age` : Age of the farmer

### Task 6 : Object Oriented Programming for Class Management System(CMS)
        1. The task is to implement a the classes `Class`, `Student` and `Teacher` in `cms_classes.py` file.
        2. The Class class should have the following attributes and methods:
                a. `name` : Name of the class
                b. `students` : List of student objects in the class
                c. `teachers` : List of teacher objects in the class
                d. `add_student` : Add a student to the class
                e. `add_teacher` : Add a teacher to the class
                f. `get_student` : Get a student from the class
                g. `get_teacher` : Get a teacher from the class
                h. `get_students` : Get all the students from the class
                i. `get_teachers` : Get all the teachers from the class
                j. `get_students_count` : Get the number of students in the class
                k. `get_teachers_count` : Get the number of teachers in the class
        3. The Student class should have the following attributes and methods:
                a. `id` : Auto generated ID 
                b. `name` : Name of the student
                c. `age` : Age of the student
        4. The Teacher class should have the following attributes and methods:
                a. `id` : Auto generated ID
                b. `name` : Name of the teacher
                c. `age` : Age of the teacher
                d. `students` : List of students assigned to the teacher
                e. `add_student` : Add a student to the teacher
                f. `get_student` : Get a student from the teacher
                g. `get_students` : Get all the students from the teacher
                h. `get_students_count` : Get the number of students assigned to the teacher


### Task 7 : Collections and Sequences in Python : Application to Medical Transcriptions
1. The task is to implement the set of functions in `medical_transcription.py` file.
2. These functions are to be used to process the medical transcriptions in `data/mtsamples.csv` file.
3. This task is heavily oriented towards the use of collections and sequences in Python. Use the most appropriate collections and sequences as possible.
4. For working with the CSV file, you can use the `csv` module in Python or the `pandas` module. `pandas` doesn't come pre-installed with Python. 
5. You can install it using `pip install pandas` command.
6. More clear instructions are given in the `medical_transcription.py` file.
