from os import system

def calculate_average(nums):
	summa = 0
	for x in nums:
		summa += x
	return summa/len(nums)


if __name__ == "__main__":
	system("clear")
	calculate_average([5,6,9,7,5,6])
