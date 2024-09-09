import pytest
#import requests
from app import app 

# BASE_URL = "http://127.0.0.1:5000/api/content"

@pytest.fixture
def client():
  """PyTest fixture to set up the Flask test client."""
  app.testing = True
  with app.test_client() as client:
    yield client

def test_content_api_status_code(client):
  """Test if API returns status code 200"""
  response = client.get('/api/content') # Use Flask's test client instead of requests
  assert response.status_code == 200

def test_content_structure(client):
  """Test if the returned content has the correct structure"""
  response = client.get('/api/content')
  content = response.get_json() # Use get_json() to parse the response as JSON

  # Check if content is a list
  assert isinstance(content, list)
  
  # Check the structure of the first item
  for item in content:
    assert "id" in item
    assert "title" in item
    assert "genre" in item
    assert "episodes" in item

def test_content_data_type(client):
  """Test if the content fields have the correct data types"""
  response = client.get('/api/content')
  content = response.get_json()

  for item in content:
    assert isinstance(item['id'], int)
    assert isinstance(item['title'], str)
    assert isinstance(item['genre'], str)
    assert isinstance(item['episodes'], int)