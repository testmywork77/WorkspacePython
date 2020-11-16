def addStudentPayload(sid):
    body = {
        "id": sid,
        "name": "name"+str(sid),
        "email": "name"+str(sid)+"@gmail.com",
        "programme": "programme"+str(sid),
        "languages": [
            "lang1",
            "lang2"
        ]
    }
    return body
