import facebook
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.tokens.models import *
import time

debug_posts = True
debug_reactions = False
debug_comments = False

COMMENTS = 'comments'
REACTIONS = 'reactions'
POSTS = 'posts'
FINISHED = 'finished'

def debug(message):
    if debug_posts:
        print(message)
        
def getNewGraphApi(page_name):
    #return facebook.GraphAPI(getNewAccessToken(page_name))
    return facebook.GraphAPI(access_token=getNewAccessToken(page_name), version = 2.9)

def get_graph_object(page_name, query, amount_of_tries = 0):
    data = None
    if amount_of_tries > 3:
        debug('Max amount of retries on object: '+query)
        return None
    try:
        debug('Getting object: '+query)
        data = getNewGraphApi(page_name).get_object(query)
    except Exception as e:
        print(e)
        amount_of_tries += 1
        debug('Try: '+str(amount_of_tries)+'Error getting object: '+query)
        time.sleep(2**amount_of_tries)
        return get_graph_object(page_name, query, amount_of_tries)
    return data
    
def get_paged_query(paging, query):

    if paging is None:
        return query
    if paging == FINISHED:
        return False

    return query+'&after='+paging
    
def save_paging(model, model_name, paging_json):

    if paging_json:
        cursors_next = paging_json.get('cursors').get('after')
    else:
        cursors_next = FINISHED
        
    if model_name == COMMENTS:
        model.comment_paging = cursors_next
    if model_name == REACTIONS:
        model.reaction_paging = cursors_next
    if model_name ==  POSTS:
        model.post_paging = cursors_next
    
    model.save()


def get_item_and_paging(extracting_function, model, model_name, data):

    if data is None:
        return
    
    if type(data) is str:
        print('data is str',data,str(extracting_function),str(model),str(model_name))
    
    extracting_function(model, data.get('data'))
    save_paging(model,model_name, data.get('paging'))

    debug(str(len(data.get('data')))+' '+model_name+' saved for '+model.name)
