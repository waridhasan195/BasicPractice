
import itertools

lst = [1, 2, 3, 4, 5, 5633]
sum_lst = itertools.accumulate(lst)
print(list(sum_lst))


lst2 = ['A', 'B', 'C', 'D', 'D']
chain_list = itertools.chain(lst, lst2)
print(list(chain_list))


names = ['Tamim', 'Sakib', 'Joe', 'Mushfiq', 'Arafat', 'Liton']
show = [1, 0, 1, 0, 1, 1]
compressed_list = itertools.compress(names, show)
print(list(compressed_list))

