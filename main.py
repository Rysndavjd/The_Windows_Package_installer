import subprocess
import wget
import pyinputplus as pyip
import os 
import shutil

print("(Made by Rysndavjd)")
print("This script will download automatically and setup programs that you choose using python.")
print("To check for supported programs read the readme.txt.")

path = os.getcwd()


def VLC():
    pkg1 = pyip.inputChoice(["Y", "N"])

    if pkg1 == "Y":
        print("Downloading VLC.")
        VLC = "https://videolan.mirror.liquidtelecom.com/vlc/3.0.18/win32/vlc-3.0.18-win32.exe"
        wget.download(VLC, "vlc-3.0.18-win32.exe")
        source = path + r"\vlc-3.0.18-win32.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\vlc-3.0.18-win32.exe"])
    elif pkg1 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit


def NIL():
    pkg2 = pyip.inputChoice(["Y", "N"])

    if pkg2 == "Y":
        print("Downloading Nomacs Image Lounge")
        NIL = "https://github.com/nomacs/nomacs/releases/latest/download/nomacs-setup-x64.msi"
        wget.download(NIL, "nomacs-setup-x64.msi")
        source = path + r"\nomacs-setup-x64.msi"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\nomacs-setup-x64.msi"])
        breakpoint
    elif pkg2 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit


def NPP():
    pkg3 = pyip.inputChoice(["Y", "N"])

    if pkg3 == "Y":
        print("Downloading Notepad++")
        NPP = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.8/npp.8.4.8.Installer.x64.exe"
        wget.download(NPP, "npp.8.4.8.Installer.x64.exe")
        source = path + r"\npp.8.4.8.Installer.x64.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\npp.8.4.8.Installer.x64.exe"])
        breakpoint
    elif pkg3 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit


def ETS():
    pkg4 = pyip.inputChoice(["Y", "N"])

    if pkg4 == "Y":
        print("Downloading Everything Search")
        ETS = "https://www.voidtools.com/Everything-1.4.1.1022.x86-Setup.exe"
        wget.download(ETS, "Everything-1.4.1.1022.x86-Setup.exe")
        source = path + r"\Everything-1.4.1.1022.x86-Setup.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\Everything-1.4.1.1022.x86-Setup.exe"])
        breakpoint
    elif pkg4 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def z7zip():
    pkg5 = pyip.inputChoice(["Y", "N"])

    if pkg5 == "Y":
        print("Downloading 7zip")
        z7zip = "https://www.7-zip.org/a/7z2201-x64.exe"
        wget.download(z7zip, "7z2201-x64.exe")
        source = path + r"\7z2201-x64.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\7z2201-x64.exe"])
        breakpoint
    elif pkg5 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def WinRAR():
    pkg6 = pyip.inputChoice(["Y", "N"])

    if pkg6 == "Y":
        print("Downloading WinRAR")
        WinRAR = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-611.exe"
        wget.download(WinRAR, "winrar-x64-611.exe")
        source = path + r"\winrar-x64-611.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\winrar-x64-611.exe"])
        breakpoint
    elif pkg6 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def Recuva():
    pkg7 = pyip.inputChoice(["Y", "N"])

    if pkg7 == "Y":
        print("Downloading Recuva")
        Recuva = "https://download.ccleaner.com/rcsetup153.exe"
        wget.download(Recuva, "rcsetup153.exe")
        source = path + r"\rcsetup153.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\rcsetup153.exe"])
        breakpoint
    elif pkg7 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def Eraser():
    pkg8 = pyip.inputChoice(["Y", "N"])

    if pkg8 == "Y":
        print("Downloading Recuva")
        Eraser = "https://tenet.dl.sourceforge.net/project/eraser/Eraser%206/6.2/Eraser%206.2.0.2993.exe"
        wget.download(Eraser, "Eraser-206.2.0.2993.exe")
        source = path + r"\Eraser-206.2.0.2993.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\Eraser-206.2.0.2993.exe"])
        breakpoint
    elif pkg8 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit


