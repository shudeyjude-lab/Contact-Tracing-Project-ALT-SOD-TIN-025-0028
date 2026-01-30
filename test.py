from contact_tracing import add_person, add_contact, get_high_risk_contacts, infection_status, contacts

# Sample data

add_person("Ade", False)
add_person("Bala", True)
add_person("Peter", False)
add_person("Jack", False)
add_person("Shina", True)
add_person("Bolatito", False)
add_person("Noah", False)
add_person("Kenny", True)
add_person("Daniel", False)
add_person("Nimi", True)

add_contact("Ade", "Bala", 70)
add_contact("Jack", "Shina", 30)
add_contact("Shina", "Jack", 30)
add_contact("Bolatito", "Daniel", 10)
add_contact("Nimi", "Jack", 20)
add_contact("Noah", "Bolatito", 32)

def print_report():
    high_risk = get_high_risk_contacts()

    print("\nExposure Report")
    print("------------")
    print(f"Total People: {len(infection_status)}")
    print(f"Total Contact Events: {len(contacts)}")
    print(f"Infected People: {sum(infection_status.values())}")
    print(f"High Risk Individuals: {len(high_risk)}")

    print("\nTop Exposures:")
    for exposed, infected, time in high_risk:
        print(f"-{exposed} exposed to {infected} for {time} minutes")

# Run report
print_report