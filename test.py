import unittest
from programacion import *

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.dict = {"items":[{"creation_date":4,"owner":{"reputation":0},"is_answered":True,"view_count":99},
        {"creation_date":0,"owner":{"reputation":1},"is_answered":True,"view_count":3},
        {"creation_date":1,"owner":{"reputation":2},"is_answered":True,"view_count":9999},
        {"creation_date":2,"owner":{"reputation":3},"is_answered":True,"view_count":15},
        {"creation_date":3,"owner":{"reputation":999},"is_answered":False,"view_count":79}]}

    def test_getNotAnsweredQuestions(self):
        self.assertEqual(len(getNotAnsweredQuestions(self.dict)),1)

    def test_getAnsweredQuestions(self):
        self.assertEqual(len(getAnsweredQuestions(self.dict)),4)

    def test_lessVisitedQuestion(self):
        self.assertEqual(lessVisitedQuestion(self.dict)['view_count'],3)

    def test_getOldestQuestion(self):
        self.assertEqual(getOldestQuestion(self.dict)['creation_date'],0)

    def test_getNewestQuestion(self):
        self.assertEqual(getNewestQuestion(self.dict)['creation_date'],4)

    def test_getHighestOwnerReputation(self):
        self.assertEqual(getOwnerHighestReputation(self.dict)['owner']['reputation'],999)
        