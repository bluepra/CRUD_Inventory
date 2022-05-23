# Shopify Backend Intern 2022 Challenge

## Replit Steps:
1. Run pip install Flask-SQLAlchemy in the console or shell
2. (ONLY IF .db FILE IS MISSING) Run create_db.py to create the database file: python ./create_db.py
3. Run app.py or hit the green "Run" button on Replit: python ./app.py
6. Please click the "Open in a new tab" button in the top right browser window (seems to work better).
   
## Git clone steps:
1. Make sure python3 is installed
2. Clone the repo: git clone https://github.com/bluepra/shopify-backend-challenge.git
3. Go to the project folder in the terminal
4. (ONLY IF .db FILE IS MISSING) Run create_db.py to create the database file: python ./create_db.py
5. Install flask and flask-sqlalchemy: pip install Flask, pip install Flask-SQLAlchemy
6. Run app.py: python ./app.py
7. Click on the link that the terminal shows which should open your browser

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



