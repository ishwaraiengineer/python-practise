      #what is set?
#python set is an unordered collection of multiple items having diff
#set are nutable, unidexed and do not contain duplicate

#create set
s = {1,2,3,4}
s.add(5)
s.update([5,6])
s.add("python")
s.add("developer")
print(s)

b = set(["hello",1,3,4,5,"world"])
b.add("new")
print(b) 

#creating set used of tuple
c=("hello","python","developer")
t=set(c)
print(t)
