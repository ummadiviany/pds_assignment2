# PDS Assignment 2
> Assignment 2 for the class CS60013 : Programming and Data Structures is due on **20th October 2022 23:59 IST**. The assignment is worth **10%** of the total marks for the course. Assignment submission is done via GitHub.

> This assignment is crafted by [Vinay](https://ummadiviany.github.io/) and [Sai Pavan](https://saipavan-tadem.github.io/) and approved by [Prof Subhamoy Mandal](https://sites.google.com/site/smandalbiomed/home).

- [PDS Assignment 2](#pds-assignment-2)
  - [Instructions](#instructions)
    - [General Instructions](#general-instructions)
    - [Evaluation Policy](#evaluation-policy)
    - [Instructions to get started with the assignment](#instructions-to-get-started-with-the-assignment)
    - [Auto Grading Instructions](#auto-grading-instructions)
    - [Submission Instructions](#submission-instructions)
    - [Deadline](#deadline)
  - [Assignment 2 : Topics](#assignment-2--topics)
  - [Task Allocation](#task-allocation)
  - [Tasks](#tasks)
    - [Task 1 : Recursive file text search](#task-1--recursive-file-text-search)
    - [Task 2 : Recursive math expression evaluation](#task-2--recursive-math-expression-evaluation)
    - [Task 3 : Recursive pattern printing](#task-3--recursive-pattern-printing)
    - [Task 4 : Object Oriented Programming for Hospital Management System(HMS)](#task-4--object-oriented-programming-for-hospital-management-systemhms)
    - [Task 5 : Object Oriented Programming for Agriculture Management System(AMS)](#task-5--object-oriented-programming-for-agriculture-management-systemams)
    - [Task 6 : Object Oriented Programming for Class Management System(CMS)](#task-6--object-oriented-programming-for-class-management-systemcms)
    - [Task 7 : Collections and Sequences in Python : Application to Medical Transcriptions](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions)
  - [Resources](#resources)
  - [All the best!](#all-the-best)

---

## Instructions

### General Instructions
1. The assignment is to be done individually. You are `not allowed to collaborate` with other students. However, you are `allowed` to the discuss the assignment with the `course TAs`.
2. Each student is required to complete `only 3 tasks` as given in the [Task Allocation](#task-allocation) table.
3. Tasks can be completed in any order. Partial credit will be given for completed tasks. 
4. The assignment submission is handled via GitHub Classroom.
5. Late submissions will not be accepted.
6. More than **20% of code plagiarism** will lead to **100% penalty** without any further notice.

### Evaluation Policy
1. The submissions will be evaluated based on the correctness of the code.
2. A `partial` credit will be given for the `correct` code that is `not complete`.
3. The `correctness` of the code will be evaluated based on the `online test cases` associated with the assignment.
4. Any `incorrect` code will be given `zero` credit.
5. Any `late` submission will be given `zero` credit.
6. Any `plagiarized` code will be given `zero` credit.

### Instructions to get started with the assignment
1. The assignment link will be shared via email.
2. Clone the assignment repository to your local machine using the command 
   ```bash 
   git clone <assignment-repo-link>
   ```
3. Go to the assignment directory using the command 
   ```bash
   cd <assignment-repo-name>
   ```
4. Open the assignment in your VS Code using the command 
   ```bash
   code .
   ```
5. Read the instructions in the `README.md` file and start working on the assignment.

### Auto Grading Instructions
1. The auto grading and test cases are only available for the [Task 1](#task-1--recursive-file-text-search), [Task 2](#task-2--recursive-math-expression-evaluation), [Task 3](#task-3--recursive-pattern-printing) and [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions).
2. All the object oriented programming tasks are not auto graded.
3. Whoever assigned with the [Task 1](#task-1--recursive-file-text-search), [Task 2](#task-2--recursive-math-expression-evaluation), [Task 3](#task-3--recursive-pattern-printing) and [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) should follow the auto grading instructions.
4. For auto graded questions your code will be tested against the online test cases. For this to work your code should produce the expected output in the format as specified in the test cases and example outputs.

### Submission Instructions
1. Test your code using the `test cases` provided in the `tests/` directory.
2. To run the test cases, use the command with `python` or `python3` depending on your system configuration. This command should be run from the assignment root directory.
   
   ```bash
   python -m unittest tests/<test_case_file_name>.py
   ```
3. Commit your changes to the local repository using the command 
   ```bash
   git add .
   git commit -m "<commit-message>"
   ```
4. Push your changes to the remote repository using the command 
   ```bash
   git push
   ```
5. Repeat steps 3 and 4 until you are done with the assignment.
### Deadline

The deadline for the assignment is **20th October 2022, 23:59 IST**. No late submissions will be accepted.

---
## Assignment 2 : Topics
  1. `Recursion`
  2. `Sequences` [Lists, Tuples, Strings, Dictionaries, Sets]
  3. `Iteration` and `Comprehensions`
  4. `Classes` and `Objects`
  5. `Complexity Analysis`


---
## Task Allocation

| Student Identifier                            | Tasks Allotted                |
|:---------------------------------------------:|:-----------------------------:|
| KAVINPURI@KGPIAN.IITKGP.AC.IN                 | [Task 2](#task-2--recursive-math-expression-evaluation), [Task 5](#task-5--object-oriented-programming-for-agriculture-management-systemams), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions)|
| SOUMITAGURIAPHD22@KGPIAN.IITKGP.AC.IN         | [Task 2](#task-2--recursive-math-expression-evaluation), [Task 5](#task-5--object-oriented-programming-for-agriculture-management-systemams), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions)|
| NAJAFARA.FATHIMA@KGPIAN.IITKGP.AC.IN          | [Task 2](#task-2--recursive-math-expression-evaluation), [Task 4](#task-4--object-oriented-programming-for-hospital-management-systemhms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| POOJA.JAIN@KGPIAN.IITKGP.AC.IN                | [Task 2](#task-2--recursive-math-expression-evaluation), [Task 4](#task-4--object-oriented-programming-for-hospital-management-systemhms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| MAMTA.RANI@KGPIAN.IITKGP.AC.IN                | [Task 2](#task-2--recursive-math-expression-evaluation), [Task 5](#task-5--object-oriented-programming-for-agriculture-management-systemams), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions)|
| BHANUMEENA27@KGPIAN.IITKGP.AC.IN              | [Task 3](#task-3--recursive-pattern-printing), [Task 6](#task-6--object-oriented-programming-for-class-management-systemcms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| DR.RAMKUMARKRISHNADHAS@KGPIAN.IITKGP.AC.IN    | [Task 3](#task-3--recursive-pattern-printing), [Task 4](#task-4--object-oriented-programming-for-hospital-management-systemhms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| DRREFLEXPATEL94@KGPIAN.IITKGP.AC.IN           | [Task 3](#task-3--recursive-pattern-printing), [Task 6](#task-6--object-oriented-programming-for-class-management-systemcms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| KAMLESHTONY10@KGPIAN.IITKGP.AC.IN             |[Task 3](#task-3--recursive-pattern-printing) , [Task 6](#task-6--object-oriented-programming-for-class-management-systemcms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| DRPRABHUKALYAN@KGPIAN.IITKGP.AC.IN            | [Task 3](#task-3--recursive-pattern-printing), [Task 4](#task-4--object-oriented-programming-for-hospital-management-systemhms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| AMARMAJHI@KGPIAN.IITKGP.AC.IN                 | [Task 1](#task-1--recursive-file-text-search), [Task 5](#task-5--object-oriented-programming-for-agriculture-management-systemams), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| samriddha.das2000@kgpian.iitkgp.ac.in         | [Task 1](#task-1--recursive-file-text-search), [Task 5](#task-5--object-oriented-programming-for-agriculture-management-systemams), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| SAURABHCHAUDHARI97@KGPIAN.IITKGP.AC.IN        | [Task 1](#task-1--recursive-file-text-search), [Task 4](#task-4--object-oriented-programming-for-hospital-management-systemhms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |
| SATHISHBT@KGPIAN.IITKGP.AC.IN                 | [Task 1](#task-1--recursive-file-text-search), [Task 6](#task-6--object-oriented-programming-for-class-management-systemcms), [Task 7](#task-7--collections-and-sequences-in-python--application-to-medical-transcriptions) |

---                     
## Tasks

### Task 1 : Recursive file text search
1. The task is to recursively search for all emails in a given directory tree.
2. The given directory tree is a directory containing sub-directories and files.
3. The text files in the directory tree may contain emails.
4. Recursively search for all emails in the directory tree.
5. The emails should be returned as a list of strings in alphabetically sorted order.
6. Complete the function `get_emails_recursive` in `recursive_text_search.py` file.
7. The recursion can be either functional or iterative. Better to use `iterative recursion`.
8. Directory tree : `data/emails/`
9. Output : Return a `list of emails(without duplicates) in alphabetically sorted order`


### Task 2 : Recursive math expression evaluation
1. The task is to recursively evaluate a math expression given as a string.
2. Complete the function `evaluate_mathexp` in `recursive_mathexp_eval.py` file.
3. Math expression will only contain +, -, *, /, ^, (, ) and integers.
4. All the math operations are to be performed as per the order of precedence (PEMDAS) or (BODMAS).
5. Examples
   1. Example 1 : `evaluate_mathexp("2+3*4")` should return `14`
      - Input : "2+3*4"
      - Output : 14
      - Reasoning : 2+3*4 => 2+12 => 14
   2. Example 2 : `evaluate_mathexp("2+3*4^2")` should return `50`
      - Input : "2+3*4^2"
      - Output : 50
      - Reasoning : 2+3* 4^2 => 2+3*16 => 2+48 => 50 


### Task 3 : Recursive pattern printing
1. The task is to implement the function `print_pattern` in `recursive_pattern.py` file. 
2. Function takes two arguments: x and n both are integers 
3. **Note 1** : Along with the printing pattern, the function should also return `x^n`
4. Strip any leading and trailing spaces from the pattern.
5. **Examples**:

 
   1. Example 1:
      - `Input` : x = 2, n = 2
      - `Returns` : 4
      - `Prints` : 
>        y^2*-z^2*-b^2*-a^3*-b^2*-z^2*-y^2
>        x^4*-y^4*-z^4*-c^4*-b^4*-a^5*-b^4*-c^4*-z^4*-y^4*-x^4
   2. Example 2:
      - `Input` : x = 3, n = 3
      - `Returns` : 27
      - `Prints` : 

>        y^3*-z^3*-b^3*-a^4*-b^3*-z^3*-y^3
>        x^9*-y^9*-z^9*-c^9*-b^9*-a^10*-b^9*-c^9*-z^9*-y^9*-x^9
>        w^27*-x^27*-y^27*-z^27*-d^27*-c^27*-b^27*-a^28*-b^27*-c^27*-d^27*-z^27*-y^27*-x^27*-w^27
        
   3. Example 3:
      - `Input` : x = 5, n = 3
      - `Returns` : 125
      - `Prints` : 

>        y^5*-z^5*-b^5*-a^6*-b^5*-z^5*-y^5
>        x^25*-y^25*-z^25*-c^25*-b^25*-a^26*-b^25*-c^25*-z^25*-y^25*-x^25
>        w^125*-x^125*-y^125*-z^125*-d^125*-c^125*-b^125*-a^126*-b^125*-c^125*-d^125*-z^125*-y^125*-x^125*-w^125

   4. Example 4:
      - `Input` : x = 3, n = 5
      - `Returns` : 243
      - `Prints` :

>        y^3*-z^3*-b^3*-a^4*-b^3*-z^3*-y^3
>        x^9*-y^9*-z^9*-c^9*-b^9*-a^10*-b^9*-c^9*-z^9*-y^9*-x^9
>        w^27*-x^27*-y^27*-z^27*-d^27*-c^27*-b^27*-a^28*-b^27*-c^27*-d^27*-z^27*-y^27*-x^27*-w^27
>        v^81*-w^81*-x^81*-y^81*-z^81*-e^81*-d^81*-c^81*-b^81*-a^82*-b^81*-c^81*-d^81*-e^81*-z^81*-y^81*-x^81*-w^81*-v^81
>        u^243*-v^243*-w^243*-x^243*-y^243*-z^243*-f^243*-e^243*-d^243*-c^243*-b^243*-a^244*-b^243*-c^243*-d^243*-e^243*-f^243*-z^243*-y^243*-x^243*-w^243*-v^243*-u^243




### Task 4 : Object Oriented Programming for Hospital Management System(HMS)
 1. The task is to implement a the classes `Hospital`, `Patient` and `Doctor` in `hms_classes.py` file.
 2. The Hospital class should have the following attributes and methods:
      - `name` : Name of the hospital
      - `doctors` : List of doctor objects in the hospital
      - `patients` : List of patient objects in the hospital
      - `add_doctor` : Add a doctor to the hospital
      - `add_patient` : Add a patient to the hospital
      - `get_doctor` : Get a doctor from the hospital
      - `get_patient` : Get a patient from the hospital
      - `get_doctors` : Get all the doctors from the hospital
      - `get_patients` : Get all the patients from the hospital
      - `get_doctors_count` : Get the number of doctors in the hospital
      - `get_patients_count` : Get the number of patients in the hospital
 3. The Patient class should have the following attributes and methods:
      - `id` : Auto generated ID 
      - `name` : Name of the patient
      - `age` : Age of the patient
      - `gender` : Sex of the patient
 4. The Doctor class should have the following attributes and methods:
      - `id` : Auto generated ID
      - `name` : Name of the doctor
      - `specialization` : Specialization of the doctor
      - `patients` : List of patients assigned to the doctor
      - `add_patient` : Add a patient to the doctor
      - `get_patient` : Get a patient from the doctor
      - `get_patients` : Get all the patients from the doctor
      - `get_patients_count` : Get the number of patients assigned to the doctor
 5. The `id` attribute of the Patient and Doctor class should be auto generated.
 6. Implement the `__str__` method for the `Hospital`, `Patient` and `Doctor` classes.
 7. Demonstrate the use of implemented classes by creating a hospital object and adding doctors and patients to it.
 8. The demo driver code should make use of all the implemented methods of the classes.
 9. This task has no test cases. You can test your code by running the `hms_classes.py` file.
 10. This task will not be auto-graded.

### Task 5 : Object Oriented Programming for Agriculture Management System(AMS)
1. The task is to implement a the classes `Farm`, `Crop`, `Farmer` and  in `ams_classes.py` file.
2. The Farm class should have the following attributes and methods:
    - `name` : Name of the farm
    - `crops` : List of crop objects in the farm
    - `farmers` : List of farmer objects in the farm
    - `add_crop` : Add a crop to the farm
    - `add_farmer` : Add a farmer to the farm
    - `get_crop` : Get a crop from the farm
    - `get_farmer` : Get a farmer from the farm
    - `get_crops` : Get all the crops from the farm
    - `get_farmers` : Get all the farmers from the farm
    - `get_crops_count` : Get the number of crops in the farm
    - `get_farmers_count` : Get the number of farmers in the farm
3. The Crop class should have the following attributes and methods:
   - `id` : Auto generated ID 
   - `name` : Name of the crop
   - `type` : Type of the crop
   - `farmers` : List of farmers assigned to the crop
   - `add_farmer` : Add a farmer to the crop
   - `get_farmer` : Get a farmer from the crop
   - `get_farmers` : Get all the farmers from the crop
   - `get_farmers_count` : Get the number of farmers assigned to the crop
4. The Farmer class should have the following attributes and methods:
   - `id` : Auto generated ID
   - `name` : Name of the farmer
   - `age` : Age of the farmer
5. The `id` attribute of the Crop and Farmer class should be auto generated.
6. Implement the `__str__` method for the Farm, Crop and Farmer classes.
7. Demonstrate the use of implemented classes by creating a farm object and adding crops and farmers to it.
8. The demo driver code should make use of all the implemented methods of the classes.
9. This task has no test cases. You can test your code by running the `ams_classes.py` file.
10. This task will not be auto-graded.

### Task 6 : Object Oriented Programming for Class Management System(CMS)
1. The task is to implement a the classes `Class`, `Student` and `Teacher` in `cms_classes.py` file.
2. The Class class should have the following attributes and methods:
   - `name` : Name of the class
   - `students` : List of student objects in the class
   - `teachers` : List of teacher objects in the class
   - `add_student` : Add a student to the class
   - `add_teacher` : Add a teacher to the class
   - `get_student` : Get a student from the class
   - `get_teacher` : Get a teacher from the class
   - `get_students` : Get all the students from the class
   - `get_teachers` : Get all the teachers from the class
   - `get_students_count` : Get the number of students in the class
   - `get_teachers_count` : Get the number of teachers in the class
3. The Student class should have the following attributes and methods:
    - `id` : Auto generated ID 
    - `name` : Name of the student
    - `age` : Age of the student
4. The Teacher class should have the following attributes and methods:
    - `id` : Auto generated ID
    - `name` : Name of the teacher
    - `age` : Age of the teacher
    - `students` : List of students assigned to the teacher
    - `add_student` : Add a student to the teacher
    - `get_student` : Get a student from the teacher
    - `get_students` : Get all the students from the teacher
    - `get_students_count` : Get the number of students assigned to the teacher
5. The `id` attribute of the Student and Teacher class should be auto generated.
6. Implement the `__str__` method for the Class, Student and Teacher classes.
7. Demonstrate the use of implemented classes by creating a class object and adding students and teachers to it.
8. The demo driver code should make use of all the implemented methods of the classes.
9. This task has no test cases. You can test your code by running the `cms_classes.py` file.
10. This task will not be auto-graded.

### Task 7 : Collections and Sequences in Python : Application to Medical Transcriptions
1. The task is to implement the set of functions in `medical_transcription.py` file.
2. These functions are to be used to process the medical transcriptions in `data/mtsamples.csv` file.
3. This task is heavily oriented towards the use of collections and sequences in Python. Use the most appropriate collections and sequences as possible.
4. For working with the CSV file, you can use the `csv` module in Python or the `pandas` module. `pandas` doesn't come pre-installed with Python. You can install it using `pip install pandas` command.
5. In this task you will be implementing the following functions:
   1. `get_medical_specalities`
      - Implement the function `get_medical_specalities` in `medical_transcription.py` file.
      - This function should return a list of all the medical specialties from the `medical_specialty` column in the `data/mtsamples.csv` file. The list should not contain any duplicates. The list should be sorted in alphabetically ascending order.
      - Check the expected output in the `tests/transcription_outputs/get_medical_specalities.txt` file.
   2. `get_medical_specialities_count`
      - Implement the function `get_medical_specialities_count` in `medical_transcription.py` file.
      - This function should return a dictionary of all the medical specialties from the `medical_specialty` column in the `data/mtsamples.csv` file. The dictionary should have the medical specialty as the key and the number of times it occurs as the value. The dictionary should be sorted in descending order of the number of times the medical specialty occurs.
      - Check the expected output in the `tests/transcription_outputs/get_medical_specialities_count.txt` file.
   3. `get_medical_speciality_sample_names`
      - Implement the function `get_medical_speciality_sample_names` in `medical_transcription.py` file.
      - This function should return a dictionary of all the medical specialties from the `medical_specialty` column in the `data/mtsamples.csv` file. The dictionary should have the medical specialty as the key and the list of sample names as the value. The dictionary should be sorted in alphabetically ascending order of the medical specialty.
      - Check the expected output in the `tests/transcription_outputs/get_medical_speciality_sample_names.txt` file.

6. This task is auto-graded. Run the test cases and check the correctness of your code.
 

## Resources
1. [Python Documentation](https://docs.python.org/3/)
2. [Class Code Materials](https://github.com/ummadiviany/pds_snippets/)
3. [Introduction to Computation and Programming Using Python](https://mitpress.mit.edu/9780262542364/introduction-to-computation-and-programming-using-python/)
4. [Elements of Programming Interviews in Python]()
   
## All the best!