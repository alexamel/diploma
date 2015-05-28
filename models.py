from peewee import *

db = MySQLDatabase('diploma_alex', user='root',passwd='chemodan')

class User(Model):
	login = CharField()
	password = CharField()

	class Meta:
		database = db	

	def __unicode__(self):
		return 'User %r' % (self.login)

	def create():
		db.conntect()
		db.create_table(User)
