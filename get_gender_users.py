import json
def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    results=data.get('results')
    l=[]
    for i in results:
        l.append(i['gender'])
    return l
f=open('data.json', 'r')
data=json.loads(f.read())

print(get_gender_users(data))      