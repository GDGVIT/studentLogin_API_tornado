from login import login
from bs4 import BeautifulSoup

def examSchedule(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	#checking that are we logged in or not

	if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#inmporting Queue
		import Queue as q

		#opening exam schedule page

		br.open("https://academics.vit.ac.in/student/exam_schedule.asp?sem=WS")
		response = br.open("https://academics.vit.ac.in/student/exam_schedule.asp?sem=WS")
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findAll('table')

		try:
			myTable = tables[1]
		except IndexError:
			myTable = 'null'
			examSchedule = {"cat1" : "Not_updated" , "cat2" : "Not_updated" , "term_end" : "Not_updated"}

		else:

			rows = myTable.findChildren(['th','tr'])
			rows = rows[2:]

			#initialising some required variables for getting schedule for CAT-1
			schedule = {}

			#holding the cat1, cat2, termend schedules in queue
			p = q.Queue()
			
			#extracting data
			for row in rows:

				cells = row.findChildren('td')

				if len(cells) != 1:

					schedule[cells[1].string.replace("\r\n\t\t","")] = dict({("crTitle",cells[2].string.replace("\r\n\t\t","")), ("slot",cells[4].string.replace("\r\n\t\t","")), ("date",cells[5].string.replace("\r\n\t\t","")), ("day",cells[6].string.replace("\r\n\t\t","")), ("session",cells[7].string.replace("\r\n\t\t","")), ("time",cells[8].string.replace("\r\n\t\t",""))})
			
				elif len(cells) == 1:

					p.put(schedule)
					schedule = {}
					continue

			cat1 = p.get()

			if p.empty():
				cat2 = {}
			else:
				cat2 = p.get()
			if p.empty():
				termend = {}
			else:
				termend = p.get()

		return {"status" : "Success" , "cat1" : cat1 , "cat2" : cat2 , "term_end" : termend}

	else :
		print "FAIL"
		return {"status" : "Failure"}