def greet(**person):
    print('hello',person['firstname'], person['lastname'], person['age'])
    
def main():
    greet(firstname= 'steve', lastname='jobs',age='45')
    greet(lastname= 'jobs', firstname='steve',age='55')
    greet(firstname= 'Bill', lastname='Gates',age='55', sal=30000)
if __name__=='__main__':
    main()
