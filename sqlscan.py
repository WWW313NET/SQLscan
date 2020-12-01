import os
import subprocess
print(" ___  ___  _     ___  ___    _")
print("|_ -||  .|| |   |_ -|| __|  / \  |\  |")
print("|___||_  || |_  |___|||__  /___\ | \ |  ")
print("       |_||___|      |___| |   | |  \|")
print("Version 1.0")
print("enter a number")
print("1 >> upgrade SQL scan")
print("2 >> finds sites vulnerable to SQL injection")
try:
    sql = int(input("number: "))

    if(sql == 1):
        os.system("cd ..")
        os.system("git clone https://github.com/WWW313NET/sqlscan")
        print("SQL scan is update")
    if(sql == 2):
        print("select a dork:")
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("6")
        print("7")
        print("8")
        print("9")
        print("10")
        print("11")
        print("12")
        print("13")
        print("14")
        print("15")
        print("16")
        print("17")
        print("18")
        print("19")
        print("20")
        print("21")
        print("22")
        print("23")
        print("24")

    dork = int(input("select a dork: "))

    if(dork == 1):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:login.asp", shell=True)

    elif(dork == 2):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:admin_login.asp", shell=True)
    
    elif(dork == 3):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:adminlogon.asp", shell=True)
    

    elif(dork == 4):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:admin_logon.asp", shell=True)

    
    elif(dork == 5):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:\admin/admin_login.php", shell=True)
    

    elif(dork == 6):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin.asp", shell=True)
    
    elif(dork == 7):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/login.asp", shell=True)

    
    elif(dork == 8):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/logon.asp", shell=True)
    
    elif(dork == 9):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/adminlogin.asp", shell=True)
    
    elif(dork == 10):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/adminlogon.asp", shell=True)
    
    elif(dork == 11):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin_login.asp", shell=True)
    
    elif(dork == 12):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin_logon.asp", shell=True)
    
    elif(dork == 13):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/admin.asp", shell=True)
    
    elif(dork == 14):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/login.asp", shell=True)

    
    elif(dork == 15):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/logon.asp", shell=True)

    
    elif(dork == 16):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/adminlogin.asp", shell=True)

    
    elif(dork == 17):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/adminlogon.asp", shell=True)

    
    elif(dork == 18):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/admin_login.asp", shell=True)

    
    elif(dork == 19):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/admin/admin_logon.asp", shell=True)

    
    elif(dork == 20):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/administrator/admin.asp", shell=True)

    
    elif(dork == 21):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/administrator/login.asp", shell=True)

    
    elif(dork == 22):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:/administrator/logon.asp", shell=True)

    
    elif(dork == 23):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:root/login.asp", shell=True)
    
    elif(dork == 24):
        subprocess.call("firefox https://duckduckgo.com/?q=inurl:admin/index.asp", shell=True)
    else:
        print("you have an error in your syntax SQL")



except:
    print("you have an error in your syntax SQL")





