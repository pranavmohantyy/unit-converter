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


def convert_length(value, from_unit, to_unit):
    if from_unit == 'meters':
        if to_unit == 'feet':
            return meters_to_feet(value)
        elif to_unit == 'inches':
            return meters_to_inches(value)
        elif to_unit == 'cm':
            return meters_to_cm(value)
        elif to_unit == 'km':
            return meters_to_km(value)
        elif to_unit == 'miles':
            return meters_to_miles(value)
    elif from_unit == 'feet':
        return feet_to_meters(value) if to_unit == 'meters' else None
    elif from_unit == 'inches':
        return inches_to_meters(value) if to_unit == 'meters' else None
    elif from_unit == 'cm':
        return cm_to_meters(value) if to_unit == 'meters' else None
    elif from_unit == 'km':
        return km_to_meters(value) if to_unit == 'meters' else None
    elif from_unit == 'miles':
        return miles_to_meters(value) if to_unit == 'meters' else None


def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: python converter.py <category> <value> <from_unit> <to_unit>")
        return
    category = sys.argv[1]
    value = float(sys.argv[2])
    from_unit = sys.argv[3]
    if category == 'length':
        to_unit = input('Enter the unit to convert to: ')
        result = convert_length(value, from_unit, to_unit)
        if result is not None:
            print(f'{value} {from_unit} = {result} {to_unit}')
        else:
            print('Conversion not possible')


if __name__ == '__main__':
    main()