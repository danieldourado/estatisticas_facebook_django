import facebook
import urllib.request, json
from pages.models import *
from estatisticas_facebook.tokens.models import *

    
def getLatestSavedToken():
    access_token = Token.objects.filter().order_by('-id')[0]
    return access_token    

def getShortLivedAccessToken(page_name):
    access_token = getLatestSavedToken()
    graph = facebook.GraphAPI(getLatestSavedToken())
    raw_json = graph.get_object(page_name+"?fields=access_token")    
    new_access_token = raw_json['access_token']
    return new_access_token

def makeAccessTokenLongLived(short_lived_access_token):
    url = 'https://graph.facebook.com/oauth/access_token?client_id=571058086572175&client_secret=c3cc91d289a9869e74f6907c9cc68909&grant_type=fb_exchange_token&fb_exchange_token='
    with urllib.request.urlopen(url+short_lived_access_token) as url:
        data = json.loads(url.read().decode())
        return data['access_token']
    
def saveAccessToken(access_token):
    new_token = Token(name=access_token)
    new_token.save()

def getNewAccessToken(page_name):
    access_token = makeAccessTokenLongLived(getShortLivedAccessToken(page_name))
    saveAccessToken(access_token)
    return access_token
    
def getNewGraphApi(page_name):
    return facebook.GraphAPI(getNewAccessToken(page_name))

def getPageInfo(page):
    raw_json = getNewGraphApi(page.name).get_object(page.name)
    print (raw_json)
    
    page.pretty_name = raw_json['name']
    page.id = raw_json['id']

def getPageInsights(args):

    since = args['since']
    raw_json = getNewGraphApi(args['id']).get_object(args['id']+'/insights?period=day&metric=page_fan_adds_unique,page_impressions_unique,page_engaged_users,page_stories,page_storytellers&since='+str(since))
    
    pagedata = raw_json['data']

    for obj in pagedata:
        print (obj['name'])
        for value in obj['values']:
            page_insights = PageInsights(
                name=obj['name'], 
                period=obj['period'], 
                title=obj['title'], 
                description=obj['description'], 
                end_time=value['end_time'], 
                value=value['value'], 
                page_id=args['id'])
            page_insights.save()

def getPosts(args):
    return