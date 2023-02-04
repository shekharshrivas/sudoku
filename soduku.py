soduku=[[8,2,7,1,5,4,3,9,6],
		[9,6,5,3,2,7,1,4,8],
		[3,4,1,6,8,9,7,5,2],
		[5,9,3,4,6,8,2,7,1],
		[4,7,2,5,1,3,6,8,9],
		[6,1,8,9,7,2,4,3,5],
		[7,8,6,2,3,5,9,1,4],
		[1,5,4,7,9,6,8,2,3],
		[2,3,9,8,4,1,5,6,7]]

def soducu_row(soduku):
	for i in soduku:
		for x in range(1,10):
			if i.count(x) != 1:
				return False
	return True
# print(soducu_row(soduku))

def soduku_column(soduku):
	lst=[]
	for i in range(len(soduku[0])):
		row=[]
		for x in range(len(soduku)):
			row.append(soduku[x][i])
		lst.append(row)
	for element in lst:
		for t in range(1,10):
			if element.count(t) != 1:
				return False
	return True

	# return lst
# print(soduku_column(soduku))

def submatrix(soduku):
	lst2=[]
	acc=[]
	acc1=[]
	acc2=[]
	acc3=[]
	acc4=[]
	acc5=[]
	acc6=[]
	acc7=[]
	acc8=[]
	for i in range(9):
		if i<3:
			for v in range(3):
				acc.append(soduku[i][v])
			for t in range(3,6):
				acc1.append(soduku[i][t])
			for third_subM in range(6,9):
				acc2.append(soduku[i][third_subM])
		elif i<6:
			for four_subM in range(3):
				acc3.append(soduku[i][four_subM])
			for five_subM in range(3,6):
				acc4.append(soduku[i][five_subM])
			for six_subM in range(6,9):
				acc5.append(soduku[i][six_subM])
		else:
			for seven_subM in range(3):
				acc6.append(soduku[i][seven_subM])
			for eight_subM in range(3,6):
				acc7.append(soduku[i][eight_subM])
			for nine_subM in range(6,9):
				acc8.append(soduku[i][nine_subM])

	lst2.append(acc)
	lst2.append(acc1)
	lst2.append(acc2)
	lst2.append(acc3)
	lst2.append(acc4)
	lst2.append(acc5)
	lst2.append(acc6)
	lst2.append(acc7)
	lst2.append(acc8)

	for element2 in lst2:
		for i in range(1,10):
			if element2.count(i) != 1:
				return False
		return True

# print(submatrix(soduku))

def soduku_or_not(soduku):
	if not(soducu_row(soduku) and soduku_column(soduku) and submatrix(soduku)):
		return False
	return True
print(soduku_or_not(soduku))



