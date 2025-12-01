def sum(n):
    if not n:
        return 0
    else:
        return n[0] + sum(n[1:])

my_list = [1, 2, 3, 11, 45,13]
print(sum(my_list))