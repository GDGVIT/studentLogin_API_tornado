from login import login
from bs4 import BeautifulSoup

def timetable(reg_no = "", pswd = ""):

		br = login(reg_no,pswd)

		#checking that are we logged in or not
		if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
			print "SUCCESS"

			#opening time table page
			br.open("https://academics.vit.ac.in/student/timetable_ws.asp")
			response = br.open("https://academics.vit.ac.in/student/timetable_ws.asp")
			soup = BeautifulSoup(response.get_data())

			#extracting tables
			tables = soup.findAll('table')

			#getting required table
			myTable = tables[1]
			rows = myTable.findChildren(['th','tr'])
			rows = rows[1:]

			#initialising some required variables
			time_table = {}

			#extracting data
			for row in rows:

				cells = row.findAll('td')
				if len(cells) == 1:
					print "row_with_no_entries"
					continue

				else:
					
					#if the course contains embedded lab
					if len(cells) == 10:
						if cells[1].getText().replace("\r\n\t\t","") in time_table.keys():
							time_table[cells[1].getText().replace("\r\n\t\t","")+"_L"] = dict({("class_number",cells[0].getText().replace("\r\n\t\t","")), ("course_code",cells[1].getText().replace("\r\n\t\t","")), ("course_title",cells[2].getText().replace("\r\n\t\t","")), ("course_type",cells[3].getText().replace("\r\n\t\t","")), ("ltpjc",cells[4].getText().replace("\n\r\n\t\t\t\t","").replace("\r\n\t\t\t\t\n","")), ("course_mode",cells[5].getText().replace("\r\n\t\t","")), ("course_option",cells[6].getText().replace("\r\n\t\t","")), ("slot",cells[7].getText().replace("\r\n\t\t","")), ("venue",cells[8].getText().replace("\r\n\t\t","")), ("faculty",cells[9].getText().replace("\r\n\t\t",""))})
						else:
							time_table[cells[1].getText().replace("\r\n\t\t","")] = dict({("class_number",cells[0].getText().replace("\r\n\t\t","")), ("course_code",cells[1].getText().replace("\r\n\t\t","")), ("course_title",cells[2].getText().replace("\r\n\t\t","")), ("course_type",cells[3].getText().replace("\r\n\t\t","")), ("ltpjc",cells[4].getText().replace("\n\r\n\t\t\t\t","").replace("\r\n\t\t\t\t\n","")), ("course_mode",cells[5].getText().replace("\r\n\t\t","")), ("course_option",cells[6].getText().replace("\r\n\t\t","")), ("slot",cells[7].getText().replace("\r\n\t\t","")), ("venue",cells[8].getText().replace("\r\n\t\t","")), ("faculty",cells[9].getText().replace("\r\n\t\t",""))})
					else:
						time_table[cells[3].getText().replace("\r\n\t\t","")] = dict({("class_number",cells[2].getText().replace("\r\n\t\t","")), ("course_code",cells[3].getText().replace("\r\n\t\t","")), ("course_title",cells[4].getText().replace("\r\n\t\t","")), ("course_type",cells[5].getText().replace("\r\n\t\t","")), ("ltpjc",cells[6].getText().replace("\n\r\n\t\t\t\t","").replace("\r\n\t\t\t\t\n","")), ("course_mode",cells[7].getText().replace("\r\n\t\t","")), ("course_option",cells[8].getText().replace("\r\n\t\t","")), ("slot",cells[9].getText().replace("\r\n\t\t","")), ("venue",cells[10].getText().replace("\r\n\t\t","")), ("faculty",cells[11].getText().replace("\r\n\t\t","")), ("registration_status",cells[12].getText().replace("\r\n\t\t",""))})
			return {"status" : "Success" , "time_table" : time_table}
		else :
			print "FAIL"
			return {"status" : "Failure"}