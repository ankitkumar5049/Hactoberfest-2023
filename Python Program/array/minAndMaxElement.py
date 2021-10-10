# Linear search
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0
        
def getMinMax(arr:list, n:int):
    minmax = pair()
    
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
    
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
        
    for i in range(2,n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
            
    return minmax
    
# Driver code
if __name__=="__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr,arr_size)
    print("Minimum element is",minmax.min)
    print("Maximum element is",minmax.max)
    
    
# Tournament method

def getMinMax(low, high, arr):
	arr_max = arr[low]
	arr_min = arr[low]
	
	if low == high:
		arr_max = arr[low]
		arr_min = arr[low]
		return (arr_max, arr_min)
		
	elif high == low + 1:
		if arr[low] > arr[high]:
			arr_max = arr[low]
			arr_min = arr[high]
		else:
			arr_max = arr[high]
			arr_min = arr[low]
		return (arr_max, arr_min)
	else:		
		mid = int((low + high) / 2)
		arr_max1, arr_min1 = getMinMax(low, mid, arr)
		arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)

	return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# Driver code
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)

   