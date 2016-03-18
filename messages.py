from login import login
from bs4 import BeautifulSoup

def messages(reg_no = "", pwd = ""):
	br = login(reg_no,pwd)

	print br.geturl()

	if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		br.open("https://academics.vit.ac.in/student/class_message_view.asp?sem=WS")
		response = br.open("https://academics.vit.ac.in/student/class_message_view.asp?sem=WS")

		soup = BeautifulSoup(response.get_data())
		try:
			tables = soup.findAll('table')
			myTable = tables[1]
			rows = myTable.findChildren(['th','tr'])

			rows = rows[1:]
			messages = []

			for row in rows[:-1]:

				cells = row.findChildren('td')
				
				messages.append({"From" : cells[0].string.replace("\r\n\t\t",""), "Course" : cells[1].string.replace("\r\n\t\t",""), "Message" : cells[2].string.replace("\r\n\t\t","").replace("\r\n"," "), "Posted on" : cells[3].string.replace("\r\n\t\t","")})
		except:
			messages = []

		return {"status" : "Success", "Messages" : messages}

	else :
		print "FAIL"
		return {"status" : "Failure"}