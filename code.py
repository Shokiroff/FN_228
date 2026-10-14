from json import dump
def write_to_file(fname):
	data = {'name' : 'Shodmon', 'stage':12,'Hobby' : 'Cybersport and football'}
	f = open(fname,'wt')
	dump(data,f)
	f.close()
	print("Faylga ma'lumot yozildi")


if __name__ == "__main__":
	write_to_file('shaxsiy.json')
