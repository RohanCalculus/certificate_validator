# Imports
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient  
from bson.objectid import ObjectId  
from dotenv import load_dotenv
from models import TrainingResponse, InternshipResponse
import os

# Create an instance of the FastAPI class
app = FastAPI()

# Load environment variables from the .env file
load_dotenv()

# Get MongoDB connection string from environment variables
connection_string = os.getenv('MONGODB_CONNECTION_STRING')

# Create a client to connect to MongoDB using the connection string
client = MongoClient(connection_string)

# Connect to the specific MongoDB database 
db = client['database']

# Root endpoint to check if the application is running
@app.get('/')
def index_root():
    """
    Root endpoint to check if the FastAPI application is running.
    Returns a JSON response indicating the app status.
    """
    return {'App': 'Running'}

# Endpoint to get training certificate information by certificate ID
@app.get("/training/{certificate_id}", response_model=TrainingResponse)
async def get_training_info(certificate_id: str):
    """
    Endpoint to fetch training certificate information from the MongoDB database using the certificate ID.
    
    Args:
        certificate_id (str): The unique ID of the training certificate in the MongoDB collection.
    
    Returns:
        TrainingResponse: A response object containing the training certificate details such as
                          name, email, program name, start date, duration, and a certificate link.
    
    Raises:
        HTTPException: If the certificate ID is not found, a 404 error is returned.
    """
    # Fetch training info from MongoDB collection 'trainingCertificates' based on the provided certificate_id
    student_info = db['trainingCertificates'].find_one({'_id': ObjectId(certificate_id)})

    # If the certificate with the given ID is not found, raise an HTTPException (404 Not Found)
    if student_info is None:
        raise HTTPException(status_code=404, detail="Training ID not found")

    # Extract the necessary fields from the MongoDB document
    name = student_info['Name']
    email = student_info['Email']
    program_name = student_info['Program']
    start_date = student_info['start_date']
    duration = student_info['Duration']

    # Fetch the certificate link if it exists, otherwise return a default message
    certificate_link = student_info.get('certificate', "Training Completion Certificate is not issued yet.")

    # Return the training information as a Pydantic model (TrainingResponse)
    return TrainingResponse(
        name=name,
        email=email,
        program_name=program_name,
        start_date=start_date,
        duration=duration,
        certificate_link=certificate_link
    )


# Endpoint to get internship certificate information by certificate ID
@app.get("/internship/{certificate_id}", response_model=InternshipResponse)
async def get_internship_info(certificate_id: str):
    """
    Endpoint to fetch internship certificate information from the MongoDB database using the certificate ID.
    
    Args:
        certificate_id (str): The unique ID of the internship certificate in the MongoDB collection.
    
    Returns:
        InternshipResponse: A response object containing the internship certificate details such as
                            name, email, project name, mentor details, start date, end date, and certificate link.
    
    Raises:
        HTTPException: If the certificate ID is not found, a 404 error is returned.
    """
    # Fetch internship info from MongoDB collection 'internshipCertificates' based on the provided certificate_id
    internship_info = db['internshipCertificates'].find_one({'_id': ObjectId(certificate_id)})

    # If the certificate with the given ID is not found, raise an HTTPException (404 Not Found)
    if internship_info is None:
        raise HTTPException(status_code=404, detail="Internship ID not found")

    # Extract the necessary fields from the MongoDB document
    name = internship_info['Name']
    email = internship_info['Email Id']
    project_name = internship_info['Project Name']
    mentor_name = internship_info['Mentor Name']
    mentor_email = internship_info['Mentor Email']
    start_date = internship_info['Start Date']
    end_date = internship_info['Submission Date']

    # Fetch the certificate link if it exists, otherwise return a default message
    certificate_link = internship_info.get('certificate', "Unable to fetch the Certificate. Reach out to our team via team@spartificial.com")

    # Return the internship information as a Pydantic model (InternshipResponse)
    return InternshipResponse(
        name=name,
        email=email,
        project_name=project_name,
        mentor_name=mentor_name,
        mentor_email=mentor_email,
        start_date=start_date,
        end_date=end_date,
        certificate_link=certificate_link
    )
