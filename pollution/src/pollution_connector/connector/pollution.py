from __future__ import absolute_import, annotations

from typing import Optional, List

from pollution_connector.connector.common import ODHBaseConnector
from pollution_connector.data_model.pollution import PollutionMeasure
from pollution_connector.data_model.traffic import TrafficSensorStation


class PollutionODHConnector(ODHBaseConnector[PollutionMeasure, TrafficSensorStation]):

    def __init__(self,
                 base_reader_url: str,
                 base_writer_url: str,
                 authentication_url: str,
                 username: Optional[str],
                 password: Optional[str],
                 client_id: Optional[str],
                 client_secret: Optional[str],
                 grant_type: List[str],
                 pagination_size: int,
                 max_post_batch_size: Optional[int],
                 requests_timeout: float,
                 requests_max_retries: int,
                 requests_sleep_time: float,
                 requests_retry_sleep_time: float) -> None:

        station_type = "TrafficSensor"
        measure_types = PollutionMeasure.get_pollution_data_types()
        measure_types = [measure_type.name for measure_type in measure_types]

        super().__init__(base_reader_url,
                         base_writer_url,
                         station_type,
                         measure_types,
                         authentication_url,
                         username,
                         password,
                         client_id,
                         client_secret,
                         grant_type,
                         pagination_size,
                         max_post_batch_size,
                         requests_timeout,
                         requests_max_retries,
                         requests_sleep_time,
                         requests_retry_sleep_time)

    @staticmethod
    def build_station(raw_station: dict) -> TrafficSensorStation:
        return TrafficSensorStation.from_odh_repr(raw_station)

    @staticmethod
    def build_measure(raw_measure: dict) -> PollutionMeasure:
        return PollutionMeasure.from_odh_repr(raw_measure)
