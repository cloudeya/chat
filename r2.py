def read_file(filename): 
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
		return lines


def convert(lines): 
	person = None #預設值
	yun_count = 0
	ding_count = 0
	yun_sticker_count = 0
	for line in lines: #對話記錄一行一行讀
		s = line.split(' ') #csv是用逗點分隔和這裡不一樣，這裡是用空白鍵切割，切割完會變清單
		time = s[0]
		name = s[1]
		if name == '昀':
			if s[2] == '貼圖':
				yun_sticker_count += 1
			else:
				for m in (s[2:]): #一句對話中有幾個字
					yun_count += len(m)
		elif name == '丁':
			for m in (s[2:]): #一句對話中有幾個字
				ding_count += len(m)
	print('昀說了', yun_count, '個字', '傳了', yun_sticker_count, '張貼圖')
	print('丁說了', ding_count, '個字')


def write_file(filename, lines): 
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')


#執行function
def main():
	lines = read_file('r2.txt')
	lines = convert(lines) #把lines丟進去回傳的值再覆蓋掉
	#write_file('output.txt', lines) 先註解掉因為這裡用不到寫入

main() #程式的進入點