def multiply(*args):
    z = 1
    count = 0
    for num in args:
        z *= num
        count += 1
    print(f"Number of parameters passed = {count} and multiplication = {z}")
    
def main():
    multiply(1,2,3,4)
    
if __name__=='__main__':
    main()
