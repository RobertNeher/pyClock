import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Modify data in repository',
                                    usage=f"{sys.argv[0]} [options]", allow_abbrev=False)
    parser.add_argument('-p', '--updatePeriod', nargs='?', help='update periosd in seconds (default = 1 sec.)',default="1")
    parser.add_argument('-o', '--options', nargs='?', help='c: random colors,\nd: show date field,\nf: show watch face,\ns: show seconds hand', default='cdfs')

    args = parser.parse_args()

    randomColor = False
    dateField = False
    watchFace = False
    secondsHand = False

    for c in args.options.lower().strip():
        if c == "c":
            randomColor = True
        elif c == "f":
            watchFace = True
        elif c == "d":
            dateField = True
        elif c == "s":
            secondsHand = True
        else:
            parser.print_help()
            sys.exit()
    print(randomColor, watchFace, dateField, secondsHand)

    if args.updatePeriod:
        period = int(args.updatePeriod.strip())
        print(period)

    # if args.options is None or any((c in options) for c in args.options.strip()):
    #     parser.print_usage()
    # else:
        randomColor = "c" in args.options.strip()
        watchFace = "f" in args.options.strip()
        dateField = "d" in args.options.strip()
        secondsHand = "s" in args.options.strip()

if __name__ == "__main__":
    main()
