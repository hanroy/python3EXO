print('exo1')

mytxt = "to be or not to be"
for i in range(0,len(mytxt)):
    print(mytxt[i])
    if mytxt[i] == "e":
        print("I found an E")

print('exo2')

mytxt2 = "to be or not to be"
nbreoccu = mytxt2.count('e')
print(nbreoccu)

print('exo3')
lst = "ilovepeace"
print(lst[0],"*",lst[1],"*",lst[2],"*",lst[3],"*",lst[4],"*",lst[5],"*",lst[6],"*",lst[7],"*",lst[8],"*",lst[9])


lst2 = "anothermethdtotry"
print(' * '.join(lst2))

print('exo4')

var = "versi versa"
print(var[::-1])

print('exo5')

var2 = input("Please enter something: ")
if var2[::-1] != var2:
    print(var2[::-1])
else:
    print("palindrome")

