s = {"That","is","a","set"}

list_to_set = set(["That","was","a","list","but","converted","in","a","set"])

a = {"serhat","serhat","serhat","serhat"}
print(a) # just one time serhat

mixed = {"Serhat",5,19.245,True}

fs = frozenset(["That","is","a","frozenset","can","not","changed"])
#fs.add("add an element") # can not

set1 = {"Serhat", 5}
set1.add("Karaarslan")

numbers = {1,6,4,89,34,3}
letters = {"s","j","k","l"}

numbers_and_letters = numbers.union(letters)
print(numbers_and_letters)

prime_numbers = {2,3,5,7,11}
even_numbers = {2,4,6,8,10}
common_numbers = prime_numbers.intersection(even_numbers)
print(common_numbers)

different_numbers = prime_numbers.difference(even_numbers)
print(different_numbers)

print(2 in prime_numbers) #True
print(4 not in prime_numbers) #True
print(prime_numbers == even_numbers) #False
print(prime_numbers < even_numbers) #False

for i in prime_numbers:
    print(i)