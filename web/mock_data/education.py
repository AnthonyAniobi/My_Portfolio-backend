from dataclasses import dataclass
from datetime import datetime


@dataclass
class Education:
    start_date:datetime
    end_date:datetime
    course:str
    school:str
    description:str

getAll=[
        Education(
            start_date= datetime.now(),
            end_date=datetime.now(),
            course="Fundamentals of Computer Science", 
            school="University of London", 
            description="Course Specialization on Computer science and mathematics"
            ),
        Education(
            start_date=datetime.now(),
            end_date=datetime.now(),
            course="Mechanical Engineering", 
            school="University of Nigeria Nsukka", 
            description="Usage and implementation of mechanical and mechatronics systems"
            ),
        Education(
            start_date=datetime.now(),
            end_date=datetime.now(),
            course="Neural Networks and Deep Learning", 
            school="Standford University", 
            description="Certification course on the concepts and application of machine learning systems"
            ),
    ]
