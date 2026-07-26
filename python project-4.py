
"""Data Analyzer and Transformer Program """


def calculate_factorial(n):
    """Calculates factorial using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def get_dataset_statistics(data):
    """Returns multiple statistical values as a tuple: (min, max, sum, avg)"""
    if not data:
        return 0, 0, 0, 0.0
    min_val = min(data)
    max_val = max(data)
    total_sum = sum(data)
    avg_val = total_sum / len(data)
    return min_val, max_val, total_sum, avg_val

def main():
    data = []
    
    while True:
        print("\nWelcome to the Data Analyzer and Transformer Program")
        print("=" * 52)
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        
        choice = input("Please enter your choice: ").strip()
        
        # Option 1: Input Data
        if choice == '1':
            print("\nStep 1: Input Data")
            raw_input = input("Enter data for a 1D array (separated by spaces): ")
            try:
                data = [float(x) if '.' in x else int(x) for x in raw_input.split()]
                print("Data has been stored successfully!")
            except ValueError:
                print("Error: Invalid input! Please enter valid numbers separated by spaces.")

        # Option 2: Display Data Summary
        elif choice == '2':
            if not data:
                print("\nNo data found! Please input data first (Option 1).")
                continue
            
            print("\nStep 2: Display Data Summary (Built-in Functions)")
            print("\nData Summary:")
            print(f"- Total elements: {len(data)}")
            print(f"- Minimum value: {min(data)}")
            print(f"- Maximum value: {max(data)}")
            print(f"- Sum of all values: {sum(data)}")
            print(f"- Average value: {sum(data) / len(data):.2f}")

        # Option 3: Calculate Factorial
        elif choice == '3':
            print("\nStep 3: Calculate Factorial (Recursion)")
            try:
                num = int(input("Enter a number to calculate its factorial: "))
                fact = calculate_factorial(num)
                print(f"Factorial of {num} is: {fact}")
            except ValueError:
                print("Error: Please enter a valid integer.")

        # Option 4: Filter Data by Threshold
        elif choice == '4':
            if not data:
                print("\nNo data found! Please input data first (Option 1).")
                continue
                
            print("\nStep 4: Filter Data by Threshold (Lambda Function)")
            try:
                threshold = float(input("Enter a threshold value to filter out data above this value: "))
                filtered_data = list(filter(lambda x: x >= threshold, data))
                
                # Format print output as comma separated numbers
                formatted_str = ", ".join(str(x) for x in filtered_data)
                print(f"\nFiltered Data (values >= {threshold}):")
                print(formatted_str if formatted_str else "No elements match the threshold criteria.")
            except ValueError:
                print("Error: Please enter a valid number for threshold.")

        # Option 5: Sort Data
        elif choice == '5':
            if not data:
                print("\nNo data found! Please input data first (Option 1).")
                continue
                
            print("\nStep 5: Sort Data")
            print("Choose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            sort_choice = input("Enter your choice: ").strip()
            
            if sort_choice == '1':
                sorted_data = sorted(data)
                formatted_str = ", ".join(str(x) for x in sorted_data)
                print(f"\nSorted Data in Ascending Order:\n{formatted_str}")
            elif sort_choice == '2':
                sorted_data = sorted(data, reverse=True)
                formatted_str = ", ".join(str(x) for x in sorted_data)
                print(f"\nSorted Data in Descending Order:\n{formatted_str}")
            else:
                print("Invalid sorting choice!")

        # Option 6: Display Dataset Statistics
        elif choice == '6':
            if not data:
                print("\nNo data found! Please input data first (Option 1).")
                continue
                
            print("\nStep 6: Display Dataset Statistics (Return Multiple Values)")
            min_v, max_v, sum_v, avg_v = get_dataset_statistics(data)
            print("\nDataset Statistics:")
            print(f"- Minimum value: {min_v}")
            print(f"- Maximum value: {max_v}")
            print(f"- Sum of all values: {sum_v}")
            print(f"- Average value: {avg_v:.2f}")

        # Option 7: Exit
        elif choice == '7':
            print("\nStep 7: Exit Program")
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a number from 1 to 7.")

if __name__ == "__main__":
    main()