'''Didderence between list and tupple is that list is mutable ...it means we can apply many methods on it but tupple is
 immutatble...means we can't apply mthods on tupple like lists...tupple only contains contant values..where list can
 contain all types of datas'''

#before checking the code i want to inform u that my code is not working when i'm using functions but suddenly
# what happended i don;t know ????????,,,,,
#but good news is without using function the code ran well ...
# becuase of unintended indent i couldn't fix it!!!!!!!!!!!!!!!!!!!!
#I couldn't define the error and something went wrong when the parameters are declared
# like i have done in the first line and line 18 is getting unused when I am declaring the parameters...



def func1(data_junk):
  split_junk = data_junk.split("#")
  print(split_junk)
  final_data = []
  for x in range(len(split_junk)):
    split_data = []
    split_d1 = split_junk[x].split("$")

    for y in range(len(split_d1)):
      split_data.append(int(split_d1[y]))
    tupple_data = tuple(split_data)
    final_data.append(tupple_data)

  print(final_data)


corrupted_data=input("junk")
func1(corrupted_data)

'''
1001111000111<3A3F>1001111000111<3A3F>



'''