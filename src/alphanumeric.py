import constants


def alphanumeric():
    return """
{0}
```py
import re
def alphanumeric(string):
    return bool(re.match(r'^[A-Za-z0-9]+$', string))
```
    """.format(constants.alphanumeric.description_alphanumeric)