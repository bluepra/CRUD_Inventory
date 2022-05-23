# Shopify Backend Intern 2022 Challenge

## Steps to run:
1. Make sure python3 and sqlite is installed
2. Run create.py to create the database file: python ./create.py
3. Install flask and flask-sqlalchemy:  pip install Flask, pip install SQLAlchemy
4. Run app.py: python ./app.py

## How to use the inventory:
1. Click the Add/Edit Warehouse button to add a warehouse
2. Once you have a warehouse, you can create and add items to the inventory
3. Hit "Edit" to edit items or warehouses
4. Hit "Delete" to remove items or warehouses
5. Removing a warehouse causes all of its items to be removed from inventory as well


## Improvements to make:
1. Seperate inventory and warehouse code into 2 different python files
2. Use foreign key constraints in SQLAlchemy to deal with ON DELETE CASCADE 
3. Host the database non-locally
4. Make the warehouse table more comprehensive
5. Do more thorough error checking on user input


Code written by Prannav Arora



