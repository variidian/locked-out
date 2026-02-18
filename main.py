import argparse, time, webbrowser
from datetime import datetime, timedelta
reminderTime = datetime.now() + timedelta(minutes=99999) 
def terminalArt(artTxt):
    with open(artTxt, 'r', encoding="utf-8") as file: 
        filecontent = file.read()
        print(filecontent)
        return artTxt
lockinArt = 'lockin.txt'
terminalArt('cat.txt')
parser = argparse.ArgumentParser(
    prog='Locked Out',
    usage='%(prog)s [options]',
    description= 'A python cli that will remind you to lock in',
    epilog='run "--help" for help')
parser.add_argument('-l','--lockin',type=int, help='Set a reminder to lock in in X minutes')
parser.add_argument('-a','--art',type=str, help='Change ASCII art to [bat,bird,cat,dolphin,whale,shark]')
args = parser.parse_args()
parser.print_help()
lockin_minutes = args.lockin
asciiArt = args.art
if args.lockin:
     print("i'll remind you in " + str(lockin_minutes) + " minute(s)")
     reminderTime = datetime.now() + timedelta(minutes=lockin_minutes)
x = True
while x:
    if datetime.now() >= reminderTime:
        with open(lockinArt, 'r', encoding="utf-8") as file:
            content = file.read()
            print(content)
        webbrowser.open_new_tab('lockin.html')
        break
    time.sleep(30)
if args.art:
    
