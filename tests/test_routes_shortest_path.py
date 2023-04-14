
def test_route_shortest_path_pedestrian(client, url_prefix, steps_point, pedestrian_mode):
    response = client.get(url_prefix + f"path/shortest?mode={pedestrian_mode}"
                                       f"&step_point={steps_point[0]}&step_point={steps_point[-1]}")
    assert response.status_code == 200, response.json()
    output = response.json()
    assert len(output) > 1
    assert len(output[0]) == 2


def test_route_shortest_path_vehicle(client, url_prefix, steps_point, vehicle_mode):
    response = client.get(url_prefix + f"path/shortest?mode={vehicle_mode}"
                                       f"&step_point={steps_point[0]}&step_point={steps_point[-1]}")
    assert response.status_code == 200, response.json()
    output = response.json()
    assert len(output) > 1
    assert len(output[0]) == 2