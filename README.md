## Project Title: Contact Tracing & Exposure Analysis System

This is a simple contact tracing system designed to track interactions between people and identify who may be at risk of infection. I built this system during my first semester at AltSchool. 

### The system allows you to:

* Store people and their infection status
* Record contact events between people
* Calculate exposure risk based on contact duration
* Identify high-risk individuals
* Print a summary exposure report

### Concepts applied

In this project, I applied different data engineering concepts:

* Data Structures: Used lists, tuples, and dictionaries to organize data into structured formats

* Functions: Cleaned and validated incoming data

* Loops & Conditional Logic: Aggregated multiple contact events and applied business rules to identify high-risk individuals

* A close contact is defined as 15 minutes or more

* A person is considered high risk if they had close contact with an infected person and their total exposure time is at least 15 minutes

### How to run the program 
1. Clone or download the repository to your local machine
3. Open a terminal and navigate to the project folder

### Run the main script: 
```bash
python contact_tracing.py
```
To run program with sample data:
```bash
python tests.py
```# Contact-Tracing-Project-ALT-SOD-TIN-025-0028
