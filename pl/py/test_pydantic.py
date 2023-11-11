from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "BBQ"
    signup_ts: Optional[datetime] = None
    friends: list[int] = []


external_data = {
    "id": "123",
    # 'name': 'xxx',
    "signup_ts": "2021-09-02 17:00",
    "friends": [1, 2, "3"],
}
user = User(**external_data)

print(user.id)
# > 123
print(repr(user.signup_ts))
# > datetime.datetime(2021, 9, 2, 17, 0)
print(user.friends)
# > [1, 2, 3]
print(user.model_dump())

print(user.schema(), type(user.schema()))
# print(user.schema_json(), type(user.schema_json()))

"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2021, 9, 2, 17, 0),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
