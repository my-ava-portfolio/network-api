from typing import List

import pytest
from litestar.testing import TestClient

from app import app
from network_api.config import settings


@pytest.fixture
def url_prefix():
    return f"{settings.API_PREFIX}/"


@pytest.fixture()
def steps_point_2_nodes() -> List[str]:
    return ["POINT(4.0793058 46.0350304)", "POINT(4.0725246 46.0397676)"]


@pytest.fixture()
def steps_point_3_nodes() -> List[str]:
    return ["POINT(4.0793058 46.0350304)", "POINT(4.0725246 46.0397676)", "POINT(4.0793058 46.0350304)"]


@pytest.fixture()
def pedestrian_mode() -> str:
    return "pedestrian"


@pytest.fixture()
def vehicle_mode() -> str:
    return "vehicle"


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
