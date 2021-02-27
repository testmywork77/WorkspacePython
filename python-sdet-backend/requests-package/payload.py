def addUserPayload():
    user_dict = {
        "name": "venkata",
        "job": "developer"
    }
    return user_dict


def addBookPayload(isbn):
    book_dict = {
        "name": "",
        "isbn": "",
        "aisle": "",
        "author": ""
    }
    return book_dict


def buildPayloadFromDB():
    addBody = {}
    addBody['name'] = ''
    addBody['isbn'] = ''
    addBody['aisle'] = ''
    addBody['author'] = ''

    return addBody
