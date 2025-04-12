def view_bookings(bookings):
    for booking in bookings:
        print(f"ID: {booking['id']}, Name: {booking['name']}, Room Type: {booking['room_type']}, Status: {booking['status']}")
