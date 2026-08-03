# Dynamic Report Generator using OOP

# Decorator
def report_header(func):

    def wrapper(self):
        print("=" * 40)
        print("       DYNAMIC REPORT")
        print("=" * 40)

        func(self)

        print("=" * 40)

    return wrapper


class Report:

    # Class Variable
    template = "General Report"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template
        print("Template changed successfully.")

    # Magic Method
    def __str__(self):
        return (
            "Title: " + self.title +
            "\nTemplate: " + Report.template +
            "\nContent: " + self.content
        )

    # Decorator
    @report_header
    def generate_report(self):
        print(self)


# ---------------- Main Program ----------------

while True:

    print("\n===== Dynamic Report Generator =====")
    print("1. Change Report Template")
    print("2. Generate Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        new_template = input("Enter New Template Name: ")
        Report.change_template(new_template)

    elif choice == "2":

        title = input("Enter Report Title: ")
        content = input("Enter Report Content: ")

        report = Report(title, content)
        report.generate_report()

    elif choice == "3":

        print("Thank You!")
        break

    else:

        print("Invalid Choice.")