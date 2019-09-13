from pyfiglet import Figlet
import logging
import sys
import getpass
import urllib
import ConfigParser

from sqlalchemy import create_engine, select, insert, update, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from sqlalchemy.sql.schema import UniqueConstraint

from font_converter import uni2zg, zg2uni

logging.basicConfig(format='Zawgyi To Unicode (%(asctime)s) - %(message)s', level=logging.INFO)
_logger = logging.getLogger(__name__)

possible_fields = [
	'CHAR', 'VARCHAR', 'NCHAR', 'NVARCHAR', 'TEXT', 'Text', 'String', 
	'Unicode', 'UnicodeText', 'JSON', 'TINYTEXT', 'MEDIUMTEXT', 'LONGTEXT'
]

def convert(option, url, db=None, port=None, user='', password=''):

	configParser = ConfigParser.RawConfigParser()
	configFilePath = r'config.ini'
	configParser.read(configFilePath)

	address = None
	if option == 1:
		address = "postgresql://%s:%s@%s:%s/%s" % (user, password, url, port, db)
	elif option == 2:
		address = "mysql+pymysql://%s:%s@%s:%s/%s" % (user, password, url, port, db)
	elif option == 3:
		address = "sqlite:///%s" % url

	engine = create_engine(address)

	try:
		if not database_exists(engine.url):
			print("Database doesn't exist.")
			return
	except Exception as dbex:
		print(dbex)
		return

	conn = engine.connect()

	session = sessionmaker(bind=engine)()

	count = 0
	table_count = len(engine.table_names())

	for table_name in engine.table_names():

		ignore_ids = []
		for k, v in configParser.items('ignore_table'):
			if k == table_name and v == '*':
				continue
			elif k == table_name:
				ignore_ids += v.split(",")

		_logger.info("%d%% - Fetching %s..." % ((count * 100/table_count), table_name))

		count = count + 1

		# sys.stdout.write('\r')
		# sys.stdout.write("%d%% - Fetching %s..." % ((count * 100/table_count), table_name))
		# sys.stdout.write("[%-20s] %d%% - Fetching %s..." % ('='*(count * 100/table_count), (count * 100/table_count), table_name))
		# sys.stdout.flush()

		metadata = MetaData(bind=engine)
		table = Table(table_name, metadata, autoload=True, autoload_with=engine)
		stmt = select([table])

		results = conn.execute(stmt).fetchall()
		columns = conn.execute(stmt).keys()


		if not table.primary_key.columns:
			_logger.info("Skipped %s because there is no have primary key." % table_name)
			continue

		primaryKeyCol = table.primary_key.columns.values()[0]
		primaryKeyColName = table.primary_key.columns.values()[0].name

		for result in results:
			data = {}
			for column, value in result.items():
				if column == primaryKeyColName:
					if str(value) in ignore_ids:
						break
					continue
				else:
					if(type(value) == str or type(value) == unicode) and \
						table.columns[column].type.__visit_name__ in possible_fields:
						try:
							val = urllib.unquote_plus(value)
						except Exception as urlex:
							val = value
						data.update({column: zg2uni(val)})

			if data:
				update_rec = update(table).where(primaryKeyCol==result[primaryKeyColName])
				update_rec = update_rec.values(data)
				session.execute(update_rec)

	session.commit()
	session.close()

	sys.stdout.write("%d%% - Finished.\n" % (count * 100/table_count))
	sys.stdout.flush()


if __name__ == '__main__':

	try:
		f = Figlet(font='cybermedium')
		print(f.renderText('Zawgyi To Unicode Database Converter Tool.\n'))
		print('Please select database type: \n')
		print('[1]: Postgresql\n')
		print('[2]: Mysql\n')
		print('[3]: Sqlite3\n')

		def choose_db():
			url_preix = raw_input("Select Database: ")
			try:
				if int(url_preix) not in [1, 2, 3]:
					return choose_db()
				return int(url_preix)
			except Exception as ex:
				return choose_db()

		db_type = choose_db()

		if db_type == 3:

			db_route = raw_input("Database file path: ")
			convert(db_type, db_route)

		else:

			db_name = raw_input("Database name: ")
			db_route = raw_input("Database route: ")

			def request_port():
				db_port = raw_input("Database port: ")
				try:
					return int(db_port)
				except Exception as ex:
					print("Please input port number\n")
					return request_port()

			db_port = request_port()
			user_name = raw_input("User name: ")
			password = getpass.getpass("Password: ")

			convert(db_type, db_route, db_name, db_port, user_name, password)
	except KeyboardInterrupt as ke:
		print("Abort!")
