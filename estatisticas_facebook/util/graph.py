import facebook
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.tokens.models import *

debug_posts = False
debug_reactions = False
debug_comments = False
FINISHED = 'finished'

def getNewGraphApi(page_name):
    return facebook.GraphAPI(getNewAccessToken(page_name))

def get_paged_query(paging, query):

    if paging is None:
        return query
    if paging == FINISHED:
        return False

    return query+'&after='+paging
    
    
def debug(message):
    if debug_posts:
        print(message)