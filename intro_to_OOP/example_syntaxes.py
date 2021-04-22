x  = 11; y = 6;z = 48
sum = x+y+z
#print("bro its so easy! " + str(sum))

example_list = ["fabregas","robin van persie","thiery henry","theo walcot",75,75.001]
for x in example_list:
    print(x)

for x in range(1, len(example_list)):
    if type(example_list[x]) == type("bro its like english!!"):
        print("bro this is super easy! Assembly is so much crap bro!!")
    elif type(example_list[x]) == type(2):
        print("bro this is super easy! Java s**ks so much bro!!")
    else:
        print("bro this is super easy! I am gonna a python guy from now on!!")

easy_dictionary = {"Sadid": 9,"Shihab": 10, "Nafiz": 9, 4: "riham", "holy lord what is this": [1,2,3,4,5,"dddd",0.00]}
for x,y in easy_dictionary.items():
    print(str(x) + " : " + str(y))

#dynamic

print(easy_dictionary[4])

i = 1
while i < 6:
  print(i)
  i += 1


