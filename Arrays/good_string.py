S = 'wdfsdfgsdgsgfdg'
vowels = ['a', 'e', 'i', 'o', 'u']
mx = 0
count = 0

for s in S:
    if s in vowels:
        count += 1
    else:
        count = 0
    if count > mx:
        mx = count

print(mx)
