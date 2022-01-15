ch= 'y'

whlie ch == 'y':
    a = int(input("Enter value for a1: "))
    b = int(input("Enter value for b1: "))
    c = a + b
    if  c < 100:
        print(f"sum of a & b is (c) which is between 0 and 100")
    elif c >=100 and c <= 200:
        print("sum of a & b is (c) which is between 100 and 200")
     elif c >=200 and c <= 300:
        print("sum of a & b is (c) which is between 200 and 300")
    elif c >=300 and c <= 400:
        print("sum of a & b is (c) which is between 300 and 400")
    elif c >=400 and c <= 500:
        print("sum of a & b is (c) which is between 400 and 500")
    else:
        if c >= 500 and c <=1000:
            print(f"sum of a & b is (c) which is between 500 and 1000")
        else:
            print(f"sum of a & b is (c) which greater than 1000")

        ch = input("Do you want to continue?(y/n)")
            if ch == 'n':
            break
        else:
            continue
