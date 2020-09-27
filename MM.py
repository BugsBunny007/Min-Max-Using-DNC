INF = float('inf')
# Divide & Conquer solution to find minimum and maximum number in a list
def findMinAndMax(A, left, right, min, max):

	# if list contains only one element

	if left == right:		   # common comparison

		if min > A[right]:	  # comparison 1
			min = A[right]

		if max < A[left]:	   # comparison 2
			max = A[left]

		return min, max

	# if list contains only two elements

	if right - left == 1:	   # common comparison

		if A[left] < A[right]:  # comparison 1
			if min > A[left]:   # comparison 2
				min = A[left]

			if max < A[right]:  # comparison 3
				max = A[right]

		else:
			if min > A[right]:  # comparison 2
				min = A[right]

			if max < A[left]:   # comparison 3
				max = A[left]

		return min, max

	# find mid element
	mid = (left + right) // 2

	# recur for left sublist
	min, max = findMinAndMax(A, left, mid, min, max)

	# recur for right sublist
	min, max = findMinAndMax(A, mid + 1, right, min, max)

	return min, max


if __name__ == '__main__':
    A=[]
    n= int(input("Enter quantity :"))
    for i in range(n): 
        print("Enter value ",i+1)        
        A.append(int(input()))
	    # initialize the minimum element by infinity and the
	# maximum element by minus infinity
    (min, max) = (INF, -INF)
    (min, max) = findMinAndMax(A, 0, len(A) - 1, min, max)
    print("The minimum element in the list is", min)
    print("The maximum element in the list is", max)

#OUTPUT:-
#python MM.py 
#Enter quantity :7
#('Enter value ', 1)
#1
#('Enter value ', 2)
#2
#('Enter value ', 3)
#3
#('Enter value ', 4)
#4
#('Enter value ', 5)
#5
#('Enter value ', 6)
#6
#('Enter value ', 7)
#7
#('The minimum element in the list is', 1)
#('The maximum element in the list is', 7)
