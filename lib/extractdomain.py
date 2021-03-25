import re


def domain_name(url):
    """
    When given a URL as a string, parses out just the domain name and returns it as a string.
    """
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
