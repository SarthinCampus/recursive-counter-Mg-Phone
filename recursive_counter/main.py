def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

def run_countdown_program():
    while True:
        num_str = input("Enter a non-negative number to start countdown: ")
        if num_str.isdigit():
            countdown(int(num_str))
            break
        else:
            print("Error")

run_countdown_program()

