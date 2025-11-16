import os
import platform
import urllib.request
import zipfile

def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def download_classic_server(url, file_name):
    path = os.path.join(os.gentenv('APPDATA'), '.mc-server') + file_name
    ver_len = len(file_name) - 4
    ver = file_name[:ver_len]
    ex_path = os.path.join(os.gentenv('APPDATA'), '.mc-server', ver)
    urllib.request.urlretrieve(url, path)
    with zipfile.ZipFile(path, 'r') as cserver:
        cserver.extractall(ex_path)

def download_server(url, file_name):
    path = os.path.join(os.gentenv('APPDATA'), '.mc-server') + file_name
    urllib.request.urlretrieve(url, path)

if __name__ == "__main__":
    clear()
    print("Copyright (c) NotHaDaoo 2025")
    print("Minecraft Java Edition server version downloader 1.0")
    while True:
        inp = input(">>> ")
        if inp == "q" or inp == "quit":
            break
        elif len(inp) < 8:
            print("Unexpected command.")
        elif inp[:8] == "download":
            if inp[8] != ' ':
                print("Unexpected command.")
            else:
                sver = "" #SVER = Server VERsion
                for i in range(len(inp) - 9):
                    sver += inp[i + 9]
                
                if sver[0] == 'c':
                    #classic server version
                    if sver == "c1.2":
                        #1.0 and 1.1 not archived
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.2.zip", "c1.2.zip")
                    elif sver == "c1.3":
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.3.zip", "c1.3.zip")
                    elif sver == "c1.4":
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.4-1327.zip", "c1.4.zip")
                    elif sver == "c1.4-reup":
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.4-1422.jar", "c1.4-reup.zip")
                    elif sver == "c1.4.1":
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.4.1.zip", "c1.4.1.zip")
                    elif sver == "c1.6":
                        #1.5 not archived
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.6.zip", "c1.6.zip")
                    elif sver == "c1.8.2":
                        #1.7, 1.8, 1.8.1 not archived
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.8.2.zip", "c1.8.2.zip")
                    elif sver == "c1.9" or sver == "c1.8.3":
                        #This is c1.8.3 but later renamed 1.9
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.8.3.zip", "c1.9.zip")
                    elif sver == "c1.9.1":
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.9.1.zip", "c1.9.1.zip")
                    elif sver == "c1.10":
                        #Not original. The archived is jar-only but the released is zip
                        download_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.10.jar", "c1.10.jar")
                    elif sver == "c1.10.1":
                        download_classic_server("https://vault.omniarchive.uk/archive/java/server-classic/c1.10.1.zip", "c1.10.1.zip")
                elif sver[0] == 'a':
                    if sver == "a0.1.0":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.0.jar", "a0.1.0.jar")
                    elif sver == "a0.1.0-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.0.exe", "a0.1.0.exe")
                    elif sver == "a0.1.1-reup":
                        #Original not archived
                        download_server("https://vault.omniarchive.uk/versions/java/server/alpha/a0.1.1-1707.jar", "a0.1.1-reup.jar")
                    elif sver == "a0.1.2_01":
                        #a0.1.2 not archived
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.2_01.jar", "a0.1.2_01.jar")
                    elif sver == "a0.1.2_01-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.2_01.exe", "a0.1.2_01.exe")
                    elif sver == "a0.1.3":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.3.jar", "a0.1.3.jar")
                    elif sver == "a0.1.3-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.3.exe", "a0.1.3.exe")
                    elif sver == "a0.1.4":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.4.jar", "a0.1.4.jar")
                    elif sver == "a0.1.4-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.1.4.exe", "a0.1.4.exe")
                    elif sver == "a0.2.0":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.0.jar", "a0.2.0.jar")
                    elif sver == "a0.2.0-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.0.exe", "a0.2.0.exe")
                    elif sver == "a0.2.0_01":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.0_01.jar", "a0.2.0_01.jar")
                    elif sver == "a0.2.0_01-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.0_01.exe", "a0.2.0_01.exe")
                    elif sver == "a0.2.1":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.1.jar", "a0.2.1.jar")
                    elif sver == "a0.2.1-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.1.exe", "a0.2.1.exe")
                    elif sver == "a0.2.2":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.2.jar", "a0.2.2.jar")
                    elif sver == "a0.2.2-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.2.exe", "a0.2.2.exe")
                    elif sver == "a0.2.2_01":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.2_01.jar", "a0.2.2_01.jar")
                    elif sver == "a0.2.2_01-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.2_01.exe", "a0.2.2_01.exe")
                    elif sver == "a0.2.3":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.3.jar", "a0.2.3.jar")
                    elif sver == "a0.2.3-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.3.exe", "a0.2.3.exe")
                    elif sver == "a0.2.4":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.4.jar", "a0.2.4.jar")
                    elif sver == "a0.2.4-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.4.exe", "a0.2.4.exe")
                    elif sver == "a0.2.5":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5-0923.jar", "a0.2.5.jar")
                    elif sver == "a0.2.5-reup":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5-1004.jar", "a0.2.5-reup.jar")
                    elif sver == "a0.2.5-reup-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5-1004.exe", "a0,2,5-reup.exe")
                    elif sver == "a0.2.5_01":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5_01.jar", "a0.2.5_01.jar")
                    elif sver == "a0.2.5_01-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5_01.exe", "a0.2.5_02.exe")
                    elif sver == "a0.2.5_02":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5_02.jar", "a0.2.5_02.jar")
                    elif sver == "a0.2.5_02-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.5_02.exe", "a0.2.5_02.exe")
                    elif sver == "a0.2.6":
                        #.exe not archived
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.6.jar", "a0.2.6.jar")
                    elif sver == "a0.2.6_01":
                        #.exe not archived
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.6_01.jar", "a0.2.6_01.jar")
                    elif sver == "a0.2.6_02":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.6_02.jar", "a0.2.6_02.jar")
                    elif sver == "a0.2.6_02-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.6_02.exe", "a0.2.6_02.exe")
                    elif sver == "a0.2.7":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.7.jar", "a0.2.7.jar")
                    elif sver == "a0.2.7-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.7.exe", "a0.2.7.exe")
                    elif sver == "a0.2.8":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.8.jar", "a0.2.8.jar")
                    elif sver == "a0.2.8-exe":
                        download_server("https://vault.omniarchive.uk/archive/java/server-alpha/a0.2.8.exe", "a0.2.8.exe")
        else:
            print("Unexpected command.")