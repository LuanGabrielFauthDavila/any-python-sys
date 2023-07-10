# import bcrypt
import uuid as uid

# def gen_password(password):
#     hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
#     return hash.decode()

# def validate_password(password, hash):
#     return bcrypt.checkpw(password.encode(), hash.encode())

def gen_uuid():
    return uid.uuid4()

def verify_dict(data, requested_fields):
    errors = {}
    for field in requested_fields:
        if field not in data:
            errors[field] = f'Field {field} not informed'
    return errors