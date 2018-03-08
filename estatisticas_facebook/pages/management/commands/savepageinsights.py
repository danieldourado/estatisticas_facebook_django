from django.core.management.base import BaseCommand, CommandError
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.posts.models import getPostInfo
from estatisticas_facebook.comments.models import getCommentInfo
from estatisticas_facebook.reactions.models import getReactionInfo


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
        page_model = Page.objects.get(id__iexact=args['id'])
        getPostInfo(page_model,args['since'])
        getCommentInfo(page_model)
        getReactionInfo(page_model)