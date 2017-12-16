from pages.models import *
from util.graph import * 

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