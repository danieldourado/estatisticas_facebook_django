import facebook
from pages.models import *
from estatisticas_facebook.tokens.models import *
def getNewGraphApi(page_name):
    return facebook.GraphAPI(getNewAccessToken(page_name))
