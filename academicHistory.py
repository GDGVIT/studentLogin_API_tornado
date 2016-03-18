from login import login
from bs4 import BeautifulSoup

def academicHistory(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		br.open("https://academics.vit.ac.in/student/student_history.asp")
		response = br.open("https://academics.vit.ac.in/student/student_history.asp")
		soup = BeautifulSoup(response.get_data())

		tables = soup.findAll('table')
		myTable = tables[2]

		rows = myTable.findChildren(['th','tr'])
		rows = rows[1:]

		#initialising some required variables
		history1 = {}

		#extracting data
		for row in rows:

			cells = row.findChildren('td')
			cells = cells[1:6]

			history1[cells[0].string.replace("\r\n\t\t","")] = dict({("course_title" , cells[1].string.replace("\r\n\t\t","")) , ("course_type" , cells[2].string.replace("\r\n\t\t","")) , ("credit" , cells[3].string.replace("\r\n\t\t","")) , ("grade" , cells[4].string.replace("\r\n\t\t",""))})

		myTable = tables[3]

		rows = myTable.findChildren(['th','tr'])
		rows = rows[1:]

		#initialising some required variables
		history2 = {}

		#extracting data
		for row in rows:

			cells = row.findChildren('td')

			history2 = dict({("credits registered" , cells[0].string.replace("\r\n\t\t","")) , ("credits earned" , cells[1].string.replace("\r\n\t\t","")) , ("cgpa" , cells[2].string.replace("\r\n\t\t","")) , ("rank" , cells[3].string.replace("\r\n\t\t",""))})

		myTable = tables[4]

		rows = myTable.findChildren(['th','tr'])
		rows = rows[1:]

		#initialising some required variables
		grdSumm = {}

		#extracting data
		for row in rows:

			cells = row.findChildren('td')

			grdSumm = dict({("S grades" , cells[0].string.replace("\r\n\t\t","")) , ("A grades" , cells[1].string.replace("\r\n\t\t","")) , ("B grades" , cells[2].string.replace("\r\n\t\t","")) , ("C grades" , cells[3].string.replace("\r\n\t\t","")) , ("D grades" , cells[4].string.replace("\r\n\t\t","")) , ("E grades" , cells[5].string.replace("\r\n\t\t","")) , ("F grades" , cells[6].string.replace("\r\n\t\t","")) , ("N grades" , cells[7].string.replace("\r\n\t\t",""))})

		return {"status" : "Success" , "history 1" : history1 , "history 2" : history2 , "grade summary" : grdSumm}

	else :
		print "FAIL"
		return {"status" : "Failure"}