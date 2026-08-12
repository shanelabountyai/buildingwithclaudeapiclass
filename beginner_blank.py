%pip install anthropic python-dotenv
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
message.content[0].text




# Beginner Python starter file
# Follow along in class and fill in each section.

# 1. Variables
# A variable stores a value.
# Example:
# name = "Alice"
# age = 21


# 2. Input and output
# Use print() to show information in the terminal.
# Example:
# print("Hello, world!")


# 3. Data types
# Strings, integers, floats, booleans, lists, and dictionaries.
# Example:
# favorite_color = "blue"
# number_of_students = 20
# is_ready = True
# names = ["Ava", "Ben", "Cora"]
# student = {"name": "Alex", "age": 19}


# 4. Conditional statements
# Use if, elif, and else to make decisions.
# Example:
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# 5. Loops
# Use for loops and while loops to repeat actions.
# Example:
# for name in names:
#     print(name)
#
# count = 0
# while count < 3:
#     print(count)
#     count += 1


# 6. Functions
# A function is a reusable block of code.
# Example:
# def greet(name):
#     return "Hello, " + name
#
# print(greet("Jordan"))


# 7. Lists and dictionaries practice
# Example:
# students = ["Sam", "Jules", "Priya"]
# print(students[0])
#
# student_data = {"name": "Sam", "grade": "A"}
# print(student_data["name"])


# 8. Your own code starts here


