#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.region import Region
from models.personnel import Personnel

def seed_database():
    # Drop the old tables if they exist
    Personnel.drop_table()
    Region.drop_table()

    # Create new tables
    Region.create_table()
    Personnel.create_table()

    # Seed data for regions (Constituencies and Counties)
    region1 = Region.create("Molo", "Nakuru")
    region2 = Region.create("Nairobi West", "Nairobi")

    # Seed data for personnel (Name, Profession, Contacts, Email)
    Personnel.create("Remmy Bett", "Plumber", "0700123456", "remmybett@gmail.com", region1.id)
    Personnel.create("Jane Smith", "Engineer", "0700987654", "janesmith@gmail.com", region2.id)

    print("Database has been updated and seeded.")

seed_database()
