input_list = ['10', '50', '77', '33']
input_str = "atme mysuru"

output_list = [character for character in input_str.split()]
output_str = ''.join(input_list)

print(input_list)
print(output_str)

print(input_str)
print(output_list)

output_list2 = [character for character in input_str]
print(output_list2)