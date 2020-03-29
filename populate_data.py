import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewProject.settings')


django.setup()

from faker import Faker

from NewApp.models import NewUser,ActivityPeriod

fake = Faker()

def populate(N=25):
    
    for data in range(1,N):
        f_real_name = fake.name()
        f_tz = fake.timezone()
        user = NewUser.objects.get_or_create(real_name=f_real_name, tz=f_tz)



if __name__ == "__main__":
    print("Populating Data.. Please Wait.....")
    populate(25)

    print("Polulating Complete")