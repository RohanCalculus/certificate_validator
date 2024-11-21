# Certificate Validator API
This project is made to help organizations validate the certificates issued by them! Students need to give the id to validate their certificates by the organization.

## 📝 Project Details
1. Get the students data to validate from the organization (csv format)
2. Convert this csv file to JSON file using [csv_to_json.py](https://github.com/RohanCalculus/certificate_validator/blob/main/csv_to_json.py)
3. Insert the data to database (MongoDB) using [mongo_db.py](https://github.com/RohanCalculus/certificate_validator/blob/main/mongo_db.py)
4. Run the API to test it

You can use this API and integrate in your organization's frontend to allow them to validate the certificates issued by them.

## 🛠️ Tools used
1. MongoDB for Database Management
2. FastAPI for API backend

## 📽️ Video Demo
The video below explains the complete process of the certificate validator API, from data insertion to database and API response.

<a href="https://www.youtube.com/watch?v=QaXX4-QX77I" target="_blank">
  <img src="https://img.youtube.com/vi/QaXX4-QX77I/maxresdefault.jpg" alt="Certificate Validator Demo" width="600" />
</a>

## ⚙️ Project Setup
1. Clone the repository
2. Setup the virtual environment
3. Install the dependencies using [requirements.txt](https://github.com/RohanCalculus/certificate_validator/blob/main/requirements.txt)
4. Fill the [`internship.csv`](https://github.com/RohanCalculus/certificate_validator/blob/main/Internship%20Data/internship.csv) to validate internship certificates
5. Fill the [`data.csv`](https://github.com/RohanCalculus/certificate_validator/blob/main/Training%20Program%20Data/data.csv) to validate training program certificates
6. Run [`csv_to_json.py`](https://github.com/RohanCalculus/certificate_validator/blob/main/csv_to_json.py) to convert respective csv to json format
7. Insert this json file to database using [`mongo_db.py`](https://github.com/RohanCalculus/certificate_validator/blob/main/mongo_db.py)
8. Once you add the data to database, students can always validate their certificates issued by your organization
