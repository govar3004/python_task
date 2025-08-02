#1
for a in range(1,11):
    if a == 5:
        break
    print(a)
    
#4
for b in range(1,11):
    if b == 2:
        continue
    print(b)
    
#5
for c in range(1,11):
     if c % 2==0:
         print(c)

#
word = "ocean academy"
for letter in "aeiou":
    word = word.replace(letter, " ")
print(word)

