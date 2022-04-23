1. Requirements (requirements.txt):
Open Your IDE (e.g. PyCharm), and open csv_table_analysis_app
directory as a new project.

Install requirements on your IDE

or

open cmd and activate any existing python environment.
Change directory to csv_table_analysis_app.
Create new environment in this directory using command:
"python -m venv venv"
Then activate the newly created environment:
"venv\Scripts\activate.bat"
Next paste below command to Your cmd.
"pip install -r requirements.txt"



2. Start application:

Open app.py and run it on Your IDE (e.g. PyCharm)

or

open cmd and change directory to csv_table_analysis_app.
Activate venv.
Next paste below command to Your cmd.
"python app.py"

Expected result: "Running on http://127.0.0.1:5000/"



3. Start unittest (after completing step 2):

Open test.py and run it on Your IDE (e.g. PyCharm)

or

open new cmd and change directory to csv_table_analysis_app.
Activate venv.
Next paste below command to Your cmd.
"python -m unittest test.py -v"



4. Test application (after completing step 2):

Open browser and paste path: http://127.0.0.1:5000/postcsv
The home page should open.
Now you can upload the csv file for analysis or open an existing analysis if exists.


