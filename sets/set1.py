# the way we are entering data, we are not sure that we will get the output in same order
#sets are unordered so index se access nahi kr sakte
#only unique elements duplicate can not be stored
#{2221,2213}
#sets are mutable
my_Set={1,2,3,4,4,4,5}
print(my_Set)

my_Set.add(6)
print(my_Set)

my_Set.add(6.1)
print(my_Set)

my_Set.add("vivek")
print(my_Set)

my_set2={1,"vivek",23,"mango"}
my_Set.update(my_set2)
print(my_Set)
#the remove throw error if the value is not present and discard will not throw
my_Set.remove(23)
print(my_Set)

my_Set.discard(4)
print(my_Set)

print(my_Set|my_set2)

print(my_Set & my_set2)

print(my_Set)

print(my_Set - my_set2)

print(my_Set^my_set2)


fac=frozenset(my_Set)
print(fac)
# fac.add(90)
# print(my_Set)