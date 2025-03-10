import os

def insecure_system_call(user_input):
    os.system("echo " + user_input)  # ❌ Unsafe: Can execute shell commands

user_input = input("Enter command: ")
insecure_system_call(user_input)
