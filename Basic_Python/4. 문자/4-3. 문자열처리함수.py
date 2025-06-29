python = "Python is Amazing"

print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True
print(len(python)) # 17
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n") 
print(index) # 5

index = python.index("n", index + 1)
print(index) # 15

print(python.find("Java")) # -1
# print(python.index("Java")) # Error 발생

print(python.count("n")) # 2