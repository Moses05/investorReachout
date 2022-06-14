import webbrowser as wb
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *

def pickMode():
    # newWindow = Tk()
    # newWindow.title("Progress Property Investor Reachout")
    # newWindow.geometry("600x400")
    # newWindow.resizable(False, False)

    # pickMode = Label(newWindow, text="Deciding type of text", fg="black",).pack()


    # nameNumber = input("Do you have the name, number and location? (yes or no) ").upper()

    # incorrectInput = True

    # while incorrectInput == True:
    #     if nameNumber == "YES":
    #         mode = 2
    #         incorrectInput = False
    #     elif nameNumber == "NO":
    #         mode = 1
    #         incorrectInput = False
    #     else:
    #         print("Incorrect Input")
    #         nameNumber = input("Do you have the name and number? (yes or no) ").upper()

    # return mode
    pass

# def createMode1Message():
#     investorName = input("Enter the name of the investor: ")
#     investorNumber = input("Enter the number of the investor: ")

#     return investorName, investorNumber

# def createMode2Message():
#     investorName = input("Enter the name of the investor: ")
#     investorNumber = input("Enter the number of the investor: ")
#     investorLocation = input("Enter the location of interest of the investor: ")

#     return investorName, investorNumber, investorLocation


# def mode1(name, number):
#     message = "https://api.whatsapp.com/send?phone=" + number + "&text=Hello%20" + name + "%2C%20%0A%0ANice%20to%20be%20in%20contact%2C%20I'm%20from%20Progress%20Property%2C%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0A%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%0A%0ALook%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0AJeff%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

#     print(message)

#     return message

# def mode2(name, number, location):
#     message = "https://api.whatsapp.com/send?phone=" + number + "&text=Hey%20" + name + "%2C%20%0A%0AMy%20company%20Progress%20Property%20Services%20has%20previously%20been%20in%20contact%20with%20you%20in%20regards%20to%20your%20search%20for%20properties%20located%20around%20" + location + ".%20%0A%0AWe%20have%20several%20new%20deals%20available%20and%20are%20hoping%20there%20is%20new%20business%20that%20can%20be%20done%20with%20you%20if%20you%20are%20still%20interested%20%3F%20%0A%0AKind%20regards%20%0A%0AJeff%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

#     return message

# continueProgram = True

# while continueProgram == True: 
#     if pickMode() == 1:
#         investorName, investorNumber = createMode1Message()
#         mode1(investorName, investorNumber)
#     else:
#         investorName, investorNumber, investorLocation = createMode2Message()
#         mode2(investorName, investorNumber, investorLocation)

#     userOption = input("Do you want to continue? (yes or no): ").upper()

#     if userOption == "YES":
#         continueProgram = True

#     elif userOption == "NO":
#         continueProgram = False
#     else:
#         print("Incorrect input, start the program again")

def mode1():
    mode1Window = Tk()
    mode1Window.title("Mode 1 (Name and Number only)")
    mode1Window.geometry("600x400")
    mode1Window.resizable(False, False)

    Label(mode1Window, text="Enter the Name of the Investor")
    investorNameInput = Entry(mode1Window, fg="white").pack()
    investorNameInput.insert(0, "Investor Name: ")

root = Tk()
root.title("Progress Property Investor Reachout")
root.geometry("850x400")
root.resizable(False, False)


welcomeText = Label(root, text="Welcome to Progress Property Services", fg="black",pady=20).grid(column=1,row=0)

mode1SelectLabel = Label(root, text="Mode 1 (If you only have name and number)", fg="black",pady=10,padx=10).grid(column=0, row=1)
mode1SelectButton = Button(root, text="Mode 1", fg="black",command=mode1).grid(column=0, row=2)

mode2SelectLabel = Label(root, text="Mode 2 (If you have name, number and location)", fg="black",pady=10,padx=10).grid(column=2, row=1)
mode2SelectButton = Button(root, text="Mode 2", fg="black",).grid(column=2, row=2)


root.mainloop()
