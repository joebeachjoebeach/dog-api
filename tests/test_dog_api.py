import dog_api as dog

def test_master_breeds():
    """Tests a call to get all master breeds."""
    res = dog.master_breeds()
    assert isinstance(res, list), "The response should be a list."


def test_all_breeds():
    """Tests a call to get all breeds."""
    res = dog.all_breeds()
    assert isinstance(res, dict), "The response should be a dictionary."


def test_subbreeds():
    breed = 'retriever'
    res = dog.subbreeds(breed)
    assert isinstance(res, list), "The response should be a list."


def test_random_image__all():
    """Tests a call to get a random image."""
    res = dog.random_image()
    assert isinstance(res, str), "The response should be a string."
    assert res[0:4] == 'http', "The response should begin with 'http'"


def test_random_image__breed():
    breed = 'poodle'
    res = dog.random_image(breed)
    assert isinstance(res, str), "The response should be a string."
    assert res[0:4] == 'http', "The response should begin with 'http'"
  
  
def test_random_image__subbreed():
    breed = 'retriever'
    subbreed = 'golden'
    res = dog.random_image(breed, subbreed)
    assert isinstance(res, str), "The response should be a string."
    assert res[0:4] == 'http', "The response should begin with 'http'"
  
  
def test_all_images__breed():
    breed = 'poodle'
    res = dog.all_images(breed)
    assert isinstance(res, list), "The response should be a list."
    for item in res:
        assert isinstance(item, str), "Each item in the list should be a string."
        assert item[0:4] == 'http', "Each string should begin with 'http'"
      

def test_all_images__subbreed():
    breed = 'retriever'
    subbreed = 'golden'
    res = dog.all_images(breed, subbreed)
    assert isinstance(res, list), "The response should be a list."
  