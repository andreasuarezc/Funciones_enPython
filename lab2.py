def isYearLeap(year):
        if year % 4 == 0 and year % 100 != 0:
                return True
        else:
                if year % 100 == 0 and year %400 == 0:
                        return True
                else:
                        return False

def daysInMonth(year, month):
        if isYearLeap(year)==True:
                if month==2:
                        return 29
        if month==2:
                return 28
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                return 31
        if month==4 or month==6 or month== 9 or month==11:
                return 30

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	print(yr)
	print(mo)
	print(result)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
