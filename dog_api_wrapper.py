import requests

base_url = 'https://dog.ceo/api/'

def _get(resource):
  """Sends a GET request to the provided url and returns the 'message' data if it exists."""
  url = '{0}{1}'.format(base_url, resource)
  res = requests.get(url)
  if res.status_code == 200:
    return res.json()['message']
  else:
    return res

def get_master_breeds():
  """Gets all breeds, not including sub-breeds. Returns an array of breed names."""
  return _get('breeds/list')
    

def get_all_breeds():
  """Gets all breeds, including sub-breeds. Returns a JSON object."""
  return _get('breeds/list/all')
    

def get_random_image():
  """Gets a random dog image. Returns a url as a string"""
  return _get('breeds/image/random')
    

def get_all_images_from_breed(breed):
  """Gets a list of all the images for the chosen breed. Returns an array of urls as strings."""
  if not isinstance(breed, str):
    raise TypeError('you must input the breed as a string')
  return _get('breed/{0}/images'.format(breed))
  

def get_random_image_from_breed(breed):
  """Gets a random image for the chosen breed. Returns a url as a string."""
  if not isinstance(breed, str):
    raise TypeError('you must input the breed as a string')
  return _get('breed/{0}/images/random'.format(breed))


def get_subbreeds_from_breed(breed):
  """Gets the list of sub-breeds from the chosen breed. Returns an array of sub-breeds."""
  if not isinstance(breed, str):
    raise TypeError('you must input the breed as a string')
  return _get('breed/{0}/list'.format(breed))
    
    
def get_all_images_from_subbreed(breed, subbreed):
  """Gets a list of all images of the chosen sub-breed. Returns an array of urls as strings."""
  if not isinstance(breed, str) or not isinstance(subbreed, str):
    raise TypeError('you must input the breed and subbreed as a string')
  return _get('breed/{0}/{1}/images'.format(breed, subbreed))
    

def get_random_image_from_subbreed(breed, subbreed):
  """Gets a random image of the chosen sub-breed. Returns a url as a string."""
  if not isinstance(breed, str) or not isinstance(subbreed, str):
    raise TypeError('you must input the breed and subbreed as a string')
  return _get('breed/{0}/{1}/images/random'.format(breed, subbreed))


