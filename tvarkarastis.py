import tkinter as tk
from pyllist import sllist, sllistnode
import os
import json

def ivedimas():
    week = sllist([sllist(), sllist(), sllist() , sllist(), sllist(), sllist(), sllist()])
    num = input("Iveskite skaiciu\n1.Skaityti savaites darbo plana\n2.Rasti kliento savaites treniruotes pagal varda\n3.Redaguoti tvarkarasti\n4.Isvesti savaites tvarkarasti i ekrana\n5.Uzdaryti programa\n")
    if num == 1:
        fileName = input("Iveskite failo pavadinima: ")
        if os.path.isfile(fileName):
            f = json.loads(fileName)
            for x in f:
                print(x)
        else:
            str = input("Sios savaites dienotvarke yra tuscia. Ar norite ja papildyti? (Taip/Ne): ")
            if str == "Taip":
                counter = 1
                while counter < 8:
                    if counter == 1:
                        print("Pirmadienis")
                    elif counter == 2:
                        print("Antradienis")
                    elif counter == 3:
                        print("Treciadienis")
                    elif counter == 4:
                        print("Ketvirtadienis")
                    elif counter == 5:
                        print("Penktadienis")
                    elif counter == 6:
                        print("Sestadienis")
                    elif counter == 7:
                        print("Sekmadienis")
                    day = week.nodeat(counter - 1)
                    date = input("Data: ")
                    time = input("Laikas: ")
                    name = input("Vardas: ")
                    surname = input("Pavarde")
                    exercises = input("Pratimai: ")
                    duomenys = {"date":date, "time":time, "name":name, "surname":surname, "exercises":exercises}
                    day.appendright(duomenys)
                    cond = input("Ar norite pereiti i kita diena? (Taip/Ne): ")
                    if cond == "Taip":
                        if counter == 7:
                            week.remove(7)
                            week.appendright(day)
                            break
                        else:
                            week.remove(counter)
                            week.insertbefore(counter, day)
                            counter += 1
            f = open(fileName, "w")
            f.write(json.dumps(week))
    elif num == 2:
        fileName = input("Iveskite failo pavadinima: ")
        if os.path.isfile(fileName):
            week = json.loads(fileName)
            vardas = input("Iveskite varda: ")
            pavarde = input("Iveskite pavarde: ")
            num = False
            lineList = []
            lineListNext = []
            for x in week:
                lineList.append(x)
                if num:
                    lineListNext.append(x)
                else:
                    num = True
            for i in range(len(lineList) - 1):
                if lineList[i] == "Vardas: " + vardas and lineList[i + 1] == "Pavarde: " + pavarde:
                    print(lineList[i - 2])
                    print(lineList[i - 1])
                    print(lineList[i])
                    print(lineList[i + 1])
                    print(lineList[i + 2])
    #elif num == 3:
        
#main
# Function to handle button click
def on_button_click(button_number):
    text_output.config(state=tk.NORMAL)  # Allow editing of the text widget
    text_output.insert(tk.END, f"Button {button_number} Clicked!\n")
    text_output.config(state=tk.DISABLED)  # Disable editing of the text widget

# Create the main window
window = tk.Tk()
window.title("Text Output with Menu")

# Create a text widget for text output
text_output = tk.Text(window, state=tk.DISABLED)
text_output.grid(row=0, column=0, columnspan=5)

# Create a menu
menu = tk.Menu(window)
window.config(menu=menu)

# Create a File menu with an Exit option
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.quit)

# Create wider buttons labeled "1," "2," "3," "4," and "5" in a horizontal layout
button_width = 10  # Adjust the width as desired
for i in range(1, 6):
    button = tk.Button(window, text=str(i), width=button_width, command=lambda i=i: on_button_click(i))
    button.grid(row=1, column=i - 1)

# Run the application
window.mainloop()
#while True:
week = sllist([sllist(), sllist(), sllist() , sllist(), sllist(), sllist(), sllist()])
num = input("Iveskite skaiciu\n1.Skaityti savaites darbo plana\n2.Rasti kliento savaites treniruotes pagal varda\n3.Redaguoti tvarkarasti\n4.Isvesti savaites tvarkarasti i ekrana\n5.Uzdaryti programa\n")
if num == 1:
    ivedimas()
        