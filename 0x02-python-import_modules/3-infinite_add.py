#!/usr/bin/python3
def main():
    from sys import argv
    sum = 0
    for count in range(1, len(argv)):
        sum += int(argv[count])
    print("{:d}".format(sum))

if __name__ == "__main__":
    main()
