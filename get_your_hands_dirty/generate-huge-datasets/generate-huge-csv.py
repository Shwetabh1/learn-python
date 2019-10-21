'''
Generate huge amounts of CSV.
What will you learn?
- File Handling
- Streams
- Faker libraries
'''
from faker import Faker
fake = Faker()


# I am taking a use case of storing person's info
# The JSON Object

csvHeaders = {
    "FIRST_NAME": fake.first_name(),
    "LAST_NAME": fake.last_name(),
    "PREFIX": fake.prefix(),
    "ADDRESS_ONE": fake.building_number(),
    "ADDRESS_TWO": fake.street_address(),
    "CITY": fake.city(),
    "STATE": fake.state(),
    "ZIP_CODE": fake.zipcode(),
    "COUNTRY": fake.country(),
    "VOICE_NUMBER": fake.phone_number(),
    "EMAIL_ADDRESS": fake.email(),
    "DATE_OF_BIRTH": fake.date(pattern="%Y-%m-%d", end_datetime=None)
}

print (csvHeaders);

