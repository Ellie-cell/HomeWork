def calculate_structure_sum(data) :
    calculate = 0
    if isinstance(data, int):
        calculate +=data
    if isinstance(data, str):
        calculate += len(data)
    if isinstance(data, (list, tuple, set)):
        for items in data:
            calculate += calculate_structure_sum(items)
    if isinstance( data, dict):
        for key in data.items() :
            calculate += calculate_structure_sum(key)
        #for value in data.items():
            #calculate += calculate_structure_sum(value)
    return calculate

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
