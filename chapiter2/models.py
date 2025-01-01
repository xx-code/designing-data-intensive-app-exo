from dataclasses import dataclass
import datetime

class User:
    def __init__(self, lastname: str, firstname: str, sex: str, size: int):
        self.lastname = lastname
        self.fistname = firstname
        self.set_sex(sex)
        self.size(size)

    def set_sex(self, sex: str):
        if len(sex) > 1 or len(sex) == 0:
            raise "No sex value"

        if sex.lower() != "w" or sex.lower() != "m":
            raise "Sex must be w or m"
    
        self.sex = sex

    def set_size(self, size: int):
        if type(size) != int:
            raise "Size must be an interger"
        
        if size <= 0:
            raise "Size must be greater than zero"
        
        self.size = size

@dataclass
class UserEducation:
    school_name: str 
    start_at: datetime.date
    end_at: datetime.date

@dataclass 
class UserWork:
    job_title: str
    organizations: str

@dataclass
class UserLocation:
    type_loc: str
    name: str

@dataclass
class UserPatners:
    type_patner: str
    user: User 

@dataclass
class UserFamilly:
    type_link: str
    user: User

class UserWithDetail(User):    
    patern: UserPatners
    familly: list[UserFamilly]
    live_in: UserLocation
    born_in: UserLocation

    def __init__(self, lastname, firstname, sex, size):
        super().__init__(lastname, firstname, sex, size)


class UserProfile:
    def __init__(self, user: User, jobs: list[UserWork], educations: list[UserEducation]):
        self.user = user
        self.jobs = jobs
        self.organizations = educations
