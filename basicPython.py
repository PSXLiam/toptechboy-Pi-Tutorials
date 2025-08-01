
numGrades=int(input('How Many Grades? '))
x=[]
totalGrades=0
for i in range(0,numGrades,1):
	myGrade=int(input('Input Your Grade: '))
	x.append(myGrade)
for i in range(0,numGrades,1):
	totalGrades=totalGrades+x[i]
	averageGrade=totalGrades/numGrades
print('Your Grades Are:')
for i in range(0,numGrades,1):
	print(x[i],'Marks')

print('Your Average Grade is ',int(averageGrade))
