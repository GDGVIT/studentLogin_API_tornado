#importing the required tornado files
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
from tornado import gen
from tornado.options import define, options

import os

# files import for fetching the data
from login import login
from facultyadvisor import getFacultyAdvisor
from timetable import getTimetable
from attendance import getAttendance
from examSchedule import getExamSchedule
from cal import getCalmarks
from spotlight import getSpotlight
from academicHistory import getAcademicHistory
from changePassword import changePassword
from messages import getMessages
from marks14 import getMarks14
from marks15 import getMarks15
from majorRoute import refresh

#importing the mechanical borwser
from mechanize import Browser

define("port", default = 8000, help="Contact the One who made it Contact PIYUSH :P", type = int)

#overloading the tornado.web.Application 
class Application(tornado.web.Application):

	def __init__(self):

		handlers = [ (r"/", SampleHandler), (r"/login", LoginHandler), (r"/facadvdet", FacultyAdvisorHandler), (r"/timetable", TimetableHandler), (r"/attendance", AttendanceHandler), (r"/exam", ExamScheduleHandler), (r"/marks", MarksHandler), (r"/calmarks", CALHandler), (r"/spotlight", SpotlightHandler), (r"/acadhist", AcademicHistoryHandler), (r"/changepsswd", ChangePasswordHandler), (r"/message", MessageHandler), (r"/refresh", RefreshHandler)]
		settings = dict(debug = True)
		tornado.web.Application.__init__(self, handlers, **settings)

#for knowing the API status
class SampleHandler(tornado.web.RequestHandler):

	def post(self):
		self.write("Hello!! And welcome To Student API in tornado")

#for logging into the student login
class LoginHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		br = login(regno, psswd)
		self.write(dict(Registration_No = regno, Campus = "Vellore", status = "You are logged in"))

#for getting the faculty advisor details
class FacultyAdvisorHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Faculty_advisor_details = getFacultyAdvisor(regno, psswd)))

#for getting the time table details
class TimetableHandler(tornado.web.RequestHandler):
	
	@gen.coroutine	
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Timetable = getTimetable(regno, psswd)))

#for getting the attendance details
class AttendanceHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Attendance = getAttendance(regno, psswd)))

#for getting the exam schedule details
class ExamScheduleHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Exam_Schedule = getExamSchedule(regno, psswd)))

#for getting the marks details
class MarksHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		if int(regno[0:2]) > 14:
			self.write(dict(Marks = getMarks15(regno, psswd)))
		else:
			self.write(dict(Marks = getMarks14(regno, psswd)))

#for getting the CAL marks details
class CALHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		if int(regno[0:2]) > 14:
			self.write(dict(CAL_marks = getCalmarks(regno, psswd)))
		else:
			self.write(dict(status = "Not Supported"))

#for getting the Spotlight details
class SpotlightHandler(tornado.web.RequestHandler):

	def post(self):
		self.write(dict(Spotlight = getSpotlight()))

#for getting the Academic History details
class AcademicHistoryHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Academic_History = getAcademicHistory(regno, psswd)))

#for getting the statuss for changing password
class ChangePasswordHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		npsswd = self.get_argument("npsswd")
		self.write(dict(Status = changePassword(regno, psswd, npsswd)))

#for getting the messages details
class MessageHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Message = getMessages(regno, psswd)))

#for getting all the data
class RefreshHandler(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Data = refresh(regno, psswd)))

#main fuction to start the API
if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()