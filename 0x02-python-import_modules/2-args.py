#!/usr/bin/python3
def main():
    import sys
    argv = sys.argv
    if len(argv) == 1:
        print("0 arguments.")
        return 0
    elif len(argv) == 2:
        print("1 argument:")
    elif len(argv) > 2:
        print("{:d} arguments:".format(len(argv) - 1))
    for args in range(1, len(argv)):
        print("{:d}: {}".format(args, argv[args]))

if __name__ == "__main__":
    main()
