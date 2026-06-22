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


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))