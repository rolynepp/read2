data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 #count =  count + 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有',len(data),'筆資料')

a = 0
for d in data:
	a = a + len(d)
	b = a / len(data) 
print('留言的平均長度為', b)

new = []
for e in data:
	if len(e) < 100:
		new.append(e)
print('一共有', len(new) , '筆留言長度小於100')
print(new[0])

good = []

for e in data:
	if 'good' in e:
		good.append(e)

print('一共有', len(good), '提到good')