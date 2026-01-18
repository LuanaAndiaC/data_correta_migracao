from datetime import datetime, timedelta

def calculate_migration_date():
    input_date = input("Enter the date of the complaint request (DD/MM/YYYY): ")

    try:
        # Convert the entered date
        complaint_date = datetime.strptime(input_date, "%d/%m/%Y")

        # Add 180 days
        date_plus_180 = complaint_date + timedelta(days=180)

        # If it's already the 1st, keep it
        if date_plus_180.day == 1:
            migration_date = date_plus_180
        else:
            # Move to the first day of the next month
            if date_plus_180.month == 12:
                migration_date = datetime(date_plus_180.year + 1, 1, 1)
            else:
                migration_date = datetime(date_plus_180.year, date_plus_180.month + 1, 1)

        print("\n📅 Result:")
        print(f"Date of complaint request: {complaint_date.strftime('%d/%m/%Y')}")
        print(f"Migration date: {migration_date.strftime('%d/%m/%Y')}")

    except ValueError:
        print("❌ Invalid date. Use the format DD/MM/YYYY.")


calculate_migration_date()