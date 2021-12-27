import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse(input("Enter Phonenumber:"))

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
print(timezone.time_zones_for_number(phone_number))

input("Enter to close")

