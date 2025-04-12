import file_operations

def add_booking(bookings):
    name = input("Enter guest name: ")
    room_type = input("Enter room type: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
    booking_id = len(bookings) + 1
    booking = {
        "id": booking_id,
        "name": name,
        "room_type": room_type,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "status": "booked"
    }
    bookings.append(booking)
    file_operations.save_to_file(bookings)
    print(f"Booking added with ID: {booking_id}")
