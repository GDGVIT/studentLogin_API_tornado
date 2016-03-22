from login import login
from bs4 import BeautifulSoup

def getMarks15(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	#checking that are we logged in or not

	if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#opening marks page

		br.open("https://academics.vit.ac.in/student/marks.asp?sem=WS")
		response = br.open("https://academics.vit.ac.in/student/marks.asp?sem=WS")
		soup = BeautifulSoup(response.get_data())

		#extracting tables

		tables = soup.findAll('table')
		myTable = tables[1]

		#initialising some required variables

		marks = {}
		rows = myTable.findChildren(['th','tr'])
		rows = rows[2:]

		#extracting data

		for row in rows:
			rowdata = []
			assessments = []
			cells = row.findAll('td')
			j = 0

			for cell in cells:
				value = cell.getText()
				#print value
				if value is u'' or value is u'N/A':
					rowdata.append('0')
					
				else:
					rowdata.append(value)
			#print rowdata

			if len(cells) == 10:
				assessments.append({"title" : "CAT-I", "max_marks" : 50, "weightage" : 10, "conducted_on" : "Check Exam Schedule", "status" : rowdata[5], "scored_marks" : rowdata[6], "scored_percentage" : (((float(rowdata[6]))/50)*10) })
				assessments.append({"title" : "CAT-II", "max_marks" : 50, "weightage" : 10, "conducted_on" : "Check Exam Schedule", "status" : rowdata[7], "scored_marks" : rowdata[8], "scored_percentage" : (((float(rowdata[8]))/50)*10) })
				assessments.append({"title" : "Digital Assignment", "max_marks" : 30, "weightage" : 30, "conducted_on" : "Check Exam Schedule", "scored_marks" : rowdata[9], "scored_percentage" : rowdata[9] })

				marks[rowdata[2].replace("\r\n\t\t","")] = {"assessments" : assessments, "max_marks" : 130, "max_percentage" : 50, "scored_marks" : (float(rowdata[6])+float(rowdata[8])+float(rowdata[9])), "scored_percentage" : ((((float(rowdata[6]))/50)*10)+(((float(rowdata[8]))/50)*10)+(float(rowdata[9])))}
			
			else:
				continue
			
		return {"status" : "Success" , "marks" : marks}

	else :
		print "FAIL"
		return {"status" : "Failure"}