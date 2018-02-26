from django.core.management.base import BaseCommand, CommandError
from estatisticas_facebook.pages.models import *

class Command(BaseCommand):
    help = 'Save page insights'

    def add_arguments(self, parser):

        parser.add_argument(
                    '--since',
                    dest='since',
                    help='Date to extract ',
                )

    def handle(self, *args, **options):
        print('Extraindo Page insights a partir de: '+str(options['since']))
        
        args = {}
        args['since'] = str(options['since'])
        args['id'] = '316136345150243'
        getPageInsights(args)
        