import subprocess

def Create(name, path, trigger):
    command = [
        "schtasks",     #https://learn.microsoft.com/vi-vn/windows-server/administration/windows-commands/schtasks-create
        "/create",
        "/tn", name,
        "/tr", path,
        "/sc", f"{trigger}"
    ]
    result = subprocess.run(command, check=True)
    if result.returncode == 0:
        print("CreateSuccessfully")
    else:
        print("Error")

    
def Delete(name):
    command = ["schtasks", "/delete", "/tn", name, "/f"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("DeleteSuccessfully")
    else:
        print("Error")

def Change(name, time, path):
    command = [
        "schtasks", 
        "/change",
        "/tn", name,
        "/sc", f"{time}",
        "/tr", path
    ]
    result = subprocess.run(command, check = True)
    if result.returncode == 0:
        print("ChangeSuccessfully")
    else:
        print("Error")


print ("1. Create task scheduler.")
print ("2. Delete task scheduler.")
print ("3. Change task scheduler.")
number = int(input("Please choose option you want:")) 
while(1):   
    if (number == 1):
        name = str(input("Please type task name:"))
        path = str(input("Please type path:"))
        trigger = str(input("ONLOGON or ONSTARTUP:"))
        Create(name, path, trigger)
        break
    elif (number == 2):
        name = str(input("Please type task name:"))
        Delete(name)
        break
    elif (number == 3):
        name = str(input("Please type task name:"))
        time = str(input("ONLOGON or ONTSTARTUP:"))
        path = str(input("New path:"))
        Change(name, time, path)
        break
    else:
        number = int(input("Type again:"))
    
