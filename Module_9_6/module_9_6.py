def all_variants(text):
    _i = 1
    while _i != len(text) + 1:
        for elem in range(len(text) - (_i - 1)):
            yield text[elem:(elem + _i)]
        _i += 1


a = all_variants("abc")
for i in a:
    print(i)
print()
a = all_variants("abcd")
for i in a:
    print(i)
print()
a = all_variants("12345")
for i in a:
    print(i)
