import tkinter as tk
from tkinter import ttk, messagebox

class GradeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("University Grade Calculator")

        self.semesters = []
        self.current_semester_index = 0

        self.create_widgets()

    def create_widgets(self):
        # Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, expand=True, fill="both")

        # Add Semester Tab
        self.add_semester_tab()

        # GPA Display
        self.gpa_label = tk.Label(self.root, text="Final GPA: ", font=("Helvetica", 12))
        self.gpa_label.pack(pady=10)

    def add_semester_tab(self):
        semester_frame = ttk.Frame(self.notebook)

        # Semester Information
        tk.Label(semester_frame, text="Semester Name:").grid(row=0, column=0, padx=5, pady=5)
        semester_name_entry = tk.Entry(semester_frame)
        semester_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(semester_frame, text="Credits:").grid(row=1, column=0, padx=5, pady=5)
        credits_entry = tk.Entry(semester_frame)
        credits_entry.grid(row=1, column=1, padx=5, pady=5)

        # Grade Entries
        tk.Label(semester_frame, text="Grades (separated by commas):").grid(row=2, column=0, padx=5, pady=5)
        grades_entry = tk.Entry(semester_frame)
        grades_entry.grid(row=2, column=1, padx=5, pady=5)

        # Calculate Button
        calculate_button = tk.Button(semester_frame, text="Calculate GPA", command=lambda: self.calculate_gpa(
            semester_name_entry.get(), credits_entry.get(), grades_entry.get()
        ))
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.notebook.add(semester_frame, text="Semester {}".format(len(self.semesters) + 1))
        self.semesters.append({
            "name": semester_name_entry,
            "credits": credits_entry,
            "grades": grades_entry,
            "gpa_label": tk.Label(semester_frame, text="GPA: "),
        })

    def calculate_gpa(self, semester_name, credits, grades):
        try:
            credits = float(credits)
            grade_list = [float(grade.strip()) for grade in grades.split(",")]

            if credits <= 0 or any(g < 0 or g > 4 for g in grade_list):
                messagebox.showerror("Error", "Invalid input. Credits should be positive, and grades should be between 0 and 4.")
                return

            semester_gpa = sum(grade_list) / len(grade_list)
            weighted_gpa = semester_gpa * credits

            self.semesters[self.current_semester_index]["gpa_label"].config(
                text="GPA: {:.2f}".format(semester_gpa)
            )

            self.update_final_gpa(weighted_gpa, credits)

            # Move to the next semester
            self.current_semester_index += 1
            self.add_semester_tab()
            self.notebook.select(len(self.semesters) - 1)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for credits and grades.")

    def update_final_gpa(self, weighted_gpa, credits):
        total_weighted_gpa = sum(semester["weighted_gpa"] for semester in self.semesters)
        total_credits = sum(semester["credits"] for semester in self.semesters)

        total_weighted_gpa += weighted_gpa
        total_credits += credits

        final_gpa = total_weighted_gpa / total_credits

        self.gpa_label.config(text="Final GPA: {:.2f}".format(final_gpa))


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculator(root)
    root.mainloop()
