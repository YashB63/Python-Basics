nos = [25, 23, 21, 67, 74, 15]
print(nos)

print(nos[1])

#2 ke baad saare print hoge
print(nos[2:])

#negative index bhi use kar sakte hai.
print(nos[-2])

#string ki list bhi ban sakti hai
words = ['apple', 'ball', 'cat']
print(words)

#numbers aur string ko combine karke bhi bana skte hai
check = [63, 'Apple', 36]
print(check)

#lists ki list bana dete hai
join = [nos, words]
print(join)

#numbers ki list mey agar koi element add karna ho to:
nos.append(50)
print(nos)#yaha element list ke end mey insert hoga

#agar kisi specific index mey daalna ho too simply:
nos.insert(3, 23)
print(nos)

#koi specific number udana ho to use karege 
nos.remove(74)
print(nos)

#ab koi specific index ka number udana ho to
nos.pop(1)
print(nos)

#aakhri element udana ho to simply use karege pop bina index specify kiye
nos.pop()
print(nos)

#multiple values udani ho to
# del use karke index specify kar do
del nos[2:]
print(nos)

#agar elements add karna ho to:
#extends use krke jo bhi elements add krne ho list bana kr bracket mey likh do
nos.extend([25,26,38,39])
print(nos)

#list ki minimum and maximum values nikaalni ho to:
x = min(nos)
y = max(nos)
print(x)
print(y)

#agar list ke elements ka sum nikaalna ho to:
print(sum(nos))

#ab maanlo aapko list ko ascending order mey sort karna ho to vo bhi kar sakte hai.
nos.sort()
print(nos)