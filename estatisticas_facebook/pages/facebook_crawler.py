import facebook

def getPageInfo(page):
    
    graph = facebook.GraphAPI(page.access_token)

    raw_json = graph.get_object(page.name)
    
    page.pretty_name = raw_json['name']
    page.save()    
    print (raw_json)