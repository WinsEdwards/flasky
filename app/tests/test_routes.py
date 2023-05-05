def test_read_all_crystals_returns_empty_list(client):
    # arrange

    # act
    response = client.get("/crystals")
    response_body = response.get_json()
    
    # assert
    assert response_body == []
    assert response.status_code == 200

def test_read_crytal_by_id(client, make_two_crystals):
    # arrange

    # act
    response = client.get("/crystals/2")
    response_body = response.get_json()
    
    # assert
    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "garnet",
        "color": "red",
        "powers": "awesomeness"
    }

def test_create_crystal(client):
    response = client.post("/crystals", json={
        "name": "tiger's eye",
        "color": "golden brown",
        "powers": "focus the mind, promoting mental clarity, assisting us to resolve problems objectively"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Crystal tiger's eye successfully created!"