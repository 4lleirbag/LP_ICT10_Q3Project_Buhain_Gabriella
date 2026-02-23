import document
print("=== Intramurals Eligibility Checker ===")


# Inputs
registered = input("Are you registered online? (yes/no): ").lower()
medical = input("Do you have a medical clearance? (yes/no): ").lower()
grade = int(input("Enter your grade level (7-10 only): "))
section = input("Enter your section: ").lower()


# Allowed sections per grade
grade7_sections = ["sapphire", "ruby", "topaz", "emerald"]
grade8_sections = ["sapphire", "ruby", "emerald"]
grade9_sections = ["sapphire", "ruby", "topaz", "emerald"]
grade10_sections = ["sapphire", "ruby", "emerald"]


# Eligibility checks
if registered != "yes":
    print("\n❌ You are NOT eligible.")
    print("👉 Please register online first.")


elif medical != "yes":
    print("\n❌ You are NOT eligible.")
    print("👉 Please secure a medical clearance.")


elif grade < 7 or grade > 10:
    print("\n❌ You are NOT eligible.")
    print("👉 Only Grades 7 to 10 are allowed.")


elif grade == 7 and section not in grade7_sections:
    print("\n❌ Invalid section for Grade 7.")
    print("👉 Allowed: Sapphire, Ruby, Topaz, Emerald")


elif grade == 8 and section not in grade8_sections:
    print("\n❌ Invalid section for Grade 8.")
    print("👉 Allowed: Sapphire, Ruby, Emerald")


elif grade == 9 and section not in grade9_sections:
    print("\n❌ Invalid section for Grade 9.")
    print("👉 Allowed: Sapphire, Ruby, Topaz, Emerald")
