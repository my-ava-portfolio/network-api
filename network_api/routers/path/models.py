from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from portfolio.core.global_values import ActivityStatus, ActivityTypes, ActivityContracts


@dataclass
class PublicationFeature:
    year: int
    editor: str
    publication: str


@dataclass
class TrainingFeature:
    year: int
    editor: str
    publication: str


@dataclass
class ActivitiesModel:
    uid: str
    id: str
    color: str | None
    no: str
    type: ActivityTypes
    name: str
    long_name: str | None
    contract: ActivityContracts
    status: ActivityStatus
    title: str
    start_date: datetime
    end_date: datetime
    keywords: Dict[str, str] | None
    years: int
    months: int
    company: str
    img_activity: str | None
    location: str
    presentation: str | None
    description: Dict | None
    url_github: str | None
    url_blog: str | None
    recommendations: Dict | None
    medias_found: bool
    publications: List[PublicationFeature] | List
    trainings: List[TrainingFeature] | List


@dataclass
class ActivitiesDurationModel:
    years: int
    months: int


@dataclass
class ActivitiesCount:
    type: ActivityTypes
    count: int


@dataclass
class ActivitiesValidityRangeModel:
    start_date: int
    end_date: int
