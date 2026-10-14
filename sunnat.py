from os import system
import json
def saralash(fname):
	with open(fname, encoding = 'utf-8') as f:
		data = json.load(f)
	res = list(filter(lambda x: x['yosh'] > 40, data))
	print(f"\t+--------------------+--------+--------------------+")
	print(f"\t|         Ism        |  Yosh  |       Lavozim      |")
	print(f"\t+--------------------+--------+--------------------+")
	for x in res:
		for y in x['ish_tajriba']:
			print(f"\t|{x['ism']:<20s}|{x['yosh']:<8d}|{y['lavozim']:<20s}|")
			print(f"\t+--------------------+--------+--------------------+")

if __name__ == "__main__":
	system("clear")
	saralash('user.json')
