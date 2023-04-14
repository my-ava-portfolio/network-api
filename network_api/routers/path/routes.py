from typing import List, Tuple

from osmrx.main.roads import GraphAnalysis
from shapely.wkt import loads
from starlite import Controller, get, Router


class ShortestPathController(Controller):

    @get("/shortest",
         operation_id="shortest path",
         summary="Compute a shortest path from wkt points (2 at least)",
         response_description="Returns a list of coordinates based on the shortest path found"
         )
    async def get_shortest_path(self, mode: str, step_point: List[str]) -> List[Tuple[float, float]]:
        """Compute a shortest path from wkt point"""
        roads_object = GraphAnalysis(mode, list(map(lambda coords: loads(coords), step_point)))
        paths_found = roads_object.get_shortest_path()
        return list(paths_found)[0].path.coords[:]


router = Router(
    path="/path",
    tags=["path"],
    route_handlers=[ShortestPathController],
    dependencies={}
)



