def is_integer(n):    
  try:  
      n= int(n)  
      print("valid integer :", n)  
  except ValueError as err:  
      print(err)  
is_integer(15)  
is_integer(5.65)  
is_integer('5.65')  
