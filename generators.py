from faker import Faker

fake = Faker()

def generate_fake_email():
    return fake.email()

def generate_fake_password(length=6):
    return fake.password(length=length)

def generate_fake_name():
    return fake.first_name()