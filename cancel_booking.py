import file_operations

def cancel_booking(bookings):
    try:
        booking_id = int(input("Enter booking ID to cancel: "))
        for booking in bookings:
            if booking["id"] == booking_id:
                bookings.remove(booking)
                file_operations.save_to_file(bookings)
                print(f"Booking {booking_id} cancelled.")
                return
        print("Invalid booking ID.")
    except ValueError:
        print("Please enter a valid booking ID.")
