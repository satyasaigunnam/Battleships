
def maxlist(list1):
    max = list1[0]
    for i in  list1:
          if i > max:
            max = i
        
    return max
list1=[10,20,30,40]        
print(maxlist(list1) ,"higest no")   