from datetime import datetime

class ContactHandler:
    def __init__(self, name=None, mobile=None, problem=None):
        self.name = name
        self.mobile = mobile
        self.problem = problem
        self.dateAndTime = None

    def set_data(self, name, mobile, problem):
        self.name = name
        self.mobile = mobile
        self.problem = problem
        self.dateAndTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_to_file(self):
        with open("data/contact.txt", "a",encoding="utf-8") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Mobile: {self.mobile}\n")
            f.write(f"Problem: {self.problem}\n")
            f.write(f"Submitted on: {self.dateAndTime}\n")
            f.write("-" * 30 + "\n")