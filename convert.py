from pyfiglet import Figlet
import logging
import sys
import getpass

from sqlalchemy import create_engine, select, insert, update, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from sqlalchemy.sql.schema import UniqueConstraint

from font_converter import uni2zg, zg2uni

logging.basicConfig(format='Zawgyi To Unicode (%(asctime)s) - %(message)s', level=logging.INFO)
_logger = logging.getLogger(__name__)


def convert(option, url, db, port, user, password):

	address = None
	if option == 1:
		address = "postgresql://%s:%s@%s:%s/%s" % (user, password, url, port, db)
	elif option == 2:
		address = "mysql+pymysql://%s:%s@%s:%s/%s" % (user, password, url, port, db)

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

		unique_col_name = []

		for result in results:
			data = {}
			for column, value in result.items():
				if(column == primaryKeyColName):
					continue
				else:
					if(type(value) == str or type(value) == unicode) and \
						table.columns[column].type.__visit_name__ in ['CHAR', 'VARCHAR', 'TEXT']:
						data.update({column: zg2uni(value)})
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
		print('[2]:  Mysql\n')

		def choose_db():
			url_preix = raw_input("Select Database: ")
			try:
				if int(url_preix) not in [1, 2]:
					return choose_db()
				return int(url_preix)
			except Exception as ex:
				return choose_db()

		db_type = choose_db()
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
