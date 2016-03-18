from login import login
from bs4 import BeautifulSoup

def spotlight():

	import mechanize

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)

	br.open("https://academics.vit.ac.in/include_spotlight_part01.asp")
	response = br.open("https://academics.vit.ac.in/include_spotlight_part01.asp")
	soup = BeautifulSoup(response.get_data())
	
	tables = soup.findAll('table')

	myTable = tables[0]

	rows = myTable.findChildren(['th','tr'])
	acad = []

	for row in rows:

		text = row.find('td').string

		if row.find('a') is not None:
			link = "https://academics.vit.ac.in/"+row.find('a')['href'] 
		else:
			link = "No_link"

		if text == None:
			print "hi"
		else:
			acad.append({"text": text, "url" : link})

	br.open("https://academics.vit.ac.in/include_spotlight_part02.asp")
	response = br.open("https://academics.vit.ac.in/include_spotlight_part02.asp")
	soup = BeautifulSoup(response.get_data())
	
	try:
		tables = soup.findAll('table')
		myTable = tables[0]

		rows = myTable.findChildren(['th','tr'])
		coe = []
		for row in rows:

			text = row.find('td').string

			if row.find('a') is not None:
				link = "https://academics.vit.ac.in/"+row.find('a')['href'] 
			else:
				link = "No_link"

			if text == None:
				print "hi"
			else:
				coe.append({"text": text, "url" : link})

	except IndexError:
		myTable = 'null'
		coe = 'no_data'

	br.open("https://academics.vit.ac.in/include_spotlight_part03.asp")
	response = br.open("https://academics.vit.ac.in/include_spotlight_part03.asp")
	soup = BeautifulSoup(response.get_data())

	try:
		tables = soup.findAll('table')
		myTable = tables[0]

		rows = myTable.findChildren(['th','tr'])
		research = []

		for row in rows:

			text = row.find('td').string

			if row.find('a') is not None:
				link = "https://academics.vit.ac.in/"+row.find('a')['href'] 
			else:
				link = "No_link"

			if text != None:
				research.append({"text": text, "url" : link})

	except IndexError:
		myTable = 'null'
		research = 'no_data'

	return {"status" : "Success" , "academics" : acad, "COE" : coe , "research" : research}