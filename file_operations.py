import json

def save_to_file(bookings):
    with open('bookings.json', 'w') as file:
        json.dump(bookings, file)

def load_from_file():
    try:
        with open('bookings.json', 'r') as file:
            bookings = json.load(file)
    except FileNotFoundError:
        bookings = []
    return bookings
