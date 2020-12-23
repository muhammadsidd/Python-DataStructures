string = input("Enter a noun ")
string_1= input("this is it ")
string_3= input ("keyboard not found press f1 ")

print("this is just a test function " + string + "that does all the cool stuff " + " in python")

friends =["Kevin", "talha"]
numbers = [1,2,3,4,5,6]

##friends.extend(numbers)
print(friends)

friends.append("tobby")
friends.insert(2, "bitch")
friends.remove("Kevin")
#friends.clear() would reset the list brother 
#friends.pop() would pop the last element of the list
#in ascending order
friends2 = friends.copy()
friends.sort()
 
print(friends)
print("this is frinds 2 ")
print(friends2)
#friends.count("x") would count how many x in the list
#to find if something is in the list 
print(friends.index("talha"))

def say_hi(name, age):
    print("hello brother " + name +" you are ", age)
def cube(num):
    return num*num*num

def power(base,pow):
    res = 1
    for i in range(1, pow +1):
        print(i)
        res = res * base
    return res

def trans(phrase):
    tran=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            tran = tran +"g"
        else:
            tran= tran+letter
    return tran

#isupper() returns true or false depending on if the letter is upper case or not

say_hi("mike",43)
print(cube(3))

user = int(input("enter your number "))
if user == 2 or user ==3:
    user=user+1
    print(user)
else:
    print("not the number ")

len(friends) #length of friends array

basen = int(input("enter base "))
pw = int(input("enter power "))

result = power(basen,pw)

print(result)


print(trans(input("enter something ")))

try: 
    nu = int(input("enter a num: "))
    print(nu)
except:
    print("invalid input")
