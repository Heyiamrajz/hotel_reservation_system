# hotel_reservation_system
This is a simple Hotel Reservation System built using Python. It helps manage room bookings, check-ins, check-outs, and cancellations. The system saves booking data to a file and loads it when the program starts.

## Features
- Add Bookings: Add new bookings with guest name, room type, check-in date, and check-out date.
- Cancel Bookings: Cancel existing bookings using the booking ID.
- Check-In: Mark guests as checked in using the booking ID.
- Check-Out: Mark guests as checked out using the booking ID.
- View Bookings: View all current bookings. Displays a message if no bookings are found.

## Project Structure
- add_booking.py: Function to add new bookings.
- cancel_booking.py: Function to cancel existing bookings.
- check_in.py: Function to check in guests.
- check_out.py: Function to check out guests.
- view_bookings.py: Function to view all bookings.
- file_operations.py: Functions to save and load booking data from a file.
- hotel_reservation_system.py: Main program that ties everything together.

## Functions and Their Interrelationships
- add_booking(): Adds a new booking and saves it to the file.
- cancel_booking(): Cancels a booking and saves the updated data to the file.
- check_in(): Marks a booking as checked in and saves the updated data to the file.
- check_out(): Marks a booking as checked out and saves the updated data to the file.
- view_bookings(): Displays all bookings or a message if no bookings are found.
- save_to_file(): Saves booking data to a JSON file.
- load_from_file(): Loads booking data from a JSON file.

## External Libraries
- json: Used for saving and loading booking data in JSON format.

## How to Run the Project
1. Ensure all files are in the same directory.
2. Run the main program:
   python hotel_reservation_system.py
