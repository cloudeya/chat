def read_file(filename): 
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines): 
	new = []
	person = None #預設值，沒宣告的話，檔案第一行如果不是人名會報錯
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #只有人名沒有對話紀錄的時候先跳過(只存了人名)
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person不是None，有值才會執行下面那行
			new.append(person + ':' + line)
	return new

def write_file(filename, lines): 
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')


#執行function
def main():
	lines = read_file('對話紀錄.txt')
	lines = convert(lines) #把lines丟進去回傳的值再覆蓋掉
	write_file('output.txt', lines)

main()