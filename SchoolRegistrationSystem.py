import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("School Registration System")
root.geometry("360x320")
root.resizable(False, False)

def defaultSystem():
    StudentRB.config(state='normal')
    FacultyRB.config(state='normal')
    NonTeachRB.config(state='normal')
    NameEntry.config(state='disabled')
    TitleCB.config(state='disabled')
    AgeEntry.config(state='disabled')
    MonthCB.config(state='disabled')
    DateCB.config(state='disabled')
    YearCB.config(state='disabled')
    AddressEntry.config(state='disabled')
    FirstYrRB.config(state='disabled')
    SecondYrRB.config(state='disabled')
    ThirdYrRB.config(state='disabled')
    FourthYrRB.config(state='disabled')
    DeptCB.config(state='disabled')
    VerifyCB.config(state='disabled')
    RegisterBTN.config(state='disabled')


def enableStudent():
    defaultSystem()
    StudentRB.config(state='normal')
    FacultyRB.config(state='normal')
    NonTeachRB.config(state='normal')
    NameEntry.config(state='normal')
    TitleCB.config(state='readonly')
    AgeEntry.config(state='normal')
    MonthCB.config(state='readonly')
    DateCB.config(state='readonly')
    YearCB.config(state='readonly')
    AddressEntry.config(state='normal')
    FirstYrRB.config(state='normal')
    SecondYrRB.config(state='normal')
    ThirdYrRB.config(state='normal')
    FourthYrRB.config(state='normal')
    DeptCB.config(state='readonly')
    VerifyCB.config(state='normal')
    RegisterBTN.config(state='normal')


def enableFaculty():
    defaultSystem()
    StudentRB.config(state='normal')
    FacultyRB.config(state='normal')
    NonTeachRB.config(state='normal')
    NameEntry.config(state='normal')
    TitleCB.config(state='readonly')
    AgeEntry.config(state='normal')
    MonthCB.config(state='readonly')
    DateCB.config(state='readonly')
    YearCB.config(state='readonly')
    AddressEntry.config(state='normal')
    FirstYrRB.config(state='disabled')
    SecondYrRB.config(state='disabled')
    ThirdYrRB.config(state='disabled')
    FourthYrRB.config(state='disabled')
    DeptCB.config(state='normal')
    VerifyCB.config(state='normal')
    RegisterBTN.config(state='normal')
def enableNonTeach():
    defaultSystem()
    StudentRB.config(state='normal')
    FacultyRB.config(state='normal')
    NonTeachRB.config(state='normal')
    NameEntry.config(state='normal')
    TitleCB.config(state='readonly')
    AgeEntry.config(state='normal')
    MonthCB.config(state='readonly')
    DateCB.config(state='readonly')
    YearCB.config(state='readonly')
    AddressEntry.config(state='normal')
    FirstYrRB.config(state='disabled')
    SecondYrRB.config(state='disabled')
    ThirdYrRB.config(state='disabled')
    FourthYrRB.config(state='disabled')
    DeptCB.config(state='normal')
    VerifyCB.config(state='normal')
    RegisterBTN.config(state='normal')

def clear():
    NameEntry.delete(0, tk.END)
    TitleCB.set("")
    AgeEntry.delete(0, tk.END)
    MonthCB.set("")
    DateCB.set("")
    YearCB.set("")
    AddressEntry.delete(0, tk.END)
    DeptCB.set("")
    VerifyCB.deselect()
    StudentRB.deselect()
    FacultyRB.deselect()
    NonTeachRB.deselect()
    FirstYrRB.deselect()
    SecondYrRB.deselect()
    ThirdYrRB.deselect()
    FourthYrRB.deselect()
    defaultSystem()

def register():
    if Verification.get() == 0:
        messagebox.showerror("Registration", "Please verify your information!")
    else:
        messagebox.showinfo("Registration", "Registration successful!")

Enrollment = tk.StringVar()
Enrollment.set("")
ProgName = tk.Label(root, text="School Registration System").grid(row=0, column=0, padx=100, sticky="w")
StudentRB = tk.Radiobutton(root, text="Student", variable=Enrollment, value="Student", command=enableStudent, state='disabled')
StudentRB.grid(row=1, column=0, padx=30, pady=5, sticky="w")
FacultyRB = tk.Radiobutton(root, text="Faculty", variable=Enrollment, value="Faculty", command=enableFaculty, state='disabled')
FacultyRB.grid(row=1, column=0, padx=130, pady=5, sticky="w")
NonTeachRB = tk.Radiobutton(root, text="NonTeach", variable=Enrollment, value="Non Teach", command=enableNonTeach, state='disabled')
NonTeachRB.grid(row=1, column=0, padx=230, pady=5, sticky="w")

