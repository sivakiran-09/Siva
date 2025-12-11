def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        print("\nCelsius to Fahrenheit Converter")
        print("="*30)
        print("1. Convert Celsius to Fahrenheit")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")
        
        if choice == '2':
            print("Thank you for using the converter. Goodbye!")
            break
        elif choice == '1':
            try:
                temp = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(temp)
                print(f"\n{temp}°C = {result:.2f}°F\n")
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()