from itertools import count


num=1234
rev=""
while num>0:
    last_digit = num % 10
    rev = rev + str(last_digit)
    num = num // 10
print(rev)


x="PYThOn"
u=0
l=0
for i in x:
    if i.isupper():
        u+=1
    if i.islower():
        l+=1
print(u)
print(l)


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
for i in a:
    for j in b:
        if i==j:
         print(i ,end=" ")


lst=[1, 2, 2, 3, 1, 4, 2]
for i in range(0,9):
    count=0
    print("frequency of ",i,"is",lst.count(i))


lst=[8, 2, 5, 1, 9]
small=lst[0]
for i in lst:
    if i<small:
        small=i
second=lst[0]
for i in lst:
    if i>small and i<second:
        second=i
print(second)

lst=[1, 2, 2, 3, 4, 4, 5]
new=[]
for i in lst:
    if i not in new:                    
        new.append(i)
print(new)

a=int(input("enter a number:"))
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
else:
    
    print("prime")

n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

s="education"
vowels="aeiouAEIOU"
new=" "
for i in s:
    if i in vowels:
        new += i
print(new)


lst=[1, 2, 3, 4, 5, 6]
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)
print("Even:",even,"count:",len(even))
print("Odd:",odd,"count:",len(odd))
 

num="5482"
total=0
for i in num:
    total+=int(i)
    

    
print("sum",total)

a="58392"
large=a[0]

for i in a:
   if large<i:
      large=i
print("large",large)

a="anisha"
vowels="aeiou"
count=""
for i in a:
    if i in vowels:
        count+=i
print("count",len(count))

name="swiggy"

rev=""
for i in name:
    rev=i+rev
print(rev)
if name==rev:
    print("Palindrome")
else:
    print("Not palindrome")


txt="python is a snake"
new=txt.split()
print(len(new))

txt="banana"
print(txt.count("a"))

txt="hello world python"
print(txt.replace(" ",""))


num="58392"
print(min(num))


num="153"
total=0
digit=0
for i in num:
    total+=int(i)**3
print(total)
if total==int(num):
    print("Amrstrong")
else:
    print("not Armstorng")


num="248531"
even=0
for i in  num:
    if int(i)%2==0:
        even+=int(i)
print("Even",even)

num="234"
multi=1
for i in num:
    multi*=int(i)
print("Multi",multi)


name="PyThOn"
upper=0
lower=0
for i in name:
    if i == i.upper():
        upper+=1
    if i == i.lower():
        lower+=1
print(upper)
print(lower)

name="Anisha123@"
alpha=0
num=0
special=0
for i in name:
    if i.isalpha():
       alpha+=1
    elif i.isnumeric():
       num+=1
    else:
        special+=1
print("Alpha",alpha)
print("Number",num)
print("Special",special)

name="anisha"
vowels="aeiou"
vow=0
constants=0
for i in name:
    if i in vowels:
        vow+=1
    else:
        constants+=1
print("Vowels",vow)
print("consonants",constants)

name="anisha"
vow="aeiou"
new=""
for i in name:
    if i not in vow:
        new+=i
print(new)

a="aabbcdde"
for i in a:
    a.count(i)
    if a.count(i)==1:
        print(i)
        break
    
    
txt="programming"
seen=""
for i in txt:
        
    if txt.count(i)>1 and i not in seen:
         
        print(i)
        seen+=i

txt="banana"
seen=""
for i in txt:
    if i not in seen:
        print(i,txt.count(i))
        seen+=i

txt="banana"
seen=""
max_count=0
max_char=""

for i in txt:
    if i not in seen:
        count=txt.count(i)
        if count>max_count:
            max_count=count
            max_char=i
        seen+=i
print("max",max_char , max_count)

a="listen"
b="silent"


if sorted(a)==sorted(b):
    print("its anagrams")
else:
    print("not anagrams")
 
      
       
        
        
    

              
        
       
      



        
                
           
               

        
            
            





    


