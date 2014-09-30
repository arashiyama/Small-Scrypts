#!/usr/bin/python

import argparse, signal, sys

def signal_handler(signal, frame):
        print('Lbh cerffrq Pgey-P!')
        sys.exit(0)
        
def rot13(s):
    result = ""

    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)

        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result
    
def main(me,argv):
    parser=argparse.ArgumentParser(description='A rot13 parser with benefits')
    parser.add_argument('Phrase',nargs='*',default=False,help='optionally provide phrase on command line')
    parser.add_argument('-i','--input',help="name of input file (defaults to STDIN)", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args=parser.parse_args()
    
    if args.Phrase:
        print rot13(" ".join(args.Phrase))
    else:
        print "Enter phrase, press CTRL-D when done"
        for l in args.input:
            print rot13(l.strip())
            
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[0],sys.argv[1:])    