from shapely import LineString
from shapely.wkt import loads


def test_route_shortest_path_pedestrian(client, url_prefix, steps_point_2_nodes, pedestrian_mode):
    response = client.get(url_prefix + f"path/shortest?mode={pedestrian_mode}"
                                       f"&step_point={steps_point_2_nodes[0]}&step_point={steps_point_2_nodes[-1]}")
    assert response.status_code == 200, response.json()
    output = response.json()
    assert len(output) == 1
    for path in output:
        geom = loads(path)
        assert isinstance(geom, LineString)
        assert geom.length > 0


def test_route_shortest_path_vehicle(client, url_prefix, steps_point_2_nodes, vehicle_mode):
    response = client.get(url_prefix + f"path/shortest?mode={vehicle_mode}"
                                       f"&step_point={steps_point_2_nodes[0]}&step_point={steps_point_2_nodes[-1]}")
    assert response.status_code == 200, response.json()
    output = response.json()
    assert len(output) == 1
    for path in output:
        geom = loads(path)
        assert isinstance(geom, LineString)
        assert geom.length > 0


def test_route_shortest_path_vehicle_with_3_points(client, url_prefix, steps_point_3_nodes, vehicle_mode):
    response = client.get(url_prefix + f"path/shortest?mode={vehicle_mode}"
                                       f"&step_point={steps_point_3_nodes[0]}&step_point={steps_point_3_nodes[1]}"
                                       f"&step_point={steps_point_3_nodes[-1]}")
    assert response.status_code == 200, response.json()
    output = response.json()
    assert len(output) == 2
    for path in output:
        geom = loads(path)
        assert isinstance(geom, LineString)
        assert geom.length > 0
