## Dog API Wrapper for Python
A Python wrapper for the [Dog API](https://dog.ceo/dog-api)

### Usage

**Import the module:**
```python
import dog
```

**Get a list of all the main breeds:**
```python
dog.master_breeds()
```

**Get a list of all breeds, including sub-breeds:**
```python
dog.all_breeds()
```

**Get a list of the sub-breeds of a particular breed:**
```python
# dog.subbreeds({breed})
dog.subbreeds('hound')
```

**Get a random image url:**
```python
# from any breed
dog.random_image()

# from a particular breed  -->  dog.random_image({breed})
dog.random_image('retriever')

# from a particular sub-breed  -->  dog.random_image({breed}, {sub-breed})
dog.random_image('terrier', 'australian')
```

**Get a list of all the image urls:**
```python
# for a particular breed  -->  dog.all_images({breed})
dog.all_images('poodle')

# for a particular sub-breed  -->  dog.all_images({breed}, {sub-breed})
dog.all_images('spaniel', 'japanese')
```

---
---

### Contributing
PR's welcome!

**Getting started**
1. Clone or download the repo
2. Install the Python dependencies: `pipenv install`
3. Activate the virtual environment: `pipenv shell`

**Running tests**

* `py.test` will work ideally, but if not:
* `PYTHONPATH=. py.test` ought to do the trick
