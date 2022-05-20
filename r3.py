#時間和人名連再一起要如何取出(清單分割)
lines = []
with open('r3.txt', 'r', encoding = 'utf-8') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ') #split只能切割字串不能切割清單,但切割出來的卻是清單
	time = s[0][:5] #用清單分割法，時間是前5個字(python中的字串可以當清單來看待)
	name = s[0][5:]
	print(time)
	print(name)
	