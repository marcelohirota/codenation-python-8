import jwt


def create_token(data, secret):
    return jwt.encode(payload=data, key=secret)


def verify_signature(token):
    try:
        return jwt.decode(jwt=token, key='acelera')

    except:
        return {"error": 2}
