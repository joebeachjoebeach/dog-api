from .utils import _get


def master_breeds():
    """Gets all breeds, not including sub-breeds. Returns a list of breed names."""
    return _get('breeds/list')
    

def all_breeds():
    """Gets all breeds, including sub-breeds. Returns a dictionary."""
    return _get('breeds/list/all')
    
    
def subbreeds(breed):
    """Gets the list of sub-breeds from the chosen breed. Returns a list of sub-breeds."""
    if not isinstance(breed, str):
        raise TypeError('you must input the breed as a string')
    return _get('breed/{0}/list'.format(breed))
    

def random_image(breed=None, subbreed=None):
    """Gets a random dog image. Returns a url as a string"""
    if breed == None and subbreed == None:
        return _get('breeds/image/random')
    elif subbreed == None:
        return _get('breed/{0}/images/random'.format(breed))
    else:
        return _get('breed/{0}/{1}/images/random'.format(breed, subbreed))
    
    
def all_images(breed, subbreed=None):
    """Gets all images from the provided breed/subbreed. Returns a list of urls."""
    if not isinstance(breed, str):
        raise TypeError('breed must be a string')
    if subbreed == None:
        return _get('breed/{0}/images'.format(breed))
    else:
        if not isinstance(subbreed, str):
            raise TypeError('subbreed must be a string')
        return _get('breed/{0}/{1}/images'.format(breed, subbreed))
        