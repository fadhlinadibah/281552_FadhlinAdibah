
# Initialize empty list to store loan calculations and initial debt service ratio 
loan_calculations = []
dsr_threshold = 70

# Define function to calculate monthly instalment
def calculate_monthly_instalment(principal, interest_rate, loan_term):
    # Convert interest rate to monthly rate
    monthly_interest_rate = interest_rate / 12 / 100

    # Calculate monthly payment using the equated monthly instalment formula (EMI)
    monthly_instalment = principal * monthly_interest_rate * (1 + monthly_interest_rate)**(loan_term * 12) / ((1 + monthly_interest_rate)**(loan_term * 12) - 1)

    return monthly_instalment

# Define function to calculate total payment over loan term
def calculate_total_payment(monthly_instalment, loan_term):
    total_payment = monthly_instalment * loan_term * 12

    return total_payment

# Define function to calculate Debt Service Ratio (DSR)
def calculate_debt_service_ratio(monthly_instalment, monthly_commitments, monthly_income):
    total_monthly_debt = (monthly_instalment + sum(monthly_commitments))
    debt_service_ratio = (total_monthly_debt / monthly_income)*100

    return debt_service_ratio

# Function to validate numerical input
def validate_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return value

# Function to display menu options
def display_menu():
    print("\nHousing Loan Eligibility and DSR Calculator")
    print("-" * 25)
    print("1. Calculate New Loan")
    print("2. Display Previous Calculations")
    print("3. Modify Debt Service Ratio Threshold")
    print("4. Delete Previous Calculation")
    print("5. Exit")

    selection = validate_numeric_input("Enter your selection: ")

    return selection

# Main program loop
while True:
    selection = display_menu()

    # Calculate new loan
    if selection == 1:
        # Get loan details
        principal = validate_numeric_input("Enter principal amount: RM ")
        interest_rate = validate_numeric_input("Enter annual interest rate (%): ")
        loan_term = validate_numeric_input("Enter loan term (in years): ")
        monthly_income = validate_numeric_input("Enter monthly income: RM ")
        
        # Get number of other monthly commitments (if any) and amount 
        monthly_commitments = []
        num_commitments = int(input("Number of other Monthly Commitments: "))
        for i in range(num_commitments):
            commitment = int(input(f"Enter Monthly Commitment {i + 1}: RM "))
            monthly_commitments.append(commitment)

        # Calculate monthly instalment
        monthly_instalment = calculate_monthly_instalment(principal, interest_rate, loan_term)

        # Calculate total payment
        total_payment = calculate_total_payment(monthly_instalment, loan_term)

        # Calculate debt service ratio
        debt_service_ratio = calculate_debt_service_ratio(monthly_instalment, monthly_commitments, monthly_income)

        # Check eligibility based on DSR
        if debt_service_ratio <= dsr_threshold:
            eligibility = "Eligible"
        else:
            eligibility = "Not Eligible"    

        # Store loan calculation details in a dictionary
        loan_calculation = {
            "Principal": principal,
            "Interest Rate": interest_rate,
            "Loan Term": loan_term,
            "Monthly Instalment": monthly_instalment,
            "Total Payment": total_payment,
            "Debt Service Ratio": debt_service_ratio,
            "Eligibility": eligibility
        }

        # Add calculation to list
        loan_calculations.append(loan_calculation)

        # Display calculation results
        print("\nLoan Calculation Summary:")
        print("-----------------------------")
        print(f"Principal Amount: RM {principal}")
        print(f"Interest Rate: {interest_rate}%")
        print(f"Loan Term: {loan_term} years")
        print(f"Monthly Instalment: RM {monthly_instalment:.2f}")
        print(f"Total Payment: RM {total_payment:.2f}")
        print(f"Debt Service Ratio: {debt_service_ratio:.2f}%")
        print(f"Eligibility: {eligibility}")

    elif selection == 2:
        # Display previous loan summary
        def previous_calculation ():
            print("\nPrevious Loan Calculations:")
            for index, loan in enumerate(loan_calculations, start=1):
                print(f"\nLoan {index}:")
                for key, value in loan_calculation.items():
                    print(f"{key}: {value}")
        previous_calculation()
    
    elif selection == 3:
        # Modify new Debt Service Ratio (DSR)
        def modify_new_dsr_threshold():
            new_dsr_threshold = float(input("Enter the new DSR threshold (%): "))
            dsr_threshold = new_dsr_threshold
            print(f"DSR threshold updated to {new_dsr_threshold}%.") 

        modify_new_dsr_threshold()

    elif selection == 4:
        # Delete selected loan summary 
        def delete_loan():
            if previous_calculation:
                try:
                    selection = int(input("Enter the index of the loan to delete: "))
                    if 1 <= selection <= len(loan_calculations):
                        deleted_loan = loan_calculations.pop(selection - 1)
                        print(f"Loan {selection} deleted.")
                        return deleted_loan
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
            else:
                print("No previous loans to delete.")
        deleted_loan = delete_loan()
    
    elif selection == 5:
        print("Thank you for using the program. Goodbye!")
        break
         
    else:
        print("Invalid selection. Please enter 1/2/3/4/5.")
