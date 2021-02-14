import insertion_sort as ins
import bubble_sort as bs 
import selection_sort as ss 
import merge_sort as ms 
import quick_sort as qs 
from os import system, name 



def display(arr):
    system('cls')  #system('cls') For windows - use system('clear') for Mac-linux to clear screen
    for i in range(len(arr)):
        print ("% d" % arr[i]) 


# Driver program 
arr = [64, 34, 25, 12, 22, 11, 90] 
if __name__ == "__main__": 
	print("\nEnter  0  for Bubble Sort")
	print("\nEnter  1  for Selection Sort")
	print("\nEnter  2  for Insertion Sort")
	print("\nEnter  3  for Quick Sort")
	print("\nEnter  4  for Merge Sort")
    
	val = input("\nEnter your value: ") 
	print(int(val)) 
	if val== '0':
		bs.bubbleSort(arr)
	elif val=='1':
		ss.selection_sort(arr)
	elif val=='2':
		ins.insertionSort(arr)
	elif val=='3':
		n = len(arr) 
		qs.quickSort(arr, 0, n-1) 
	elif val=='4':
		n=len(arr)
		ms.mergeSort(arr,0,n-1)
	else :
		print("\nWrong Input, Try Again !!")


display(arr)

