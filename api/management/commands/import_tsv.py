import csv
from django.core.management.base import BaseCommand
from api.models import Movie
from datetime import datetime

class Command(BaseCommand):
	help = 'Imports data from a TSV file'

	def add_arguments(self, parser):
		parser.add_argument('file', type=str)

	def handle(self, *args, **options):
		with open(options['file'], 'r') as tsvfile:
			reader = csv.DictReader(tsvfile, delimiter='\t')
			for row in reader:
				if row['startYear'] != '\\N' and (len(row['primaryTitle']) < 150 and len(row['originalTitle']) < 150) and datetime.strptime(row['startYear'], '%Y') >= datetime.strptime('1970', '%Y') and row['titleType'] == 'movie' and row['genres'] != '\\N' and row['runtimeMinutes'] != '\\N' and row['isAdult'] != '1':
					movie = Movie(
						tconst=row['tconst'],
						titleType=row['titleType'],
						primaryTitle=row['primaryTitle'],
						originalTitle=row['originalTitle'],
						isAdult=row['isAdult'] == '1',
						startYear=datetime.strptime(row['startYear'], '%Y'),
						endYear=None if row['endYear'] == '\\N' else datetime.strptime(row['endYear'], '%Y'),
						runtimeMinutes=int(row['runtimeMinutes']) if row['runtimeMinutes'] != '\\N' else None,
						genres=row['genres'],
					)
					movie.save()

		self.stdout.write(self.style.SUCCESS('Successfully imported data'))

