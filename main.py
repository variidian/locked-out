import argparse, time, webbrowser, shelve, winsound, sys
from datetime import datetime, timedelta


def terminalArt(artTxt):
    with open(artTxt, 'r', encoding="utf-8") as file: 
        filecontent = file.read()
        print(filecontent)
        return filecontent
    
lockinArt = 'lockin.txt'
with shelve.open('mydata') as db:
    if 'savedAsciiArt' in db:
        art = db['savedAsciiArt']
    else:
        db['savedAsciiArt'] = 'bat.txt'
        art = db['savedAsciiArt']
    if 'savedReminderTime' in db:
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
if len(sys.argv) == 1:
    parser.print_help()
lockin_minutes = args.lockin
asciiArt = args.art
newnote = args.note

if args.lockin:
     print("i'll remind you in " + str(lockin_minutes) + " minute(s)")
     reminderTime = datetime.now() + timedelta(minutes=lockin_minutes)
     with shelve.open('mydata') as db:
         db['savedReminderTime'] = reminderTime

if args.note:
    with shelve.open('mydata') as db:
        if args.note == 'show_note':
            if 'savedNote' in db:
                print( "note: "+ db['savedNote'])
            else:
                print("No note saved yet :[")
        else:
            db['savedNote'] = args.note
            print("Note saved!")

if args.art:
    art = str(asciiArt) + '.txt'
    with shelve.open('mydata') as db:
        db['savedAsciiArt'] = art
terminalArt(art)
with shelve.open('mydata') as db:
    while 'savedReminderTime' in db:
        if datetime.now() >= reminderTime:
            with open(lockinArt, 'r', encoding="utf-8") as file:
                content = file.read()
                print(content)
            winsound.Beep(1000, 2000)
            webbrowser.open_new_tab('lockin.html')
            with shelve.open('mydata') as db:
                del db['savedReminderTime'] 
            break
        time.sleep(30)