
from collections import OrderedDict
 
dict = {'raj':'10','raju':'9','sanju':'15','yash':'2','suraj':'32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
