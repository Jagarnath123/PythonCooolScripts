# Fix Spelling and Grammar with Python
# pip install gingerit
from gingerit.gingerit import GingerIt
def Fix_Grammar(text):
    ginger = GingerIt()
    correction = ginger.parse(text)
    return correction
Fix_Grammer("The fliwers is very good")