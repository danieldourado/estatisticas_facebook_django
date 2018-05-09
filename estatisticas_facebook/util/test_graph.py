from django.test import TestCase
from estatisticas_facebook.util.graph import *

class TestGraph(TestCase):
    
    def setUp(self):
        pass
    
    def test_get_graph_object(self):
        get_paged_query('nonsense', 'nonsense')