import tornado.ioloop
import tornado.web

import os
import json

from login import login
from facultyadvisor import facultyAdvisor
from timetable import timetable
from attendance import attendance
from examSchedule import examSchedule
from cal import calmarks
from spotlight import spotlight
from academicHistory import academicHistory
from changePassword import changePassword
from messages import messages
from marks14 import marks14
from marks15 import marks15

from mechanize import Browser
br = Browser()

class sampleHandler(tornado.web.RequestHandler):

	def post(self):
		self.write("Hello!! And welcome To Student API in tornado")

class LoginHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		br = login(regno, psswd)
		self.write(dict(Registration_No = regno, Campus = "Vellore", status = "You are logged in"))

class FacultyAdvisorHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Faculty_advisor_details = facultyadvisor(regno, psswd)))

class TimetableHandler(tornado.web.RequestHandler):
	
	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(timetable = timetable(regno, psswd)))

class AttendanceHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(attendance = attendance(regno, psswd)))

class ExamScheduleHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Exam_Schedule = exmaSchedule(regno, psswd)))

class MarksHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		if int(regno[0:2]) > 14:
			self.write(dict(Faculty_advisor_details = marks15(regno, psswd)))
		else:
			self.write(dict(Faculty_advisor_details = marks14(regno, psswd)))

class CALHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		if int(regno[0:2]) > 14:
			self.write(dict(CAL_marks = calmarks(regno, psswd)))
		else:
			self.write(dict(status = "Not Supported"))

class SpotlightHandler(tornado.web.RequestHandler):

	def get(self):
		self.write(dict(Spotlight = spotlight()))

class AcademicHistoryHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(Academic_History = academicHistory(regno, psswd)))

class ChangePasswordHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(status = changePassword(regno, psswd)))

class MessageHandler(tornado.web.RequestHandler):

	def post(self):
		regno = self.get_argument("regNo")
		psswd = self.get_argument("psswd")
		self.write(dict(message = messages(regno, psswd)))

if __name__ == "__main__":
	application = tornado.web.Application([ (r"/", sampleHandler), (r"/login", LoginHandler), (r"/facadvdet", FacultyAdvisorHandler), (r"/timetable", TimetableHandler), (r"/attendance", AttendanceHandler), (r"/exam", ExamScheduleHandler), (r"/makrs", MarksHandler), (r"/calmarks", CALHandler), (r"/spotlight", SpotlightHandler), (r"/acadhist", AcademicHistoryHandler), (r"/message", MessageHandler) ], debug = True)
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()