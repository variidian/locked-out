import argparse, time, webbrowser
from datetime import datetime, timedelta
reminderTime = datetime.now() + timedelta(minutes=99999) 
def terminalArt(artTxt):
    with open(artTxt, 'r', encoding="utf-8") as file: 
        filecontent = file.read()
        print(filecontent)
        return artTxt
lockinArt = 'lockin.txt'
parser = argparse.ArgumentParser(
    prog='Locked Out',
    usage='%(prog)s [options]',
    description= terminalArt('cat.txt') + ' A python cli that will remind you to lock in',
    epilog='run "--help" for help')
parser.add_argument('-l','--lockin',type=int, help='Set a reminder to lock in in X minutes')
args = parser.parse_args()
parser.print_help()
lockin_minutes = args.lockin
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
