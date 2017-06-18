import requests

session = requests.Session()
session.auth = ('sg0958026', 'Nh#zxq88qh')
#url =('https://sonar.sabre.com/api/authentication/validate')
#session.get(url)
def get_session():
    return session


#def login_session():
#    session.get(url)
#    return session

