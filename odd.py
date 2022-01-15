def odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
def main():
    n1 = int(input("ENter a number: "))
    if odd(n1):
        print(f"number - {n1} is an odd number")
    else:
        print(f"number - {n1} is not odd number")
main()
