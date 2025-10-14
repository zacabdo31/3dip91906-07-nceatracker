#this program is a NCEA Assesment Tracker which will allow you to set Deadlines for your internal/external, set credits, set due dates and completion status
#setting up base base/parent class for all the assesments being stored
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Parent Class
class Assessment:
    """Base class representing a general assessment."""
    def __init__(self, name, credits, due_date, status, assessment_type):
        # Encapsulation: These are attributes stored inside each object
        self.name = name
        self.credits = credits
        self.due_date = due_date
        self.status = status
        self.assessment_type = assessment_type

    def __str__(self):
        """
        Converts the assessment object into a readable string.
        Used when displaying in GUI or saving to a text file.
        """
        return f"{self.name} | {self.credits} credits | Due: {self.due_date} | Status: {self.status} | Type: {self.assessment_type}"

# Child Classes
class InternalAssessment(Assessment):
    """Represents internal assessments (derived from the parent class)."""
    def __init__(self, name, credits, due_date, status):
        # Uses inheritance with super() to get attributes from the parent class
        super().__init__(name, credits, due_date, status, assessment_type="Internal")

class ExternalAssessment(Assessment):
    # Uses inheritance with super() to get attributes from the parent class
    def __init__(self, name, credits, due_date, status):
        super().__init__(name, credits, due_date, status, assessment_type="External")


# Manager Class
class AssessmentManager:
    """
    Handles all the backend logic - adding, removing, calculating totals,
    and saving assessment data to a text file.
    """
    def __init__(self):
        # Holds all assessments as a list of Assessment objects
        self.assessments = []

    def add_assessment(self, assessment):
        """Adds a new assessment object to the list."""
        self.assessments.append(assessment)

    def remove_assessment(self, index):
        """Removes an assessment from the list based on its index (position)."""
        if 0 <= index < len(self.assessments):
            del self.assessments[index]

    def total_credits(self):
        """Calculates total credits from all assessments."""
        return sum(a.credits for a in self.assessments)

    def completed_credits(self):
        """Calculates only credits from completed assessments."""
        return sum(a.credits for a in self.assessments if a.status.lower() == "completed")

    def save_to_file(self, filename="assessments.txt"):
        """
        Saves all assessments to a text file.
        Each line contains one assessment in readable format.
        """
        try:
            with open(filename, "w") as file:
                for assessment in self.assessments:
                    file.write(str(assessment) + "\n")
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False #indicates failure

