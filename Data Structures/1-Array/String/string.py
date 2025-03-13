letter = "a"
print(letter)

apostroph = 'a'
quotation_mark = "a"

multi_line = """A string 
what consist of multiple
lines """
print(multi_line)

str = "That is a string1"
print(str[0])
print(str[-2])
print(str[3:6])

s = "That's the second string"

s1 = 'B' + s[1:]
print(s1)

# del s
# print(s)

s2 = "Third"

s3 = s1.replace("Second", s2)
print(s3)

print(len(s3))

print(s3.upper())
print(s3.lower())

space = "     space      "

print(space)
print(space.strip())

m1 = "Hello"
m2 = "World"
m3 = m1 + m2
print(m3)

print(m3 * 4)

name = "alice"
print(f"Name: {name}")

python = "Python"

print("t" in python)
print("a" in python)