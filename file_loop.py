import os

for file in os.listdir():
    if file.endswith('.py'):
        with open(file, 'r') as f:
            print(f.read())