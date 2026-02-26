import argparse, time, webbrowser, shelve, sys, os, autostarter
from datetime import datetime, timedelta
from pathlib import Path
from platformdirs import user_data_dir
from playsound3 import playsound
data_dir = user_data_dir('lockedout', 'variidian') #data directory
os.makedirs(data_dir, exist_ok=True) #make directory
mydata = os.path.join(data_dir, "my_data.db") #path to file for shelf use

script_dir = Path(__file__).parent #get parent directory of current script
def main(): #for pyproject.toml so running 'lockedout' works
     autostarter.add(
         'cmd /k lockedout',
    identifier="lockedout"
    )

def terminalArt(artTxt): #function to print contents of the ascii art files
    with open(artTxt, 'r', encoding="utf-8") as file: 
        filecontent = file.read()
        print(filecontent)
        return filecontent
    
lockinArt = script_dir / 'lockin.txt' 

with shelve.open(mydata) as db: #collect previously set ascii art / set to bat art if none
    if 'savedAsciiArt' in db:
        art = db['savedAsciiArt']
    else:
        db['savedAsciiArt'] = script_dir / 'bat.txt'
        art = db['savedAsciiArt']
    if 'savedReminderTime' in db: #collect previously set reminder time so it remembers to remind the user when the time comes
        reminderTime = db['savedReminderTime']
    

parser = argparse.ArgumentParser(
    prog='Locked Out',
    usage='%(prog)s [options] [-h]',
    description= 'A python cli that will remind you to lock in',
    epilog='run "--help" for help')
parser.add_argument('-l','--lockin',type=int, help='Set a reminder to lock in in X minutes')
parser.add_argument('-n','--note', type=str, nargs='?', const='show_note',help='quick notes. updates only to the last note.')
parser.add_argument('-a','--art',type=str, help='Change ASCII art to [bat,bird,cat,dolphin,whale,shark]')
args = parser.parse_args()

if len(sys.argv) == 1: #if no arguments are parsed then print the help info
    parser.print_help()

lockin_minutes = args.lockin
asciiArt = args.art
newnote = args.note

if args.lockin: 
     print("i'll remind you in " + str(lockin_minutes) + " minute(s)")
     reminderTime = datetime.now() + timedelta(minutes=lockin_minutes)
     with shelve.open(mydata) as db:
         db['savedReminderTime'] = reminderTime

if args.note:
    with shelve.open(mydata) as db:
        if args.note == 'show_note':
            if 'savedNote' in db:
                print( "note: "+ db['savedNote'])
            else:
                print("No note saved yet :[")
        else:
            db['savedNote'] = args.note
            print("Note saved!")

if args.art: 
    art = script_dir / f"{asciiArt}.txt"
    with shelve.open(mydata) as db:
        db['savedAsciiArt'] = art
terminalArt(Path(script_dir) / Path(art).name) #path turns a string into actual path. .name gets file name and removes folder nesting

with shelve.open(mydata) as db: #check if its time to remind the user as long as theres a reminder set, on a loop interval of 30 sec
    while 'savedReminderTime' in db:
        if datetime.now() >= reminderTime:
            with open(lockinArt, 'r', encoding="utf-8") as file:
                content = file.read()
                print(content)
            webbrowser.open_new_tab(Path(script_dir)/'lockin.html')
            playsound(Path(script_dir) / "alarm.mp3")
            with shelve.open(mydata) as db:
                del db['savedReminderTime'] 
            break
        time.sleep(30)