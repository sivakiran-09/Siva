def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    while True:
        print("\nTemperature Converter")
        print("="*30)
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Celsius to Kelvin")
        print("3. Convert Fahrenheit to Celsius")
        print("4. Convert Fahrenheit to Kelvin")
        print("5. Convert Kelvin to Celsius")
        print("6. Convert Kelvin to Fahrenheit")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Thank you for using the converter. Goodbye!")
            break
        elif choice == '1':
            try:
                temp = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(temp)
                print(f"\n{temp}°C = {result:.2f}°F\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        elif choice == '2':
            try:
                temp = float(input("Enter temperature in Celsius: "))
                result = celsius_to_kelvin(temp)
                print(f"\n{temp}°C = {result:.2f}K\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        elif choice == '3':
            try:
                temp = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_celsius(temp)
                print(f"\n{temp}°F = {result:.2f}°C\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        elif choice == '4':
            try:
                temp = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_kelvin(temp)
                print(f"\n{temp}°F = {result:.2f}K\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        elif choice == '5':
            try:
                temp = float(input("Enter temperature in Kelvin: "))
                result = kelvin_to_celsius(temp)
                print(f"\n{temp}K = {result:.2f}°C\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        elif choice == '6':
            try:
                temp = float(input("Enter temperature in Kelvin: "))
                result = kelvin_to_fahrenheit(temp)
                print(f"\n{temp}K = {result:.2f}°F\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        else:
            print("Invalid choice! Please enter a valid option (1-7).")

if __name__ == "__main__":
    main()