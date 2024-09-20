# National Construction Authority Personnel Management System

This system is designed to manage personnel information for the National Construction Authority within different regions, including creating, updating, listing, and deleting personnel records. The application stores and retrieves personnel data by regions, which are categorized by constituencies and counties in Kenya.

# Features
Create new regions and personnel.
Update existing region information or personnel contacts.
Delete regions or personnel from the system.
Find personnel by their names.
List all personnel in a specific county or constituency.


# Technologies Used
Python 
SQLite for the database
SQLAlchemy ORM for database interaction
Click for the CLI interface

# Installation Instructions

Clone the Repository

git clone https://github.com/Remmy@4873/personnel-management-system.git



# Install the required Python libraries using pip:
pip install -r requirements.txt

# Set Up the Database

Ensure the database is initialized by running the database setup script:
python lib/database.py

# Usage Instructions
Once the setup is complete, you can interact with the system through the command-line interface (CLI). Here's how you can use the various features:

# Run the Application
Run the main CLI script:

python lib/cli.py

You'll be greeted with a menu:

Please select an option:
0. Exit the program
1. Create region
2. Update region
3. Delete region
4. Find personnel by name
5. Create personnel
6. Update personnel contacts
7. Delete personnel
8. List all personnel in a county
9. List all personnel in a constituency


# Project Structure

📦Python-p3-project
 ┣ 📂lib
 ┃ ┣ 📜cli.py                # Main CLI script
 ┃ ┣ 📜helpers.py            # Helper functions for region and personnel management
 ┃ ┣ 📜database.py           # Database setup and session management
 ┃ ┣ 📜models/
 ┃ ┃ ┣ 📜region.py           # Region model
 ┃ ┃ ┗ 📜personnel.py        # Personnel model
 ┣ 📜README.md               # Project documentation
 ┣ 📜requirements.txt        # List of dependencies
 ┗ 📜management.db      
 
    
# Random Data Generation
I’ve included a set of random personnel data representing different professions within the construction field across Kenyan counties and constituencies. These can be loaded into your database for testing purposes.






