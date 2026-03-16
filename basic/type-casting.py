x = "10"
y = int(x)  # Type casting from string to integer
print(y)  # Output: 10
print(type(y))  # Output: <class 'int'>

firstname = "ProgrammerBanda"
# firstname = int(firstname)  # This will raise a ValueError because "ProgrammerBanda" cannot be converted to an integer
print(firstname)
print(type(firstname))  # Output: <class 'str'>


isStudent = True
isStudentConvert = int(isStudent)
print(isStudentConvert)
