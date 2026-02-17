import argparse, time, webbrowser
from datetime import datetime, timedelta
parser = argparse.ArgumentParser(
    prog='Locked Out',
    usage='%(prog)s [options]',
    description='A python cli that will remind you to lock in',
    epilog='run "--help" for help')
parser.add_argument('-l','--lockin',type=int, help='Set a reminder to lock in in X minutes')
args = parser.parse_args()
parser.print_help()
lockin_minutes = args.lockin
if args.lockin:
     print("i'll remind you in " + str(lockin_minutes) + " minute(s)")
     currentTime = datetime.now()
     reminderTime = currentTime + timedelta(minutes=lockin_minutes)
     x = True
     while x:
        if datetime.now() >= reminderTime:
            print("time to lock in..")
            webbrowser.open_new_tab('lockin.html')
            break
        time.sleep(30)
        
        
     