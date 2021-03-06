from typing import Any, Optional
from xml.etree.ElementTree import fromstring

from devtools import debug
from pydantic import BaseModel
from pydantic.utils import GetterDict

xmlstring = """
<User Id="2138">
    <FirstName />
    <LoggedIn Value="true" />
</User>
"""


class UserGetter(GetterDict):

    def get(self, key: str, default: Any) -> Any:

        # element attributes
        if key in {'Id', 'Status'}:
            return self._obj.attrib.get(key, default)

        # element children
        else:
            try:
                return self._obj.find(key).attrib['Value']
            except (AttributeError, KeyError):
                return default


class User(BaseModel):
    Id: int
    Status: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    LoggedIn: bool

    class Config:
        orm_mode = True
        getter_dict = UserGetter


debug(fromstring(xmlstring))

user = User.from_orm(fromstring(xmlstring))

debug(user)
