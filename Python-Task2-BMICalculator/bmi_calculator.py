
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# Colors
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def show_line():
    print(CYAN + "=" * 48)

def show_welcome():
    show_line()
    print(MAGENTA + Style.BRIGHT +
          "          WELCOME TO BMI HEALTH CHECK")
    show_line()
    print(YELLOW + "       Your Personal BMI Calculator")
    print(GREEN + "          Stay Healthy, Stay Happy!")
    show_line()

def show_bmi_chart():
    print(YELLOW + "\n         BMI REFERENCE CHART")
    print(WHITE + "-" * 40)
    print(CYAN + "Underweight : BMI below 18.5")
    print(GREEN + "Normal      : BMI 18.5 - 24.9")
    print(YELLOW + "Overweight  : BMI 25 - 29.9")
    print(RED + "Obese       : BMI 30 and above")
    print(WHITE + "-" * 40)

def calculate_bmi():
    try:
        print(BLUE + "\n       ENTER YOUR DETAILS")

        name = input(CYAN + "Enter your name: ").strip()

        if not name:
            print(RED + "Name cannot be empty!")
            return

        weight = float(input(CYAN + "Enter weight (kg): "))
        height = float(input(CYAN + "Enter height (meters): "))

        if weight <= 0 or height <= 0:
            print(RED + "\nError: Values must be greater than zero!")
            return

        if height > 3:
            print(RED + "\nPlease enter height in meters (example: 1.65).")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            message = "Consider a balanced diet."
            color = YELLOW

        elif bmi < 25:
            category = "Normal"
            message = "Great! Keep maintaining healthy habits."
            color = GREEN

        elif bmi < 30:
            category = "Overweight"
            message = "Focus on balanced food and activity."
            color = YELLOW

        else:
            category = "Obese"
            message = "Consider discussing your health with a professional."
            color = RED

        # Display result
        print("\n")
        show_line()
        print(MAGENTA + Style.BRIGHT + "              BMI REPORT")
        show_line()

        print(WHITE + "Name       : " + CYAN + name)
        print(WHITE + "Weight     : " + str(weight) + " kg")
        print(WHITE + "Height     : " + str(height) + " m")
        print(WHITE + "BMI        : " + GREEN + f"{bmi:.2f}")
        print(WHITE + "Category   : " + color + Style.BRIGHT + category)

        # Visual BMI bar
        bar_length = min(int(bmi), 40)
        print(WHITE + "\nBMI Visual : " +
              color + "#" * bar_length + WHITE + " " + str(bmi))

        show_line()
        print(color + Style.BRIGHT + message)
        print(WHITE + "Note: BMI is a general screening measure,")
        print(WHITE + "not a medical diagnosis.")
        show_line()

    except ValueError:
        print(RED + "\nInvalid input! Please enter numbers only.")

def main():
    show_welcome()
    show_bmi_chart()

    while True:
        calculate_bmi()

        choice = input(
            YELLOW + "\nDo you want to calculate again? (yes/no): "
        ).strip().lower()

        if choice not in ["yes", "y"]:
            print(GREEN + "\nThank you for using BMI Health Check!")
            print(MAGENTA + "Stay Healthy! Have a Nice Day!")
            show_line()
            break

if __name__ == "__main__":
    main()
