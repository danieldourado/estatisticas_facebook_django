import facebook
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.tokens.models import *

debug_posts = False
debug_reactions = False
debug_comments = False

def getNewGraphApi(page_name):
    return facebook.GraphAPI(getNewAccessToken(page_name))

def get_paging_query(model):
    return 
    "https://graph.facebook.com/v2.11/316136345150243_1487629434667589/reactions?access_token=EAAIHX9JlcI8BAJg1MxqPGVJis03wtzt0cyxSwMdU63avyKoX6ZAHyYGQbnUbX3NSDfXZCpj35GUfAHMsF5CYu2MbC2valQSbnRZCQMwbQ8ifZAPa6VZBxVtYcneBWIjZAK8syT06ADfReMZBhIi6p8ZAk7Wdk83oqJn6Da8bpjnxPMQ7ZBcUgMhCIetGJ1I3CKwZBoHFqLJlOsZCAZDZD&pretty=false&limit=25&after=TVRBd01EQXhOak0zTlRFek1qVXdPakUxTVRNNU9ETTVNamM2TWpVME1EazJNVFl4TXc9PQZDZD"

def debug(message):
    if debug_posts:
        print(message)