first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = ((len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

second_result = (len(a) == len(b) for a in first for b in second if first.index(a) == second.index(b))

print(list(first_result))
print(list(second_result))
