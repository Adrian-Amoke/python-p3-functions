#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    else:
        return number / 2

    
print(greet_programmer())
print(greet("Naureen"))
print(greet_with_default())
print(greet_with_default("Sunny")) 
print(add(45,55))  
print(halve(4))
print(halve("two"))
