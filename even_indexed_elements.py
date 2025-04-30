def even_indexed_elements(lst):
    return [(element, index) for index, element in enumerate(lst) if index % 2 == 0]
my_list = ['a', 'b', 'c', 'd', 'e']
result = even_indexed_elements(my_list)
print(result)