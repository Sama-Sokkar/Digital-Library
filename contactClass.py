class ContactHandler:
    def __init__(self, name=None, mobile=None, problem=None):
        self.name = name
        self.mobile = mobile
        self.problem = problem

    def set_data(self, name, mobile, problem):
        self.name = name
        self.mobile = mobile
        self.problem = problem

    def save_to_file(self):
        with open("data/contact.txt", "a") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Mobile: {self.mobile}\n")
            f.write(f"Problem: {self.problem}\n")
            f.write("-" * 30 + "\n")