# Function to find the intersection of two arrays
def find_intersection(arr1, arr2, temp, m, n, k):
	i = 0
	j = 0
	while i < m and j < n:
		if arr1[i] < arr2[j]:
			i += 1
		elif arr2[j] < arr1[i]:
			j += 1
		else:
			temp[k[0]] = arr1[i]
			i += 1
			j += 1
			k[0] += 1

# Main function


def main():
	arr1 = [1, 5, 10, 20, 40, 80]
	arr2 = [6, 7, 20, 80, 100]
	arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
	n1 = len(arr1)
	n2 = len(arr2)
	n3 = len(arr3)

	temp = [0] * 200000
	ans = [0] * 200000

	k = [0] # Mutable list to simulate pass-by-reference

	# Function call to find the temp array
	find_intersection(arr1, arr2, temp, n1, n2, k)
	temp_size = k[0]
	k[0] = 0

	# Function call to find the ans array
	find_intersection(arr3, temp, ans, n3, temp_size, k)

	print("Common elements present in arrays are:")

	# Printing the common elements
	for i in range(k[0]):
		print(ans[i], end=" ")
	print()


if __name__ == "__main__":
	main()
