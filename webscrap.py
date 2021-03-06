import requests
from bs4 import BeautifulSoup
from string import digits
import sys
import os.path
from os import system, name

filenotexist = 0
refrnr = 0
tryagain = 1


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if os.path.isfile("webscrapuid"):
    filenotexist = 0
else:
    filenotexist = 1
    uidpreset = ""

if filenotexist == 0:
    f = open("webscrapuid", "r")
    uidpresetlines = f.read()
    uidpreset = "".join(uidpresetlines.splitlines())

uidpreset = ''.join(c for c in uidpreset if c in digits)

if uidpreset == "" or filenotexist == 1:
    uid = int(input("Enter a valid UID: "))
    struid = str(uid)
    savechoice = int(input("Type 1 to save UID for automatic use (can change later): "))
    if savechoice == 1:
        f = open("webscrapuid", "w")
        f.write(struid)
        f.close()
        if filenotexist == 1:
            print("Saved UID file successfully created")
        print("UID was successfully saved")
        print("")
    else:
        print("UID not saved")
        print("")
else:
    struid = uidpreset

while True:
    print("Refresh attempt no.", str(refrnr))
    url = "https://minecraftathome.com/minecrafthome/show_user.php?userid=" + struid
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    wronguid = soup.findAll("h2")[0].get_text()
    if "Unable to handle request" in wronguid:
        print("The user ID [", struid, "] is nonexistent.", sep="")
        wrongg = 1
    else:
        wrongg = 0
        info = soup.findAll(style="padding-left:12px")[3]
        result = str(info)
        total_creds = ""
        for i in range(len(result)):
            if i != 10:
                total_creds = total_creds + result[i]
        total_creds2 = ""
        for i in range(len(total_creds)):
            if i != 27:
                total_creds2 = total_creds2 + total_creds[i]
        not_allowed_list = ["<td style=padding-left:12px>", "</td>"]
        for not_allowed_list_item in not_allowed_list:
            total_creds2 = total_creds2.replace(not_allowed_list_item, "")
        info2 = soup.findAll(style="padding-left:12px")[4]
        result2 = str(info2)
        total_creds3 = ""
        for i in range(len(result2)):
            if i != 10:
                total_creds3 = total_creds3 + result2[i]
        total_creds4 = ""
        for i in range(len(total_creds3)):
            if i != 27:
                total_creds4 = total_creds4 + total_creds3[i]
        not_allowed_list = ["<td style=padding-left:12px>", "</td>"]
        for not_allowed_list_item in not_allowed_list:
            total_creds4 = total_creds4.replace(not_allowed_list_item, "")
        print("Total credits for UID [", struid, "]: ", total_creds2, sep="")
        print("Total recent average credits for UID [", struid, "]: ", total_creds4, sep="")
        print("")
    while tryagain == 1:
        if wrongg == 0:
            optend = input("Type 'r' to refresh with same UID, 'a' to search for another UID, 'x' to exit or 'c' to"
                           " clear all text: ")
        if wrongg == 1:
            optend = input("Type 'a' to search for another UID, 'x' to exit or 'c' to clear all text: ")
        if wrongg == 0:
            if optend == "r":
                refrnr = refrnr + 1
                print(" ")
                print("Refreshing...")
                print(" ")
                break
            else:
                if optend == "a":
                    refrnr = 0
                    print(" ")
                    uid = int(input("Enter new UID: "))
                    savechoice2 = input("Type 'a' if you want to save this new UID: ")
                    struid = str(uid)
                    if savechoice2 == "a" or savechoice2 == "A":
                        f = open("webscrapuid", "w")
                        f.write(struid)
                        f.close()
                        print("New UID saved successfully!")
                    else:
                        print("New UID not saved.")
                    print(" ")
                    break
                else:
                    if optend == "x":
                        print("Script ended successfully.")
                        sys.exit(69)
                    else:
                        if optend == "c":
                            clear()
                            print("Text cleared!")
                        else:
                            tryagain = 1
        if wrongg == 1:
            if optend == "a":
                refrnr = 0
                print(" ")
                uid = int(input("Enter new UID: "))
                struid = str(uid)
                print(" ")
                break
            else:
                if optend == "x":
                    print("Script ended successfully.")
                    sys.exit(69)
                else:
                    if optend == "c":
                        clear()
                        print("Text cleared!")
                    else:
                        tryagain = 1
