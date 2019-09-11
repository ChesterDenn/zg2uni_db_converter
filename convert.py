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


def convert(url, db, port, user, password):
	engine = create_engine("postgresql://%s:%s@%s:%s/%s" % (user, password, url, port, db))
	if not database_exists(engine.url):
		print("Database doesn't exist.")

	conn = engine.connect()

	session = sessionmaker(bind=engine)()

	count = 0
	table_count = len(engine.table_names())

	for table_name in engine.table_names():

		# _logger.info("Fetching %s... \t\t\t\t\t\t\t\t\t%d%%" % (table_name, 5*count))

		count = count + 1

		sys.stdout.write('\r')
		sys.stdout.write("%d%% - Fetching %s..." % ((count * 100/table_count), table_name))
		# sys.stdout.write("[%-20s] %d%% - Fetching %s..." % ('='*(count * 100/table_count), (count * 100/table_count), table_name))
		sys.stdout.flush()

		metadata = MetaData(bind=engine)
		table = Table(table_name, metadata, autoload=True, autoload_with=engine)
		stmt = select([table])

		results = conn.execute(stmt).fetchall()
		columns = conn.execute(stmt).keys()


		if not table.primary_key.columns:
			# _logger.info("Skipped %s because there is no have primary key." % table_name)
			continue

		primaryKeyCol = table.primary_key.columns.values()[0]
		primaryKeyColName = table.primary_key.columns.values()[0].name

		unique_col_name = []

		# No Need to check unique column
		'''
		for constraint in sorted(table.constraints):
			if isinstance(constraint, UniqueConstraint):
				for col in constraint.columns:
					unique_col_name.append(col.name)
		'''

		for result in results:
			data = {}
			for column, value in result.items():
				if(column == primaryKeyColName):
					continue
				else:
					if(type(value) == str or type(value) == unicode) and str(table.columns[column].type) in ['CHAR', 'VARCHAR']:
						data.update({column: zg2uni(value)})
					# if(type(value) == str or type(value) == unicode) and (column not in unique_col_name) and str(table.columns[column].type) in ['CHAR', 'VARCHAR']:
						# data.update({column: zg2uni(value)})
			if data:
				# _logger.debug(data)
				update_rec = update(table).where(primaryKeyCol==result[primaryKeyColName])
				update_rec = update_rec.values(data)
				session.execute(update_rec)

	session.commit()
	session.close()

	sys.stdout.write("%d%% - Finished.\n" % (count * 100/table_count))
	sys.stdout.flush()


if __name__ == '__main__':

	f = Figlet(font='cybermedium')
	print(f.renderText('Zawgyi To Unicode Database Converter Tool.\n'))

	#print("Zawgyi To Unicode Database Converter Tool.\n\n")

	db_name = raw_input("Database name: ")
	db_route = raw_input("Database route: ")
	db_port = raw_input("Database port: ")
	user_name = raw_input("User name: ")
	password = getpass.getpass("Password: ")

	convert(db_route, db_name, db_port, user_name, password)
