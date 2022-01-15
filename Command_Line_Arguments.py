import sys
def main():
    print(f"printing all the arguments ata the command line includeing file name:\n")
    print(f"Printing the total number of command ine arguments including file name:\n")
    print("you can use for loop to traverse through sys.argv")
    for arg in sys.argv:
         print(arg)

    if __name__== "__main__":
        main()
