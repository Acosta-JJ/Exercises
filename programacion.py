#!/usr/bin/python3
import requests

def getJSON(api_endpoint):
    response = requests.get(url=api_endpoint)
    return response.json()


def getNotAnsweredQuestions(data):
    return list(filter(lambda x:not x['is_answered'], data['items']))


def getAnsweredQuestions(data):
    return list(filter(lambda x:x['is_answered'], data['items']))


def lessVisitedQuestion(data):
    return min(data['items'], key=lambda x:x['view_count'])


def getOldestQuestion(data):
    return min(data['items'], key=lambda x:x['creation_date'])


def getNewestQuestion(data):
    return max(data['items'], key=lambda x:x['creation_date'])


def getOwnerHighestReputation(data):
    return max(data['items'], key=lambda x:x['owner']['reputation'] )

if __name__ == "__main__":
    url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data = getJSON(url)
    answeredQuestions = getAnsweredQuestions(data)
    print("The amount of answered questions is: " + str(len(answeredQuestions)))
    notAnsweredQuestions = getNotAnsweredQuestions(data)
    print("The amount of NOT answered questions is: " + str(len(notAnsweredQuestions)))
    lessVisited = lessVisitedQuestion(data)
    print("The least visited question has this visits: " + str(lessVisited['view_count']))
    oldestQuestion = getOldestQuestion(data)
    print("The oldest question has this tittle: " + oldestQuestion['title'])
    newestQuestion = getNewestQuestion(data)
    print("The newest question has this tittle: " + newestQuestion['title'])
    ownerHighestReputation = getOwnerHighestReputation(data)
    print("The owner with high reputation is: " + ownerHighestReputation['owner']['display_name'] + " and the reputation score is: "+ str(ownerHighestReputation['owner']['reputation']))

