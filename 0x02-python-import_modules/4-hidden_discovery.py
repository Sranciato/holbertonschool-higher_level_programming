#!/usr/bin/python3
def main():
    import hidden_4
    for objname in dir(hidden_4):
        if objname[:2] == "__":
            continue
        print(objname)

if __name__ == "__main__":
    main()
