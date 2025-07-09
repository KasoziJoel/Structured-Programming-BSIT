def calculate_fine(days_late):
    if days_late <= 0:
        return 0, False
    elif days_late <= 7:
        return days_late * 1000, False
    elif days_late < 30:
        return days_late * 2000, False
    else:
        return 50000, True

def get_valid_input():
    while True:
        try:
            days_late = int(input("Enter number of days late: "))
            if days_late < 0:
                print("Please enter a non-negative integer.")
            else:
                return days_late
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    days_late = get_valid_input()
    fine, banned = calculate_fine(days_late)
    print("\nSummary:")
    print(f"Days late: {days_late}")
    print(f"Fine: {fine} UGX")
    print(f"Banned: {'Yes' if banned else 'No'}")

if __name__ == "__main__":
    main()

