from datetime import datetime


class Experience:
    start_date: datetime
    end_date: datetime
    position:str
    company:str
    description: str

    def __init__(self, start_date, end_date, position, company, description) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.company = company
        self.position = position
        self.description = description

getAll= [
    Experience(
        start_date=datetime.now(),
        end_date=datetime.now(),
        position="Software Development",
        company="Forrest and Finch",
        description="Software developer for mobile applications using Flutter"
    ),
    Experience(
        start_date=datetime.now(),
        end_date=datetime.now(),
        position="Chief Technical Officer",
        company="Switch",
        description="Software and hardware development for the company"
    ),
    Experience(
        start_date=datetime.now(),
        end_date=datetime.now(),
        position="Programming Tutor",
        company="Sisakest Groups",
        description="Taught 23 students programming"
    ),
]