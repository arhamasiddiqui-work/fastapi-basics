from fastapi.testclient import TestClient
from main import app

client=TestClient(app)     # api ko test karne ke liye

#   Test Home api
def test_Home():
    response=client.get("/")
    # checking status code
    assert response.status_code==200 # assert: check for expected result
    # reponse data
    assert response.json() == {
        "message":"Testing API"
        }

# Test Add api
def test_Add():
    response=client.get("/add?a=5&b=5")
    # checking status code
    assert response.status_code==200
    # response data
    assert response.json()=={
        "result":10
    }