def WDS():
    pkg9 = pyip.inputChoice(["Y", "N"])

    if pkg9 == "Y":
        print("Downloading WinDirStat")
        WDS = "https://windirstat.net/wds_current_setup.exe"
        wget.download(WDS, "wds_current_setup.exe")
        source = path + r"\wds_current_setup.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\wds_current_setup.exe"])
        breakpoint
    elif pkg9 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit


def Steam():
    pkg11 = pyip.inputChoice(["Y", "N"])

    if pkg11 == "Y":
        print("Downloading Steam")
        Steam = "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe"
        wget.download(Steam, "SteamSetup.exe")
        source = path + r"\SteamSetup.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\SteamSetup.exe"])
        breakpoint
    elif pkg11 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def EGL():
    pkg12 = pyip.inputChoice(["Y", "N"])

    if pkg12 == "Y":
        print("Downloading Epic Games Launcher")
        EGL = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi"
        wget.download(EGL, "EpicGamesLauncherInstaller.msi")
        source = path + r"\EpicGamesLauncherInstaller.msi"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\EpicGamesLauncherInstaller.msi"])
        breakpoint
    elif pkg12 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def FurMark():
    pkg13 = pyip.inputChoice(["Y", "N"])

    if pkg13 == "Y":
        print("Downloading FurMark")
        FurMark = "https://geeks3d.com/dl/get/701"
        wget.download(FurMark, "FurMark_Setup.exe")
        source = path + r"\FurMark_Setup.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\FurMark_Setup.exe"])
        breakpoint
    elif pkg13 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def Chrome():
    pkg14 = pyip.inputChoice(["Y", "N"])

    if pkg14 == "Y":
        print("Downloading Chrome")
        Chrome = "https://www.google.co.za/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#"
        wget.download(Chrome, "ChromeSetup.exe")
        source = path + r"\ChromeSetup.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\ChromeSetup.exe"])
        breakpoint
    elif pkg14 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def Brave():
    pkg15 = pyip.inputChoice(["Y", "N"])

    if pkg15 == "Y":
        print("Downloading Brave")
        Discord = "https://laptop-updates.brave.com/latest/winx64"
        wget.download(Discord, "BraveSetup.exe")
        source = path + r"\BraveSetup.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\BraveSetup.exe"])
        breakpoint
    elif pkg15 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

def BTW():
    pkg16 = pyip.inputChoice(["Y", "N"])

    if pkg16 == "Y":
        print("Downloading Bitwarden")
        BTW = "https://vault.bitwarden.com/download/?app=desktop&platform=windows"
        wget.download(BTW, "Bitwarden-Installer-2022.12.0.exe")
        source = path + r"\Bitwarden-Installer-2022.12.0.exe"
        destination = path + r"\downloaded_files"
        shutil.move(source, destination)
        subprocess.call(["powershell.exe", r".\downloaded_files\Bitwarden-Installer-2022.12.0.exe"])
        breakpoint
    elif pkg16 == "N":
        print("Continuing to next App.")
        breakpoint
    else:
        exit

print("\n \nInstall VLC (Y = yes, N = no)")
VLC()
print("\n Install Nomacs Image Lounge (Y = yes, N = no)")
NIL()
print("\n Install Notepad++ (Y = yes, N = no)")
NPP()
print("\n Install Everything search (Y = yes, N = no)")
ETS()
print("\n Install 7zip (Y = yes, N = no)")
z7zip()
print("\n Install WinRar (Y = yes, N = no)")
WinRAR()
print("\n Install Recuva (Y = yes, N = no)")
Recuva()
print("\n Install Eraser (Y = yes, N = no)")
Eraser()
print("\n Install WinDirStat (Y = yes, N = no)")
WDS()
print("\n Install Steam (Y = yes, N = no)")
Steam()
print("\n Install Epic Games launcher (Y = yes, N = no)")
EGL()
print("\n Install FurMark (Y = yes, N = no)")
FurMark()
print("\n Install Chrome (Y = yes, N = no)")
Chrome()
print("\n Install Brave (Y = yes, N = no)")
Brave()
print("\n Install Bitwarden Password Manager (Y = yes, N = no)")
BTW()