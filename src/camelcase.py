import constants


def to_camel_case():
    return """
{0}
```py
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
```
    """.format(constants.camelcase.description_camelcase)
