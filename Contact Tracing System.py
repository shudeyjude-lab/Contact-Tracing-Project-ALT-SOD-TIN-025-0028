  # =========================================

# Student Name: Achuka Jude

# Learner ID: ALT/SOD/TIN/025/0028

# Track: Data Engineering

# Mini Project: Contact Tracing System

# =========================================

# People and Infection Status
infection_status =  {}         

# Contact Events
contacts = []       

# First Function
def add_person(name: str, infected: bool):
    name = name.strip().title()

    if name in infection_status:
        infection_status[name] = infected
        return False
    else:
        infection_status[name] = infected
        return True

# Second Function
def add_contact(person1: str, person2: str, duration: int):
    person1 = person1.strip().title()
    person2 = person2.strip().title()

    if duration <= 0:
        return
    
    if person1 == person2:
        return
    
# Auto-add missing people
    if person1 not in infection_status:
        add_person(person1, False)

    if person2 not in infection_status:
        add_person(person2, False)

# Store contact event
    contacts.append((person1, person2, duration))

# Third Function
def get_high_risk_contacts():
    contact_by_two_persons = {}

# Exposed person, Infected person, & Total Exposure time
    for person1, person2, duration in contacts:
        contact_by_one_person = tuple(sorted([person1, person2]))  
        if contact_by_one_person in contact_by_two_persons:
            contact_by_two_persons[contact_by_one_person] += duration
        else:
            contact_by_two_persons[contact_by_one_person] = duration

    results = []

# Exposure rules
    for (person1, person2), total_exposure_time in contact_by_two_persons.items():
        if total_exposure_time >= 15:
            infected_person1 = infection_status.get(person1, False)
            infected_person2 = infection_status.get(person2, False)

            if infected_person1 and not infected_person2:
                results.append((person2, person1, total_exposure_time))      
            elif infected_person2 and not infected_person1:
                results.append((person1, person2, total_exposure_time))

    return results