
import random

repairs = {}
repairID = 0

def registration(repairs, repairID):
    cancelled = False
    while True:
        name = input("Enter your name: ").title() #Customer name.
        device = input("What type of device would you like to repair: ").capitalize() #Device type (laptop, desktop, etc.
        problem = input("Report problem (press 'e' to exit): ") #Reported problem. #Customer name, device type, and reported problem cannot be empty.

        if problem.lower()  == "e":
            cancelled = True
            break

        if name.strip() == "" or device.strip() == "" or problem.strip() == "":
            print("Name, device or problem input can't be empty")
            continue
        else:
            break
        
    if cancelled == True:
        return repairs, repairID

    repairID += 1
    repairs.update({repairID: {"Name": [name], "Device": [device], "Problem": [problem], "Status": "Pending", "Cost": [randumNum]}})
    return repairs, repairID

def view(repairs, repairID):
    for repair in repairs:
        print(f"Repair ID: {repair}, Name: {repairs[repair]["Name"][0]}, Device: {repairs[repair]["Device"][0]}\n"
                f"Problem: {repairs[repair]["Problem"][0]}\nStatus: {repairs[repair]["Status"]}\nFinal Cost: €{repairs[repair]["Cost"][0]}\n")
    return repairs, repairID


def search(repairs, repairID):
    while True:
        try:
            searchID = int(input("Search repair ID ('0' to exit): "))
        except ValueError:
            print("Invalid input")
            continue
        if searchID == 0:
            break
        if searchID not in repairs.keys(): #Searching for a nonexistent job ID must display an appropriate message.
            print("Invalid repair ID")
            continue
        else:
            print(f"{repairs[searchID]}")
    return repairs, repairID



def update(repairs, repairID):
    while True:
        try:
            updateRepair = int(input("Enter repair ID ('0' to exit): "))
        except ValueError:
            print("Invalid input")
            continue
        
        if updateRepair == 0:
            break

        if updateRepair not in repairs.keys():
            print("ID not found")
            continue

        try:
            newStatus = int(input("Update Status:\n"
            "1: Pending\n"
            "2: In Progress\n"
            "3: Copleted\n"))
        except ValueError:
            print("Invalid input")
            continue


        if newStatus == 1:
            repairs[updateRepair]["Status"] = "Pending"
        elif newStatus == 2:
            repairs[updateRepair]["Status"] = "In Progress"
        elif newStatus == 3:
            repairs[updateRepair]["Status"]= "Completed"
        else:
            print("Out of range")
            continue
    return repairs, repairID

while True:
    randumNum = random.randint(0, 201) #random price generator
    print() #Display a menu with options to register a repair, view all repairs, search by job ID, update a repair's status, and exit.
    print("-Mr Robot Repairs-")
    print("-------------------")
    print("1: Register repair")
    print("2: View repairs")
    print("3: Search ID")
    print("4: Update repair status")
    print("5: Exit")
    option = input("Choose option: ")
    print()
    


    if option == "1":
        repairs, repairID = registration(repairs, repairID)

    elif option == "2": #When viewing all repairs, display the job ID, customer, device, problem, status, and cost.
        repairs, repairID = view(repairs, repairID)

    elif option == "3": 
        repairs, repairID = search(repairs, repairID)

    elif option == "4": #When updating a repair, the user must select a valid job ID and status.
        repairs, repairID = update(repairs, repairID)

    elif option == "5":
        print("Exiting")
        break

    else: #Invalid input must not crash the program or accidentally register an incomplete repair.
        print("No such option")


#When exiting, display how many repairs were registered and how many are still pending.
pending = 0
for key, value in repairs.items():
    if value["Status"] == "Pending":
        pending += 1


print(f"Total repairs: {repairID}")
print(f"Pending repairs: {pending}")
