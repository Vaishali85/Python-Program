def prime(num):

    
    if num <= 0:
        return  False
    
    for i in range(2,num):
        print(f'i -value {i}')
        if num % i==0:
            return False
        
        return True
    
def main():
        n1 = int(input("Enter a number"))
        if prime(n1):
            print(f"number- {n1} is a prime number")
        else:
            print(f"number-{n2} is not a prime number")    
main()
