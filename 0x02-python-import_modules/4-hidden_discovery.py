#!/usr/bin/python3
import builtins
import hidden_4
names = dir(hidden_4)

print_names = []
for name in names:
    if not name.startswith('__'):
        print_names.append(name)
print_names.sort()
for names in print_names:
    print("{}".format(names))
