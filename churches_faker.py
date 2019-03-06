import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','faithfulcity.settings')

import django
# Import settings
django.setup()

import random
from churches.models import model_church
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.company()
        fake_location = fakegen.address()
        fake_denomination = random.choice(['Evangelical','Anglican','Baptist','Catholic','Non-denominational','Luthern'])
        fake_services = random.choice([1,1,1,2,2,2,2,2,3,4,5])
        fake_serviceTimes = [random.choice(['8:30am','9:00am','9:30am']),random.choice(['10:00am','10:30am','11:00am']),random.choice(['11:30am','12:00am','12:30am']),random.choice(['3:30pm','4:00pm','4:30pm']),random.choice(['5:00pm','5:30pm','6:00pm'])][:fake_services]
        fake_phoneNumber = fakegen.phone_number()
        fake_website = fakegen.url()
        fake_podcast = fake_website+"podcast"
        fake_pastor = fakegen.name()
        fake_noCampuses = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,4,5])
        fake_size = random.randint(100,1000)*fake_noCampuses**2
        fake_ageRange13_24 = random.randint(1,45)
        fake_ageRange25_35 = random.randint(1,90-fake_ageRange13_24)
        fake_ageRange35_55 = random.randint(1,90-(fake_ageRange13_24+fake_ageRange25_35))
        fake_ageRange55 = 100-(fake_ageRange13_24+fake_ageRange25_35+fake_ageRange35_55)
        fake_perFamily = random.randint(1,80)
        fake_startDate = fakegen.date_between(start_date="-50y", end_date="today")
        fake_sundaySchool = ('Yes','No')[random.randint(0,1)]
        fake_smallGroups = ('Yes','No')[random.randint(0,1)]
        fake_preachingStyle = ('Topical','Verse-by-verse','Narrative','Other','Mix')[random.randint(0,4)]
        print (fake_preachingStyle)
        # Create new User Entry
        church = model_church.objects.get_or_create(name=fake_name,
                                        location=fake_location,
                                        denomination=fake_denomination,
                                        services=fake_services,
                                        serviceTimes=fake_serviceTimes,
                                        phoneNumber=fake_phoneNumber,
                                        website=fake_website,
                                        podcast=fake_podcast,
                                        pastor=fake_pastor,
                                        noCampuses=fake_noCampuses,
                                        size=fake_size,
                                        ageRange13_24=fake_ageRange13_24,
                                        ageRange25_35=fake_ageRange25_35,
                                        ageRange35_55=fake_ageRange35_55,
                                        ageRange55=fake_ageRange55,
                                        perFamily=fake_perFamily,
                                        startDate=fake_startDate,
                                        sundaySchool=fake_sundaySchool,
                                        smallGroups=fake_smallGroups,
                                        preachingStyle=fake_preachingStyle)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(50)
    print('Populating Complete')
