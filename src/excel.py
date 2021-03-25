import constants


def excel():
    return """
{0}
```py
def parse(values, criteria):
    if type(criteria) in [int, float] or (type(criteria) is str and criteria[0] not in "<>"):
        return [item for item in values if item == criteria]

    rel = criteria.translate(None, "0123456789.")
    limit = float(criteria.translate(None, "<>="))

    if   rel == "<>":
        return [item for item in values if item <> limit]
    elif rel == "<=":
        return [item for item in values if item <= limit]
    elif rel == ">=":
        return [item for item in values if item >= limit]
    elif rel == "<":
        return [item for item in values if item < limit]
    elif rel == ">":
        return [item for item in values if item > limit]


def count_if(values, criteria):
    return len(parse(values, criteria))


def sum_if(values, criteria):
    return sum(parse(values, criteria))


def average_if(values, criteria):
    return sum(parse(values, criteria)) * 1.0 / len(parse(values, criteria))
```
""".format(constants.excel.description_excel)


def countif():
    return """
{0}
```py
def parse(values, criteria):
    if type(criteria) in [int, float] or (type(criteria) is str and criteria[0] not in "<>"):
        return [item for item in values if item == criteria]

    rel = criteria.translate(None, "0123456789.")
    limit = float(criteria.translate(None, "<>="))

    if   rel == "<>":
        return [item for item in values if item <> limit]
    elif rel == "<=":
        return [item for item in values if item <= limit]
    elif rel == ">=":
        return [item for item in values if item >= limit]
    elif rel == "<":
        return [item for item in values if item < limit]
    elif rel == ">":
        return [item for item in values if item > limit]


def count_if(values, criteria):
    return len(parse(values, criteria))
```
""".format(constants.excel.description_countif)


def sumif():
    return """
{0}
```py
def parse(values, criteria):
    if type(criteria) in [int, float] or (type(criteria) is str and criteria[0] not in "<>"):
        return [item for item in values if item == criteria]

    rel = criteria.translate(None, "0123456789.")
    limit = float(criteria.translate(None, "<>="))

    if   rel == "<>":
        return [item for item in values if item <> limit]
    elif rel == "<=":
        return [item for item in values if item <= limit]
    elif rel == ">=":
        return [item for item in values if item >= limit]
    elif rel == "<":
        return [item for item in values if item < limit]
    elif rel == ">":
        return [item for item in values if item > limit]



def sum_if(values, criteria):
    return sum(parse(values, criteria))
```
    """.format(constants.excel.description_sumif)


def averageif():
    return """
{0}
```py
def parse(values, criteria):
    if type(criteria) in [int, float] or (type(criteria) is str and criteria[0] not in "<>"):
        return [item for item in values if item == criteria]

    rel = criteria.translate(None, "0123456789.")
    limit = float(criteria.translate(None, "<>="))

    if   rel == "<>":
        return [item for item in values if item <> limit]
    elif rel == "<=":
        return [item for item in values if item <= limit]
    elif rel == ">=":
        return [item for item in values if item >= limit]
    elif rel == "<":
        return [item for item in values if item < limit]
    elif rel == ">":
        return [item for item in values if item > limit]


def count_if(values, criteria):
    return len(parse(values, criteria))


def sum_if(values, criteria):
    return sum(parse(values, criteria))


def average_if(values, criteria):
    return sum(parse(values, criteria)) * 1.0 / len(parse(values, criteria))
```
""".format(constants.excel.description_averageif)
