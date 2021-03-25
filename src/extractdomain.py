import constants


def domain_name():
    return """
{0}
```py
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
```
    """.format(constants.extractdomain.description_domain_name)
