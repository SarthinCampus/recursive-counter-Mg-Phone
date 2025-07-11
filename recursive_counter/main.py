def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

def run_countdown_program():
    while True:
        num_str = input("Enter a non-negative number to start countdown: ")
        if num_str.isdigit():  # Check if the input consists only of digits
            num = int(num_str)
            if num >= 0:
                countdown(num)
                break  # Exit the loop if a valid non-negative number is entered
            else:
                print("Error")
        else:
            print("Error")

run_countdown_program()
