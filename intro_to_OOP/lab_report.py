

input_junk = "11$6$48#9$4$76#9$4$79"

sparsed_junk_string  = input_junk.split("#")
print(sparsed_junk_string)

sparsed_data_packet_string = []

for i in range(len(sparsed_junk_string)):
    to_be_split = "to be splited : " + sparsed_junk_string[i]
    print(to_be_split)
    temp_list = sparsed_junk_string[i].split("$")
    print("temp list for loop " + str(i) + " : ")
    print(temp_list)


    for i in range(len(temp_list)):
        temp_list[i] = int(temp_list[i])

    sparsed_data_packet_string.append(tuple(temp_list))

#print(sparsed_data_packet_string)
#print(input_junk)



