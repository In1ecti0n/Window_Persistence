import subprocess

def Create(name, path):
    command = ["sc","create", name, f"binPath= {path}"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("CreateSuccessfully")
    else:
        print("Error")

def Delete(name):
    command = ["sc", "delete", name]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("DeleteSuccessfully")
    else:
        print("Error")

def Change(name, mode):
    command = ["sc", "config", name, f"start= {mode}"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("ChangeSuccessfully")
    else:
        print("Error")

print("1. Create service.")
print("2. Delete service.")
print("3. Change service.")

while True:
    number = int(input("Please choose option you want: "))
    if number == 1:
        name = input("Please type service name: ")
        path = input("Please type path: ")
        Create(name, path)
        break
    elif number == 2:
        name = input("Please type service name: ")
        Delete(name)
        break
    elif number == 3:
        name = input("Please type service name: ")
        mode = input("Mode (auto, disabled, manual): ")
        Change(name, mode)
        break
    else:
        print("Invalid option. Please try again.")
