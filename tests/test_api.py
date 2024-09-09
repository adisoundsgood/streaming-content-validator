import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/content"

def test_content_api_status_code():
    """Test if API returns status code 200"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_content_structure():
    """Test if the returned content has the correct structure"""
    response = requests.get(BASE_URL)
    content = response.json()

    # Check if content is a list
    assert isinstance(content, list)
    
    # Check the structure of the first item
    for item in content:
        assert "id" in item
        assert "title" in item
        assert "genre" in item
        assert "episodes" in item

def test_content_data_type():
    """Test if the content fields have the correct data types"""
    response = requests.get(BASE_URL)
    content = response.json()

    for item in content:
        assert isinstance(item['id'], int)
        assert isinstance(item['title'], str)
        assert isinstance(item['genre'], str)
        assert isinstance(item['episodes'], int)