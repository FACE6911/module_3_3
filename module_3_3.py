def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()

values_list = [2, True, 'old']
values_dict = {'a': 1, 'b': False, 'c': 'new'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)