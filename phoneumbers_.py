import phonenumbers

number = "+959253899174"

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier

service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))