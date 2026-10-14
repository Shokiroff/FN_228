from json import dump
def write_to_file(fname):
	data = {'name' : 'Shodmon', 'stage':12,'Hobby' : 'Cybersport and football'}
	f = open(fname,'wt')
	dump(data,f)
	f.close()
	print("Faylga ma'lumot yozildi")


def read_file(fname):
	with open(fname,"rt") as f:
		data = json.load(f)
		pass

if __name__ == "__main__":
	write_to_file('shaxsiy.json')
