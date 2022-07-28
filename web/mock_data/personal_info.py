import datetime


class PersonalInfo:
    image: str
    age:int
    complete_adress:str
    short_adress:str
    phone_line1:str
    phone_line2:str 
    github_link:str
    linkedin_link:str
    codeCanyon_link:str
    facebook_link:str
    playstore_link:str
    fiverr_link:str
    upwork_link:str
    gmail_link:str
    copyright:str

    def __init__(self):
        self.age = datetime.date.today().year - 1998
        self.copyright = datetime.date.today().year
        self.image = "https://res.cloudinary.com/aniobi/image/upload/v1632079157/my_website/person_k8nkzg.jpg"

        #adress
        self.complete_adress = "Plot 7 goldenvilla crescent, Ogui, Enugu State, Nigeria."
        self.short_adress = "Enugu State, Nigeria"

        #phone number
        self.phone_line1 = "+234 9092202826"
        self.phone_line2 = "+234 9060309095"

        #defining all the links
        self.github_link = "https://www.github.com/AnthonyAniobi"
        self.linkedin_link = "https://www.linkedin.com/in/anthony-aniobi"
        self.codeCanyon_link = "https://codecanyon.net/user/anthony_aniobi"
        self.facebook_link = "https://www.facebook.com/anthony.aniobi.50"
        self.playstore_link = "https://play.google.com/store/apps/dev?id=5804461597216736224"
        self.fiverr_link = "https://www.fiverr.com/anthony_aniobi"
        self.upwork_link = "https://www.upwork.com/freelancers/~01ecfe969ef675be42"
        self.gmail_link = "anthonyaniobi198@gmail.com"
        self.grabcad_link = ""
