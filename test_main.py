from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

# Test Home Endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


# Test POST: Create Ticket
def test_create_ticket():
    response = client.post("/ticket", json={
        "id": 1,
        "flight_name": "Air Bangladesh",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "Air Bangladesh",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    }


# Test GET: Get All Tickets
def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert isinstance(response.json(), list)   
    assert len(response.json()) > 0            


# Test PUT: Update Ticket
def test_update_ticket():
    response = client.put("/ticket/1", json={
        "id": 1,
        "flight_name": "Air India",
        "flight_date": "2025-10-20",
        "flight_time": "16:00",
        "destination": "Kolkata"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "Air India",
        "flight_date": "2025-10-20",
        "flight_time": "16:00",
        "destination": "Kolkata"
    }


# Test DELETE: Delete Ticket
def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "Air India",
        "flight_date": "2025-10-20",
        "flight_time": "16:00",
        "destination": "Kolkata"
    }
