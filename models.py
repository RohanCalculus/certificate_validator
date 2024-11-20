from pydantic import BaseModel 
from typing import Optional 

# Pydantic model for validating and serializing the response for the training certificate endpoint
class TrainingResponse(BaseModel):
    """
    Pydantic model for defining the structure of the response for training certificate information.
    
    Attributes:
        name (str): The name of the student.
        email (str): The student's email address.
        program_name (str): The name of the training program.
        start_date (str): The date the training started.
        duration (str): The duration of the training program.
        certificate_link (Optional[str]): A link to the certificate (if issued), else a default message.
    """
    name: str
    email: str
    program_name: str
    start_date: str
    duration: str
    certificate_link: Optional[str]

# Pydantic model for validating and serializing the response for the internship certificate endpoint
class InternshipResponse(BaseModel):
    """
    Pydantic model for defining the structure of the response for internship certificate information.
    
    Attributes:
        name (str): The name of the intern.
        email (str): The intern's email address.
        project_name (str): The name of the project the intern worked on.
        mentor_name (str): The name of the intern's mentor.
        mentor_email (str): The mentor's email address.
        start_date (str): The start date of the internship.
        end_date (str): The end/submission date of the internship.
        certificate_link (Optional[str]): A link to the certificate (if available), else a default message.
    """
    name: str
    email: str
    project_name: str
    mentor_name: str
    mentor_email: str
    start_date: str
    end_date: str
    certificate_link: Optional[str]