import re

text = input("Enter a text: ")

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)