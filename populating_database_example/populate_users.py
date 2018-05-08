import os
# Configure settings for project
# Need to run this before calling models from application!
# The below line sets the environment, you put 'DJANGO_SETTINGS_MODULE' followed by your settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE','populating_database_example.settings')

import django
# Import settings
django.setup()

from users.models import User
from faker import Faker

fake = Faker()

def populate_users(num = 10):
    '''
    Create num entries of users
    '''

    print('Deleting all users....')
    User.objects.all().delete()

    for i in range(num):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()

        # You could just use create, get_or_create tries to first get the record, if it doesn't exist, it then creates it. We attach the [0] to the end to actually grab the record from the 'get' part of it
        user = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_users(10)
    print('Finished creating users')
