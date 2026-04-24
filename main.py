import subprocess, os, pickle,llm

PASSWORD = "admin123"

def run_command(user_input):
    cmd = "echo " + user_input
    subprocess.call(cmd, shell=True)

def load_data(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)

def calculate(items=[]):
    total = 0
    for i in range(len(items)):
        total = total + items[i]
    return total

def check(value):
    if value == True:
        print("Valid")

def divide(a, b):
    try:
        return a / b
    except Exception:
        return None

def unused():
    x = 10
