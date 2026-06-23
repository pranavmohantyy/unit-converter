def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084


def meters_to_inches(meters):
    return meters * 39.3701

def inches_to_meters(inches):
    return inches / 39.3701


def meters_to_cm(meters):
    return meters * 100

def cm_to_meters(cm):
    return cm / 100


def meters_to_km(meters):
    return meters / 1000

def km_to_meters(km):
    return km * 1000


def meters_to_miles(meters):
    return meters / 1609.34

def miles_to_meters(miles):
    return miles * 1609.34


def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462


def convert_units():
    while True:
        print("Choose conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            length_choice = input("Convert (1) meters to feet, (2) feet to meters: ")
            if length_choice == '1':
                meters = float(input("Enter meters: "))
                print(f"{meters} meters = {meters_to_feet(meters)} feet")
            elif length_choice == '2':
                feet = float(input("Enter feet: "))
                print(f"{feet} feet = {feet_to_meters(feet)} meters")
        elif choice == '2':
            weight_choice = input("Convert (1) kg to lbs, (2) lbs to kg: ")
            if weight_choice == '1':
                kg = float(input("Enter kg: "))
                print(f"{kg} kg = {kg_to_lbs(kg)} lbs")
            elif weight_choice == '2':
                lbs = float(input("Enter lbs: "))
                print(f"{lbs} lbs = {lbs_to_kg(lbs)} kg")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    convert_units()