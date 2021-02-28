from utilities.configurations import *


def userPayload():
    user_dict = {
        "name": "venkata",
        "job": "developer"
    }
    return user_dict


def userPayloadFromFeature(name, job):
    user_dict = {
        "name": name,
        "job": job
    }
    return user_dict


def buildPayloadFromMySQL(query):
    user_dict = {}
    row = getQuery(query)
    user_dict['name'] = row[0]
    user_dict['job'] = row[1]
    return user_dict
