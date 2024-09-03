def cgpaCalculator():
	TotalScoreOfferable = 0
	obtainedGrade = 0

	numberOfCourses = int(input("Please Enter the number of Courses you Offered: "))
	print ("*******************")
	for x in range(numberOfCourses):
		Course1 = input("Enter The Course you took:")
		credit = int(input ("How many credit is the Course you took: "))
		score = input("Please Enter your Score:")
		print ("****************")
		TotalScoreOfferable += credit* 5

		if (score=='O'):
			grade = 10
		elif(score=='A+'):
			grade = 9
		elif(score=='A' ):
			grade = 8
		elif(score=='B+'):
			grade = 7
		elif (score=='B'):
			grade = 6
		elif (score=='c'):
			grade = 5
		else :
			grade = 0

		obtainedGrade += credit*grade

	Cgpa =float((obtainedGrade / TotalScoreOfferable) * 5)
	print("THANKS FOR ALL YOUR INPUT YOUR CGPA IS : " + str(Cgpa))


cgpaCalculator()
