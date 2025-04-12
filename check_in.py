import file_operations

def check_in(bookings):
    try:
        booking_id = int(input("Enter booking ID to check in: "))
        for booking in bookings:
            if booking["id"] == booking_id and booking["status"] == "booked":
                booking["status"] = "checked in"
                file_operations.save_to_file(bookings)
                print(f"Booking {booking_id} checked in.")
                return
        print("Invalid booking ID or already checked in.")
    except ValueError:
        print("Please enter a valid booking ID.")