NameLabel = (tk.Label(root, text="Name").grid(row=2, column=0, padx=10, sticky="w"))
NameEntry = tk.Entry(root, width=29)
NameEntry.grid(row=2, column=0, padx=50, pady=10, sticky="w")
TitleLabel = tk.Label(root, text="Title").grid(row=2, column=0, padx=250, pady=10, sticky="w")
TitleCB = ttk.Combobox(root, values = ["Mr.", "Mrs.","Ms."], state='readonly', width=5)
TitleCB.grid(row=2, column=0,padx=285, pady=10, sticky="w")

AgeLabel = tk.Label(root, text="Age").grid(row=3, column=0, padx=20, sticky="w")
AgeEntry = tk.Entry(root, width=5)
AgeEntry.grid(row=3, column=0, padx=50, pady=10, sticky="w")
BirthdateLabel = tk.Label(root, text="Birthdate").grid(row=3, column=0, padx=90, pady=10, sticky="w")
MonthCB = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state='readonly', width=10)
MonthCB.grid(row=3, column=0, padx=145, pady=10,sticky="w")
DateCB = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22","23", "24", "25", "26", "27", "28", "29", "30", "31"], state='readonly', width=3)
DateCB.grid(row=3, column=0, padx=236, pady=10,sticky="w")
YearCB = ttk.Combobox(root, values=[" ", "2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017",
                                               "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008",
                                               "2007", "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999",
                                               "1998", "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990",
                                               "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981",
                                               "1980", "1979", "1978", "1977", "1976", "1975", "1974", "1973", "1972",
                                               "1971", "1970"], state='readonly', width=5)
YearCB.grid(row=3, column=0, padx=285, pady=10,sticky="w")

AddressLabel = tk.Label(root, text="Address").grid(row=4, column=0, padx=0, sticky="w")
AddressEntry = tk.Entry(root, width=48)
AddressEntry.grid(row=4, column=0, padx=50, pady=10, sticky="w")

year = tk.StringVar()
year.set("")
FirstYrRB = tk.Radiobutton(root, text="First Year", variable=year, value="First Year",  state='disabled')
FirstYrRB.grid(row=5, column=0, padx=10, pady=5, sticky="w")
SecondYrRB = tk.Radiobutton(root, text="Second Year", variable=year, value="Second Year", state='disabled')
SecondYrRB.grid(row=5, column=0, padx=85, pady=5, sticky="w")
ThirdYrRB = tk.Radiobutton(root, text="Third Year", variable=year, value="Third Year", state='disabled')
ThirdYrRB.grid(row=5, column=0, padx=180, pady=5, sticky="w")
FourthYrRB = tk.Radiobutton(root, text="Fourth Year", variable=year, value="Fourth Year", state='disabled')
FourthYrRB.grid(row=5, column=0, padx=260, pady=5, sticky="w")

DeptLabel = tk.Label(root, text="Department").grid(row=6, column=0, padx=10, sticky="w")
DeptCB = ttk.Combobox(root, values=["College of Accountancy and Finance",
                                    "College of Architecture, Design and Built Environment",
                                    "College of Arts and Letters", "College of Business Administration",
                                    "College of Communication", "College of Computer and Information Sciences",
                                   "College of Education", "College of Engineering", "College of Human Kinetics",
                                    "College of Law", "College of Political Science and Public Administration",
                                    "College of Social Sciences and Development", "College of Science",
                                    "College of Tourism, Hospitality and Transportation Management"], state='readonly', width=40)
DeptCB.grid(row=6, column=0, padx=80, pady=10,sticky="w")

Verification = tk.BooleanVar()
VerifyCB = tk.Checkbutton(root, text="I agree to the Terms and Conditions.", variable=Verification)
VerifyCB.grid(row=7, column=0, padx=70, sticky="w")

RegisterBTN = tk.Button(root, text="Register", command=register, width=10, state='disabled')
RegisterBTN.grid(row=8, column=0, padx=100, sticky="w")
ClearBTN = tk.Button(root, text="Clear", command=clear, width=10).grid(row=8, column=0, padx=200, sticky="w")

defaultSystem()
root.mainloop()
