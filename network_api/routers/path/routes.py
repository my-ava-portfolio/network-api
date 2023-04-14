from typing import List, Tuple

from osmrx.main.roads import GraphAnalysis
from shapely.wkt import loads
from starlite import Controller, get, Router


class ShortestPathController(Controller):

    @get("/shortest", dependencies={})
    async def get_shortest_path(self, mode: str, step_point: List[str]) -> List[Tuple[float, float]]:
        roads_object = GraphAnalysis(mode, list(map(lambda coords: loads(coords), step_point)))
        paths_found = roads_object.get_shortest_path()
        return list(paths_found)[0].path.coords[:]


router = Router(
    path="/path",
    route_handlers=[ShortestPathController],
    dependencies={}
)



