import requests

base_url = 'https://dog.ceo/api/'

def _get(resource):
    """Sends a GET request to the provided resource and returns the 'message' data if it exists."""
    url = '{0}{1}'.format(base_url, resource)
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['message']
    else:
        return res
    