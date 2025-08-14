#this program is a NCEA Assesment Tracker which will allow you to set Deadlines for your internal/external, set credits, set due dates and completion status
# Initialize storage
# This will hold all assessments entered by the user.
# Each assessment will be stored as a dictionary.
assessment_list = []
# Function to add a new assessment
def add_assessment():
    # Get name of the internal assessment
    name = input("Enter the name of the internal assessment: ")

    # Get credit value, with input validation for integers
    try:
        # Get credit value, with input validation for integers
        credits = int(input("Enter the number of credits: "))
    except ValueError:
        print("Please enter a valid number for credits.")
        return  # Stop function if invalid number
    

    # Get due date (no strict validation yet, free text)
    due_date = input("Enter the due date (e.g., 20 Aug 2025): ")
    # Get completion status (yes/no)
    status = input("Is the assessment completed? (yes/no): ").lower()
    # Add to list as dictionary
    assessment = {
        "name": name,
        "credits": credits,
        "due_date": due_date,
        "status": status
    }
    # Add dictionary to the assessment list
    assessment_list.append(assessment)
    print("Assessment added successfully.\n")

# Function to display all assessments
def display_assessments():
    #Shows all assessments currently stored in a clear list format.
    if not assessment_list:
        print("No assessments recorded yet.\n")
        return # Exit if no assessments
    print("\nCurrent Assessments:")
    # Loop through the list and display each assessment
    for i, a in enumerate(assessment_list, 1):
        print(f"{i}. {a['name']} | {a['credits']} credits | Due: {a['due_date']} | Status: {a['status']}")
    print()
# Function to calculate total and completed credits
def calculate_credits():
    #Calculates total and completed credits and displays them.
    total_credits = 0
    completed_credits = 0
    # Loop through each assessment to sum up credits
    for a in assessment_list:
        total_credits += a["credits"]
        if a["status"] == "yes":
            completed_credits += a["credits"]
        else:
            print('no completed credits')
    # Display results
    print(f"\nTotal credits: {total_credits}")
    print(f"Completed credits: {completed_credits}\n")
# Function to save to a text file
def save_to_file():
    with open("assessments.txt", "w") as file:
        for a in assessment_list:
            line = f"{a['name']},{a['credits']},{a['due_date']},{a['status']}\n"
            file.write(line)
    print("Data saved to assessments.txt. Goodbye!")
# Main menu loop
def main_menu():
    while True:
        print("1. Add Assessment")
        print("2. View Assessments")
        print("3. View Total Credits")
        print("4. Save and Exit")
        choice = input("Choose an option (1-4): ")
         # Match input to function calls
        if choice == "1":
            add_assessment()
        elif choice == "2":
            display_assessments()
        elif choice == "3":
            calculate_credits()
        elif choice == "4":
            save_to_file()
            break# Exit loop after saving
        else:
            print("Invalid input. Please try again.\n")
# Start the program
main_menu()

