# Day 3 of code
#7/9/21
# Project Birthday storing app
#version 1
#problems cant check if person is already in dict, do date check
# plan to redo project with a csv file once i learn
import os

#This dictonary will store all Bdays given to it
def fill_Bdays(dict):
    """
     Take in a dictonary and return a filled dictonary
    """
    name = ""
    month_day = ""


    while True:
        print("Enter the name of the person or leave blank to quit:")
        name = input()
        # check to see if a name was entered
        if(name == ""):
            break
        print("Enther the month and day: ")
        month_day = input()
        dict[name] = month_day
    return dict
def name_File():
    """
     This function will create the name of the file and let user name it
    """
    fname = ""
    exten = ".txt"
    print("What would u like the name of your file to be...")
    fname = input()
    return fname+ exten
def make_File(fname):
    """
    This function will take in the name of the file created the create an actual file in cwd
    """
    f= open(fname,"w+")
    f.close()
    return f"The file {fname} has been created........"
def write_File(fname, dict):
    """
     This function will write our dictonary to our files
    """
    counter = 1
    f = open(fname,"w+")
    for k,v in dict.items():
        f.writelines(f"{counter}. {k} , {v}\n")
        counter +=1
    f.close()
    return f"files have been writtrn in {fname}......."
def read_File(fname):
    """
    Function will take in the file name and read it line for line

    """
    filename = open(fname,"r")
    readlin = filename.readlines()
    for line in readlin:
        print(line)
    filename.close()
    return f"These are files in {fname}"

def add_Files(fname,dict):
    """
     This function will take in  fname add appeded it to a file
    """
    name = ""
    bday_month = ""
    count = 1
    file_name = open(fname,"+a")
    while True:
        print("Enther the user name or leave blank to quit: ")
        name = input()
        if (name == ""):
            break
        print("Enther the month and the date: ")
        bday_month = input()
        dict[name] = bday_month
    for i in dict.items():
        file_name.writelines(f"{count}, {name}, {bday_month}")
        count +=1
    file_name.close()
    return f"Files have been added to file {fname}......"


print("This program is meant to save birthdays and write them to a text file.")
bday_dict = {}
fill_Bdays(bday_dict)
print("you must now write the files to a text.")
my_file = name_File()
print("The file has been name now time to create...")
make_File(my_file)
print("Time to write to file...")
write_File(my_file,bday_dict)
print("These is what is contained inside of your files.")
read_File(my_file)