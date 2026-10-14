from os import system
import json

def uqish(fname):
	with open(fname, encoding = 'utf-8') as f:
		data = json.load(f)
	return data

def filtrlash(data, nom):
	return list(filter(lambda x: x["ta'lim"]['mutaxassislik'].lower() == nom.lower(), data))

def jadval(data, nom):
	print(f"\n\"{nom}\" bo'yicha o'qiganlar:")
	print("+--------------------+------+----------------------------+")
	print(f"| {'Ism':<18s} | {'Yosh':<4s} | {'Universitet':<26s} |")
	print("+--------------------+------+----------------------------+")
	for x in data:
		uni = x["ta'lim"]['universitet'][:26]
		print(f"| {x['ism']:<18s} | {x['yosh']:<4d} | {uni:<26s} |")
	print("+--------------------+------+----------------------------+")

if __name__ == "__main__":
	system("clear")
	data = uqish('users.json')
	nom = input("Mutaxassislik nomi >>> ")
	natija = filtrlash(data, nom)
	if natija:
		jadval(natija, nom)
	else:
		print("Bunday mutaxassislik bo'yicha hech kim topilmadi")
