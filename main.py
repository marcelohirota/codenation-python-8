import jwt


def create_token(data, secret):
    return jwt.encode(payload=data, key=secret, algorithm='HS256')


def verify_signature(token):
    try:
        return jwt.decode(jwt=token, key='acelera', algorithms='HS256')

    except:
        return {"error": 2}


token = create_token({"language": "Python"}, 'acelera')

print(token)
