import phonenumbers
from phonenumbers import geocoder, carrier

while True:
    num = input("Enter number (+countrycode) or 'exit': ")
    
    if num.lower() == "exit":
        break

    try:
        n = phonenumbers.parse(num)
        if phonenumbers.is_valid_number(n):
            print("Valid ✅")
            print("Location:", geocoder.description_for_number(n, "en"))
            print("Carrier:", carrier.name_for_number(n, "en"))
        else:
            print("Invalid ❌")
    except:
        print("Wrong format")

    print("-" * 30)
