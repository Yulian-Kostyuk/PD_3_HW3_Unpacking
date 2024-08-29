print('Функция с параметрами по умолчанию:')
def print_params(a = 4, b = 'string', c = True):
    print(a, b, c)
print_params(1, True, '')
print_params(12, True)
print_params(13, c = 'code')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print('Распаковка параметров:')
values_list = [7, 'text', False]
values_dict = {'a': 11, 'b': True, 'c': 'Number'}
print_params(*values_list)
print_params(**values_dict)

print('Распаковка + отдельные параметры:')
values_list_2 = [True, 'Words']
print_params(*values_list_2, 42)