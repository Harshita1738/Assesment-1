def process_numbers(nums):
  even_numbers=list(filter(lambda x:x%2==0,nums))
  list1=list(map(lambda x:x**2,even_numbers))
  print(list1)
  dict1={x:x**2 for x in even_numbers}
  print(dict1)
  tuple1=(list1,dict1)
  print(tuple1)