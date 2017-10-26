import dog

def test_get_master_breeds():
  """Tests a call to get all master breeds."""
  res = dog.get_master_breeds()
  assert isinstance(res, list), "The response should be a list."


def test_get_all_breeds():
  """Tests a call to get all breeds."""
  res = dog.get_all_breeds()
  assert isinstance(res, dict), "The response should be a dictionary."


def test_get_random_image():
  """Tests a call to get a random image."""
  res = dog.get_random_image()
  assert isinstance(res, str), "The response should be a string."
  assert res[0:4] == 'http', "The response should begin with 'http'"
  
  
def test_get_all_images_from_breed():
  breed = 'poodle'
  res = dog.get_all_images_from_breed(breed)
  assert isinstance(res, list), "The response should be a list."
  for item in res:
    assert isinstance(item, str), "Each item in the list should be a string."
    assert item[0:4] == 'http', "Each string should begin with 'http'"
      

def test_get_random_image_from_breed():
  breed = 'poodle'
  res = dog.get_random_image_from_breed(breed)
  assert isinstance(res, str), "The response should be a string."
  assert res[0:4] == 'http', "The response should begin with 'http'"
  
  
def test_get_subbreeds_from_breed():
  breed = 'retriever'
  res = dog.get_subbreeds_from_breed(breed)
  assert isinstance(res, list), "The response should be a list."
  
  
def test_get_all_images_from_subbreed():
  breed = 'retriever'
  subbreed = 'golden'
  res = dog.get_all_images_from_subbreed(breed, subbreed)
  assert isinstance(res, list), "The response should be a list."
  
  
def test_get_random_image_from_subbreed():
  breed = 'retriever'
  subbreed = 'golden'
  res = dog.get_random_image_from_subbreed(breed, subbreed)
  assert isinstance(res, str), "The response should be a string."
  assert res[0:4] == 'http', "The response should begin with 'http'"
  
