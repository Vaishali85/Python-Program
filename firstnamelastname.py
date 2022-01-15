def greet(fname,lname):
    print(f"Hello {fname} {lname}")
    
def main():
           greet(fname="anand", lname='deshpande')
           greet(lname="deshpande",fname='anand')
if __name__=='__main__':
    main()
