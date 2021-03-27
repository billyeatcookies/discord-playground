def to_camel_case(s):
    return s[0] + s.title().translate(str.maketrans('','',"-_"))[1:] if s else s
