# Fix Spelling and Grammar with Python
# pip install gingerit
from gingerit.gingerit import GingerIt


def fix_grammar(text):
    ginger = GingerIt()
    correction = ginger.parse(text)
    return correction


fix_grammar("he fliwers is very good")
