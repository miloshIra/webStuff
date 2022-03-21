main_dict={}
def insert_item(item):
   if item in main_dict:
       main_dict[item] += 1
   else:
       main_dict[item] = 1
#Driver code
insert_item('Key1')
insert_item('Key2')
insert_item('Key2')
insert_item('Key3')
insert_item('Key1')
print(main_dict)
print (len(main_dict))
