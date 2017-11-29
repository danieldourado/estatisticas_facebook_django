import facebook
from pages.models import *

def getPageInfo(page):
    
    graph = facebook.GraphAPI(page.access_token)
    raw_json = graph.get_object(page.name)
    print (raw_json)
    
    page.pretty_name = raw_json['name']
    page.id = raw_json['id']


def getPageInsights(args):

    pagename = Page.objects.get(id=args['id'])

    #token = 'EAACEdEose0cBAD6KsQvpVng9vUXf2xzVVTZAX2BwoX3bpRRg9RIfZAg88V3ZBT3P8nrDdiND9TuqN6E4fUhI27WOeATc8ZCRXFttxWt4dFrZCweSJg5Qx0ZCtaRLRa93HDuyZADKDRkb95DqOtbsqXmOMhaoZBbj0qQXgXw7hlZC7I4n37u1m7eKkimGThgWBtNIZD'
    token = args['access_token']
    graph = facebook.GraphAPI(token)
    since = args['since']
    raw_json = graph.get_object(pagename.name+'/insights?period=day&metric=page_fan_adds_unique,page_impressions_unique,page_engaged_users,page_stories,page_storytellers&since='+str(since))
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
