#!/usr/bin/python3
import requests

def getJSON(api_endpoint):
    response = requests.get(url=api_endpoint)
    return response.json()


def getNotAnsweredQuestions(data):
    return list(filter(lambda x:not x['is_answered'], data['items']))


def getAnsweredQuestions(data):
    return list(filter(lambda x:x['is_answered'], data['items']))

if __name__ == "__main__":
    url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data = getJSON(url)
    answeredQuestions = getAnsweredQuestions(data)
    print("The amount of answered questions is: \n" + str(len(answeredQuestions)))
    notAnsweredQuestions = getNotAnsweredQuestions(data)
    print("The amount of NOT answered questions is: \n" + str(len(notAnsweredQuestions)))
    