# Gui Class
class AssessmentTrackerApp:
    """
    This class creates the graphical interface for the program.
    It connects GUI buttons and inputs with the backend functions from AssessmentManager.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("NCEA Assessment Tracker") # Window title
        self.manager = AssessmentManager() # Create instance of manager class

        # Load the main menu window when the app starts
        self.main_menu()

    # --- Utility function to clear current screen ---
    def clear_window(self):
        """Removes all widgets from the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        """Displays the main menu options."""
        self.clear_window()
        #title
        tk.Label(self.root, text="NCEA Assessment Tracker", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        # Buttons leading to other windows
        tk.Button(self.root, text="Add Assessment", command=self.add_assessment_window, width=25).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Remove Assessment", command=self.remove_assessment_window, width=25).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.root, text="View Assessments", command=self.view_assessments_window, width=25).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self.root, text="View Total Credits", command=self.show_credits_window, width=25).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Save Data", command=self.save_data, width=25).grid(row=5, column=0, padx=5, pady=5)

    # --- Add Assessment Window ---
    def add_assessment_window(self):
        self.clear_window()
        tk.Label(self.root, text="Add New Assessment", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

        #add name of assesment
        tk.Label(self.root, text="Name:").grid(row=1, column=0, sticky="w", padx=10)
        name_entry = tk.Entry(self.root)
        name_entry.grid(row=1, column=1, columnspan=2, pady=2)

        #input credits
        tk.Label(self.root, text="Credits:").grid(row=2, column=0, sticky="w", padx=10)
        credits_entry = tk.Spinbox(self.root, from_=1, to=31, width=5)
        credits_entry.grid(row=2, column=1, columnspan=2, pady=2)

        # Date Selection with Spinboxes
        tk.Label(self.root, text="Due Date D/M/Y:").grid(row=3, column=0, sticky="w", padx=10)
        day_spin = tk.Spinbox(self.root, from_=1, to=31, width=5)
        month_spin = tk.Spinbox(self.root, from_=1, to=12, width=5)
        year_spin = tk.Spinbox(self.root, from_=2025, to=2030, width=8)
        day_spin.grid(row=3, column=1, sticky="w", pady=2)
        month_spin.grid(row=3, column=1, padx=55, pady=2)
        year_spin.grid(row=3, column=2, sticky="w", pady=2)

        # Status dropdown 
        tk.Label(self.root, text="Status:").grid(row=4, column=0, sticky="w", padx=10)
        status_combo = ttk.Combobox(self.root, values=["completed", "not_completed"])
        status_combo.grid(row=4, column=1, columnspan=2, pady=2)

        # Assessment type dropdown (Internal or External)
        tk.Label(self.root, text="Type:").grid(row=5, column=0, sticky="w", padx=10)
        type_combo = ttk.Combobox(self.root, values=["Internal", "External"])
        type_combo.grid(row=5, column=1, columnspan=2, pady=2)

        def save_assessment():
            """Validates and saves new assessment data."""
            try:
                name = name_entry.get()
                credits_text = credits_entry.get()
                day = day_spin.get()
                month = month_spin.get()
                year = year_spin.get()
                status = status_combo.get()
                assessment_type = type_combo.get()

                # --- Validate all fields ---
                if not name or not credits_text or not status or not assessment_type:
                    raise ValueError("All fields must be filled!")

                # --- Validate credits input ---
                if not credits_text.isdigit():
                    raise ValueError("Credits must be a numeric value!")
                credits = int(credits_text)

                # --- Validate date ---
                due_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                datetime.strptime(due_date, "%Y-%m-%d") # Validate format + real date

                # --- Create assessment ---
                 # Create either Internal or External assessment using polymorphism
                if assessment_type == "Internal":
                    new_assessment = InternalAssessment(name, credits, due_date, status)
                else:
                    new_assessment = ExternalAssessment(name, credits, due_date, status)

                # Add assessment to manager list
                self.manager.add_assessment(new_assessment)
                messagebox.showinfo("Success", "Assessment added successfully!")
                
                # Return to main menu
                self.main_menu()

            except ValueError as e:
                # If any input is invalid
                messagebox.showerror("Error", str(e))

        # Buttons at the bottom
        tk.Button(self.root, text="Save", command=save_assessment, width=10).grid(row=6, column=0, pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=10).grid(row=6, column=1, pady=10)

    # --- Remove Assessment Window ---
    def remove_assessment_window(self):
        self.clear_window()

        tk.Label(self.root, text="Remove Assessment", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        # Display each assessment with index
        for i, a in enumerate(self.manager.assessments, 1):
            tk.Label(self.root, text=f"{i}. {a}").grid(row=i, column=0, sticky="w", padx=10)
            
        # Input for choosing which assessment to delete
        tk.Label(self.root, text="Enter number to remove:").grid(row=len(self.manager.assessments)+1, column=0, sticky="w", padx=10)
        index_entry = tk.Entry(self.root)
        index_entry.grid(row=len(self.manager.assessments)+1, column=1)

        def remove_item():
            """Deletes selected assessment by index."""
            try:
                index = int(index_entry.get()) - 1
                self.manager.remove_assessment(index)
                messagebox.showinfo("Success", "Assessment removed successfully!")
                self.main_menu()
            except Exception:
                messagebox.showerror("Error", "Invalid input.")

        tk.Button(self.root, text="Remove", command=remove_item, width=10).grid(row=len(self.manager.assessments)+2, column=0, pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=10).grid(row=len(self.manager.assessments)+2, column=1, pady=10)

    # --- View Assessments Window ---
    def view_assessments_window(self):
        self.clear_window()

        tk.Label(self.root, text="All Assessments", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # Loop through and show each assessment
        for i, a in enumerate(self.manager.assessments, 1):
            tk.Label(self.root, text=f"{i}. {a}").grid(row=i, column=0, sticky="w", padx=10)

        tk.Button(self.root, text="Back", command=self.main_menu, width=10).grid(row=len(self.manager.assessments)+1, column=0, pady=10)

    # --- View Credits Window ---
    def show_credits_window(self):
        self.clear_window()

        total = self.manager.total_credits()
        completed = self.manager.completed_credits()

        tk.Label(self.root, text="Credits Summary", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text=f"Total Credits: {total}").grid(row=1, column=0, sticky="w", padx=10)
        tk.Label(self.root, text=f"Completed Credits: {completed}").grid(row=2, column=0, sticky="w", padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=10).grid(row=3, column=0, pady=10)

    # --- Save Data to File ---
    def save_data(self):
        success = self.manager.save_to_file()
        if success:
            messagebox.showinfo("Success", "All data saved to assessments.txt successfully!")
        else:
            messagebox.showerror("Error", "Failed to save data to file.")

# run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = AssessmentTrackerApp(root)
    root.mainloop()
