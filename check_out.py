import file_operations

def check_out(bookings):
    try:
        booking_id = int(input("Enter booking ID to check out: "))
        for booking in bookings:
            if booking["id"] == booking_id and booking["status"] == "checked in":
                booking["status"] = "checked out"
                file_operations.save_to_file(bookings)
                print(f"Booking {booking_id} checked out.")
                return
        print("Invalid booking ID or not checked in.")
    except ValueError:
        print("Please enter a valid booking ID.")
