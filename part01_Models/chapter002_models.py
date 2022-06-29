from devtools import debug
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


user = User(id='123')

debug(user)

assert user.id == 123
assert user.name == 'Jane Doe'
assert user.__fields_set__ == {'id'}

debug(user.__fields_set__)

assert user.dict() == dict(user) == {'id': 123, 'name': 'Jane Doe'}

user.id = 321
assert user.id == 321
