import pyfiglet
import sys
import random

if len(sys.argv)>=4 and (sys.argv[1] == '-f' or sys.argv[1]=='--font') :
    try:
        fontname=sys.argv[2]
        text=" ".join(sys.argv[3:])
        print(pyfiglet.figlet_format(text, font=fontname))
    except:
        sys.exit("invalid usage")

elif len(sys.argv)==1:
    m=input("enter text: ")
    print(pyfiglet.figlet_format(m))

else:
    sys.exit('invalid usage')

