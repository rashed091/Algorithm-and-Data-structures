greeting = "Hello world! "
greeting[4]
print('world' in greeting)
len(greeting)
print(greeting.find('lo'))
print(greeting.replace('llo', 'y'))
print(greeting.startswith('Hell'))
print(greeting.isalpha())
greeting.lower()  # => "hello world! "
greeting.title()  # => "Hello World! "
greeting.upper()  # => "HELLO WORLD! "
greeting.strip()  # => "Hello world!"
greeting.strip('dH !')
print('ham cheese bacon'.split())
# => "ello worl"
slayer = ["Buffy", "Anne", "Summers"]

print(" ".join(slayer))


slayers = "Buffy\nFaith"

print(slayers.splitlines())


L = [1, 2, 3]
# print(*L)
