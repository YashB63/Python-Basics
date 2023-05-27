#Immutability: string ke letters ko change, letters ke index ko use karke nahi kar sakte hai.

#maan lo name hai uske ek letter ko change karna hai

name = "fox"
#name[0] = 'b'    ye error de dega 

#to uske liye hum slicing ka use kar sakte hai

last_letters = name[1:]

#Ab karege string Concatenation
x = 'b' + last_letters 
print(x)

x = 'Hi brother!'

# y = x + " Let's play cricket"
# print(y)

#baar baar x mey hi new cheeze add krke 
#x mey sb kuch reassign karwa ke nikal skte hai
x = x + " Let's play cricket"
print(x)

#Multiplication in letters

letter = 'z'
print(letter*10)#10 baar z print ho jaayega

#ab 2 cases hai 
# lets say aapko koi number print karwana hai eg: 63

print(6+3)#ye 9 output dega
#whereas
print('6'+'3')#ye 63 output dega kyuki humne string bana diya hai.

x = 'Hello World!'
print(x.upper())#ye string ko uppercase mey convert kar dega

print(x.lower())#ye complete string ko lower case mey convert kar dega

print(x.split())#ye kya krega ki bhai string ke tukde karke ek list bana dega comprising og each word as seperate strings

print(x.split('o'))#jaha jaha O hai waha se o uda dega and baaki splitted words ki list bana dega

s='hello'
print(s[1])