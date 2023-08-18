import json
from pprint import pprint
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    results=data.get('results')
    l=[]
    for i in results:
        l.append(i['email'])
    return l
f=open('randomuser_data.json','r')
data=json.loads(f.read())
pprint(get_email(data))   