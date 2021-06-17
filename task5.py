#3
country = ["england","australia","india","usa"]
capital = ["london","canbera","delhi","washinton d.c"]
data = dict(zip(country,capital))
print(data)
#2
csk= {"caption":"dhoni","batsman":"raina","bowler":"jadeja"}
del csk["caption"]
print(csk)
#4
n = 56
b =[x for x in range(0,56)]
print("the length of n:",len(b))
#1
got = {"jon":"stark","cersi":"lanister",}
got1 = {"denerys":"trageryn",}
got.update(got1)
print(got)
#5
set = {1,234,34,4545,657}
set2 = {1,234,5567,45}
print(set-set2)