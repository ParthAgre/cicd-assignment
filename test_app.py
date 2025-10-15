from app import app

def test_hello_world_endpoint():
    """
    Tests the main endpoint of the application.
    It checks for a successful response and the correct content.
    """
    # Create a test client to make requests to the app
    with app.test_client() as client:
        # Send a GET request to the root URL
        response = client.get('/')
        
        # Assert that the HTTP status code is 200 (OK)
        assert response.status_code == 200
        
        # Assert that the response contains our expected message
        assert b"Hi! The CI/CD pipeline is working!" in response.data