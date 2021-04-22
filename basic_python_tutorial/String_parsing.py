
arduino_data = "14$15$3$19$14$7$19"

sparsed_data = arduino_data.split("$")
print(sparsed_data)

sparsed_data_int = []

for x in range(len(sparsed_data)):
    sparsed_data_int.append(int(sparsed_data[x]))

print(sparsed_data_int)

for x in sparsed_data_int:
    print(x)
    print(type(x))
