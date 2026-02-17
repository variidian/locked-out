import argparse
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
     print("test")