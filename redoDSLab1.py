def countNegatives(array, size):
	count = 0
	for i in range(size):
		if (array[i] < 0):
			count += 1
	return count;
	
def findMinMultof5(array, size):
	minMult = 0
	for i in range(size):
		if(array[i] % 5 == 0 and minMult == 0):
			minMult = array[i]
		elif(array[i] % 5 == 0 and array[i] < minMult):
			minMult = array[i]
	return minMult;
	
def findMinMultOf5Index(array, size):
	index = -1
	minMult = 0
	for i in range(size):
		if(array[i] % 5 == 0 and array[i] == 0):
			minMult = array[i]
			index = i
		elif(array[i] % 5 == 0 and array[i] < minMult):
			minMult = array[i]
			index = i
	return index;
			
def removeFxn(array, size, index):
	if(size > index and index >= 0):
		i = index
		for i in range (size - 1):
			array[i] = array[i + 1]
		return True;
	else:
		return False;

	
##main
ex1 = [3, 1, 5, -1, 10]
print(countNegatives(ex1, 5)) ##prints 1
print(countNegatives(ex1, 3)) ##prints 0

print(findMinMultof5(ex1, 5)) ##prints 5
print(findMinMultof5(ex1, 3)) ##prints 5

print(findMinMultOf5Index(ex1, 5)) ##prints -1
print(findMinMultOf5Index(ex1, 4)) ##prints -1
print(findMinMultOf5Index(ex1, 3)) ##prints -1
print(findMinMultOf5Index(ex1, 2)) ##prints -1
print(findMinMultOf5Index(ex1, 1)) ##prints -1
print("---------------------------------")

##print(removeFxn(ex1, 5, 0)) ##prints true
##print(removeFxn(ex1, 5, 1)) ##prints true

##print(removeFxn(ex1, 4, 0)) ##prints true
##print(removeFxn(ex1, 4, 4)) ##prints false

if(removeFxn(ex1, 5, 4) == True):
	for i in range(5):
		print(ex1[i])