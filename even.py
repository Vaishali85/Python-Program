def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def main():
    n1 = int(input("Enter a number: "))
    if even(n1):
        print(f"number - {n1} is an even number")
    else:
        print(f"number - {n1} is not even number")
main()
