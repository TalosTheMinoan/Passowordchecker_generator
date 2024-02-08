import re
import math
import random
import string

class PasswordChecker:
    def __init__(self):
        self.password_blacklist = set(["password", "123456", "qwerty", "letmein", "monkey", "123456789", "password1"])  # Sample blacklist
        self.special_characters = "!@#$%^&*()-_+="

    def check_password_strength(self, password):
        if password.lower() in self.password_blacklist:
            return "Weak", "Password is part of a known blacklist of commonly used or compromised passwords."

        if len(password) < 8:
            return "Weak", "Password should be at least 8 characters long."

        if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            return "Weak", "Password should contain both uppercase and lowercase letters."

        if not any(char.isdigit() for char in password):
            return "Weak", "Password should contain at least one digit."

        if not any(char in self.special_characters for char in password):
            return "Weak", f"Password should contain at least one special character ({self.special_characters})."

        return "Strong", "Password is strong."

    def suggest_edits(self, password):
        edits = []

        if len(password) < 8:
            edits.append("Add more characters to the password.")

        if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            edits.append("Include both uppercase and lowercase letters in the password.")

        if not any(char.isdigit() for char in password):
            edits.append("Add at least one digit to the password.")

        if not any(char in self.special_characters for char in password):
            edits.append(f"Add at least one special character ({self.special_characters}) to the password.")

        return edits

    def estimate_crack_time(self, password):
        character_set = 94  # Number of possible characters (uppercase, lowercase, digits, and common symbols)
        password_length = len(password)
        entropy = math.log(character_set ** password_length, 2)  # Entropy in bits
        crack_time_seconds = 0.5 * (2 ** entropy) / (2 * (10 ** 12))  # Time to crack in seconds (assuming 1000 guesses per second)
        crack_time_hours = crack_time_seconds / 3600  # Time to crack in hours
        crack_time_years = crack_time_hours / 8760  # Time to crack in years
        return round(crack_time_years, 2)

    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + self.special_characters
        return ''.join(random.choice(characters) for _ in range(length))

    def run(self):
        print("Welcome to the Password Strength Checker and Generator!")
        print("1. Check password strength")
        print("2. Generate password")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            password = input("Enter your password: ")
            strength, suggestion = self.check_password_strength(password)
            print(f"Password Strength: {strength}")
            if strength == "Weak":
                print(f"Suggestion: {suggestion}")
                print("Possible edits to strengthen the password:")
                for edit in self.suggest_edits(password):
                    print("-", edit)
                crack_time_years = self.estimate_crack_time(password)
                print(f"Estimated time to crack: {crack_time_years} years")
        elif choice == "2":
            length = int(input("Enter the length of the password to generate: "))
            generated_password = self.generate_random_password(length)
            print(f"Generated password: {generated_password}")
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    checker = PasswordChecker()
    checker.run()
