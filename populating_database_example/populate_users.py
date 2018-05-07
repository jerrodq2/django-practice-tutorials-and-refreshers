import os
# Configure settings for project
# Need to run this before calling models from application!
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

        user = User.objects.create(first_name = first_name, last_name = last_name, email = email)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_users(10)
    print('Finished creating users')
