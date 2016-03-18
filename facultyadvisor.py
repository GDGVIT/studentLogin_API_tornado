from login import login
from bs4 import BeautifulSoup

def facultyAdvisor(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	#checking that are we logged in or not

	if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#opening faculty advisor details page
		#opening faculty advisor details page
		br.open("https://academics.vit.ac.in/student/faculty_advisor_view.asp")
		response = br.open("https://academics.vit.ac.in/student/faculty_advisor_view.asp")
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findChildren('table')
		myTable = tables[1]
		rows = myTable.findChildren(['th','tr'])

		#initialising some required variables
		faculty_advisor = {}

		#extracting data
		for row in rows:

			cells = row.findChildren('td')

			if len(cells) == 1:
				continue

			else:
				faculty_advisor[cells[0].string.replace("\r\n\t\t","")] = cells[1].string.replace("\r\n\t\t","")

		return {"status" : "Success" , "faculty_det" : faculty_advisor}

	else :
		print "FAIL"
		return {"status" : "Failure"}