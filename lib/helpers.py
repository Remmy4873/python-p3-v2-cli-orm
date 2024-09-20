from database import session
from models.region import Region
from models.personnel import Personnel

def create_region(constituency, county):
    """Create a new region."""
    region = Region(constituency=constituency, county=county)
    session.add(region)
    session.commit()
    print(f"Region '{constituency}, {county}' created successfully!")

def update_region(region_id, new_constituency, new_county):
    """Update an existing region."""
    region = session.query(Region).filter_by(id=region_id).first()
    if region:
        region.constituency = new_constituency
        region.county = new_county
        session.commit()
        print(f"Region ID {region_id} updated successfully!")
    else:
        print(f"No region found with ID {region_id}.")

def delete_region(region_id):
    """Delete a region."""
    region = session.query(Region).filter_by(id=region_id).first()
    if region:
        session.delete(region)
        session.commit()
        print(f"Region ID {region_id} deleted successfully!")
    else:
        print(f"No region found with ID {region_id}.")

def find_personnel_by_name(name):
    """Find personnel by name."""
    personnel = session.query(Personnel).filter_by(name=name).first()
    if personnel:
        print(f"ID: {personnel.id}, Name: {personnel.name}, Profession: {personnel.profession}, Contacts: {personnel.contacts}, Email: {personnel.email}")
    else:
        print(f"No personnel found with the name '{name}'.")

def create_personnel(name, profession, contacts, email, region_id):
    """Create a new personnel."""
    personnel = Personnel(name=name, profession=profession, contacts=contacts, email=email, region_id=region_id)
    session.add(personnel)
    session.commit()
    print(f"Personnel '{name}' created successfully!")

def update_personnel_contacts(personnel_id, new_contacts):
    """Update personnel contacts."""
    personnel = session.query(Personnel).filter_by(id=personnel_id).first()
    if personnel:
        personnel.contacts = new_contacts
        session.commit()
        print(f"Personnel ID {personnel_id}'s contacts updated successfully!")
    else:
        print(f"No personnel found with ID {personnel_id}.")

def delete_personnel(personnel_id):
    """Delete a personnel."""
    personnel = session.query(Personnel).filter_by(id=personnel_id).first()
    if personnel:
        session.delete(personnel)
        session.commit()
        print(f"Personnel ID {personnel_id} deleted successfully!")
    else:
        print(f"No personnel found with ID {personnel_id}.")

def list_personnel_by_county(county):
    """List all personnel in a county."""
    personnel = Personnel.get_all_by_county(county)
    if personnel:
        for p in personnel:
            print(f"ID: {p.id}, Name: {p.name}, Profession: {p.profession}, Contacts: {p.contacts}, Email: {p.email}")
    else:
        print(f"No personnel found in the county '{county}'.")

def list_personnel_by_constituency(constituency):
    """List all personnel in a constituency."""
    personnel = Personnel.get_all_by_constituency(constituency)
    if personnel:
        for p in personnel:
            print(f"ID: {p.id}, Name: {p.name}, Profession: {p.profession}, Contacts: {p.contacts}, Email: {p.email}")
    else:
        print(f"No personnel found in the constituency '{constituency}'.")

def find_personnel_by_profession(profession):
    """Find personnel by profession."""
    personnel = session.query(Personnel).filter_by(profession=profession).all()
    if personnel:
        for p in personnel:
            print(f"ID: {p.id}, Name: {p.name}, Profession: {p.profession}, Contacts: {p.contacts}, Email: {p.email}")
    else:
        print(f"No personnel found with the profession '{profession}'.")
