#dictionary  mey 2 cheeze hoti hai: pehla hota hai key, dusra hota hai key se juda hua element
data = {1:'Yash',2:'YoYash',4:'YoYoyash'}
print(data)

#agar index use krke element print karana ho to:
print(data[2])

#ek aur tarika hai data nikaalne ka index ke through
print(data.get(4))
print(data.get(3))#kyuki 3 naam ki koi key nahi hai isiliye none print hoga

#ab maan lo aapko none print nahi karana hai agar koi key ko element assigned nahi hai to
#to uske liye kya krege
z = data.get(3,'Not Found')
print(z)

#Lists ko use karke dictionary banana ho to:
keys = ['Yash', 'Yash_Two', "Yash_Three"]
values = ['Apple', 'Pine Apple', 'Strawberry']
data_new = dict(zip(keys,values))#dict function dictionary mey convert karne ke liye use hoga 
print(data_new)

#agar upar bani dictionary mey koi element add karna ho to
data_new['Yash_Four'] = 'Lichi'
print(data_new)
#Ab maan lo upar bani dictionary mey se koi element replace karna ho to
del data_new['Yash']
print(data_new)

#Ab ek aisi dictionary banate hai jisme list aur dictionary saath mey hoge
plyr = {'WK':'Dhoni', 'Open':'Gayle', 'Bowler':['Bravo', 'Malinga'], 'Allrounder':{'Bat':'Pollard', 'Ball':'Rashid'}}
print(plyr)
