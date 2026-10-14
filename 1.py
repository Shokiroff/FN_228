from os import system
import json
def saralash(fname):
	with open(fname, encoding = 'utf-8') as file:
		data = json.load(file)
	print("Yosh statistikasi:")
	print(f"Jami odamlar: {len(data)} ta")
	res = list(filter(lambda x: x['yosh'], data))
	sm = sum(map(lambda x: x['yosh'], res))
	print(f"O'rtacha yosh: {sm/len(res)}")
	mx = max(list(map(lambda x: x['yosh'], res)))
	mn = min(list(map(lambda x: x['yosh'], res)))
	print(f"Eng katta: {mx}")
	print(f"Eng kichik: {mn}")

if __name__ == "__main__":
	system("clear")
	saralash('user.json')
