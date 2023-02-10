import math

# multiline strings can be created using triple quotes
a ='''string1
string2'''
print(a)
print("length :",len(a))


a = '''a
b'
c
d'''

print(a)
print("length :",len(a))


a="\ab"
print(a)
print("length :",len(a))

a = "Seema\'s pen"
print(a)
print("length :",len(a))


p = q = 5
print(id(p))
print(id(q))
print(id(5))

print("\nFloor and divison operators")
print(100/10)
print(100//32)
print(6.5//2)
print(4**3)
print(6%2.5)
print(6%5)

print("Comparison operators")
print([1,2,3]<[2,4,6])
print([1,2,3]==[2,4,6])
print([2.0,3.0]==[2,3])
print([1,2,3]<[1,2])
print([1,2]>[3,4,5])

print(not(5))
print(not(5<2))
print("arithmetic operators")
print(7*8/5//2)
print(7*((8/5)//2))
print(87//5)
print(int(85//5.0))
a,b,c = 1,2,3
print(a//b**c+a-c*a)
print(math.ceil(1.03)+math.floor(1.03))




for a in [1,4,5]:
    print(a) #Takes values from the list
    print("a")

for a in range(1,9):
    print(a) 


for ch in 'calm':
    print(ch)


print(2+5) #Adds two integers 
print("2"+"8") 

print(3*"go") 
print("go"*3)
print("7"*4)



print(ord('A')) #Prints ascii value
print(chr(65))  #Prints character of given ascii value

word="amazing"
print(word[0:7]) # 7 will not be included 
print(word[0:3])
print(word[7:3])
print(word[3:7])
print(word[:7]) 
print(word[3:]) 
print(word[:3]+word[3:]) 
print(word[:-7])
print(word[1:6:2]) #Skip desired number of characters 
print(word[::-2]) 
w=word[5]
print(w) 
print(word[8:10]) #Not an error but empty string will be printed


#len() function 
print(len("Python"))
print(len("Python Programming"))
str="abcdabbacdabbbaca"
#count() funcion
print(str.count("ab"))
print(str.count('ab',4,8)) 
print(str.count('ab',4))
print("_____")


s="I love doing python" 
print(s.find("python")) # Returns lowest index
print(s.index("python")) 
print("_____") 
print("Python String methods: ")
str1="Python1234" 
print(str1.isalnum())  
str2="Python-1234"
print(str2.isalnum())  # Contains special symbol 
print(str1.isdigit())
print(str1.isalpha())
s4="abcde" 
ss="ABcd" 
str5=" " 
print(s4.islower()) 
print(ss.isupper()) 
print(str1.isspace())
print(str5.isspace()) 
print(ss.strip()) 
print(ss.lstrip()) 
print(str.rstrip()) 


print("abcd".startswith("ab"))
print("abcd".endswith("ab"))
print(s.title()) 
print(s.istitle()) 
print("*".join("Hello"))
strings=("trial","Hello","new")
print("*".join(strings))
string="This is old"
x=string.replace("old","new")
print(x)



s1="I LOVE PYTHON"
print(s1.split()) 
print(s1.split(" "))
print(s1.split('o'))
print("A#B#C#D#E".split("#",2))
print("ComputerScience".split("er",2))
s2="Application"
print(s2.replace('a','A'))  
s3="Abcabcbacdab"
print(s3.replace('a','A',2)) 