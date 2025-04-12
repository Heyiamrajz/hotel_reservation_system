import add_booking
import cancel_booking
import check_in
import check_out
import view_bookings
import file_operations

def main():
    bookings = file_operations.load_from_file()
    while True:
        print("\nHotel Reservation System")
        print("1. Add Booking")
        print("2. Cancel Booking")
        print("3. Check In")
        print("4. Check Out")
        print("5. View Bookings")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_booking.add_booking(bookings)
        elif choice == '2':
            cancel_booking.cancel_booking(bookings)
        elif choice == '3':
            check_in.check_in(bookings)
        elif choice == '4':
            check_out.check_out(bookings)
        elif choice == '5':
            view_bookings.view_bookings(bookings)
        elif choice == '6':
            file_operations.save_to_file(bookings)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
