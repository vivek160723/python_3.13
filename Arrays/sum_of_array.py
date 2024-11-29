from functools import reduce
import array

my_arr = array.array("i", [10, 20, 30, 40, 30, 40, 30])
ans = reduce(lambda x, y: x + y, my_arr)

print(ans)