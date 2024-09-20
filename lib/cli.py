import logging
from helpers import (
    create_region,
    update_region,
    delete_region,
    create_personnel,
    delete_personnel,
    find_personnel_by_name,
    list_personnel_by_county,
    list_personnel_by_constituency,
    update_personnel_contacts,
    find_personnel_by_profession  # Import the new function
)

# Suppress SQLAlchemy log messages
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

def main():
    while True:
        print("\nPlease select an option:")
        print("0. Exit the program")
        print("1: Create region")
        print("2: Update region")
        print("3: Delete region")
        print("4. Find personnel by name")
        print("5: Create personnel")
        print("6: Update personnel contacts")
        print("7: Delete personnel")
        print("8: List all personnel in a county")
        print("9: List all personnel in a constituency")
        print("10: Search personnel by profession")  # New option for profession search

        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            constituency = input("Enter the region's constituency: ")
            county = input("Enter the region's county: ")
            create_region(constituency, county)
            input("Press Enter to return to the menu...")
        elif choice == "2":
            region_id = input("Enter the region's id: ")
            constituency = input("Enter the new constituency: ")
            county = input("Enter the new county: ")
            update_region(region_id, constituency, county)
            input("Press Enter to return to the menu...")
        elif choice == "3":
            region_id = input("Enter the region's id: ")
            delete_region(region_id)
            input("Press Enter to return to the menu...")
        elif choice == "4":
            name = input("Enter the personnel's name: ")
            find_personnel_by_name(name)
            input("Press Enter to return to the menu...")
        elif choice == "5":
            name = input("Enter the personnel's name: ")
            profession = input("Enter the personnel's profession: ")
            contacts = input("Enter the personnel's contacts: ")
            email = input("Enter the personnel's email: ")
            region_id = input("Enter the region id for the personnel: ")
            create_personnel(name, profession, contacts, email, region_id)
            input("Press Enter to return to the menu...")
        elif choice == "6":
            personnel_id = input("Enter the personnel's id: ")
            new_contacts = input("Enter the new contacts: ")
            update_personnel_contacts(personnel_id, new_contacts)
            input("Press Enter to return to the menu...")
        elif choice == "7":
            personnel_id = input("Enter the personnel's id: ")
            delete_personnel(personnel_id)
            input("Press Enter to return to the menu...")
        elif choice == "8":
            county = input("Enter the county: ")
            list_personnel_by_county(county)
            input("Press Enter to return to the menu...")
        elif choice == "9":
            constituency = input("Enter the constituency: ")
            list_personnel_by_constituency(constituency)
            input("Press Enter to return to the menu...")
        elif choice == "10":  # New search by profession option
            profession = input("Enter the profession: ")
            find_personnel_by_profession(profession)
            input("Press Enter to return to the menu...")
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
