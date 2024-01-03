import os
import logging
import dataclasses
from typing import Optional

import yaml

from pyfivetran.client import FivetranClient

logging.basicConfig(level=logging.INFO)
lger = logging.getLogger(__name__)

# create a dataclass of the dsl representation of a connector in yaml


@dataclasses.dataclass
class Connector:
    group_id: str
    service: str

    trust_certificates: Optional[bool] = None
    trust_fingerprints: Optional[bool] = None
    run_setup_tests: Optional[bool] = None
    paused: Optional[bool] = None
    pause_after_trial: Optional[bool] = None
    sync_frequency: Optional[int] = None

    # define class method factory to convert from yaml to dataclass
    @classmethod
    def from_yaml(cls, yaml_path: str) -> "Connector":
        """
        Factory method to convert from YAML to Connector dataclass.

        :param yaml_path: Path to the YAML file
        :return: Connector dataclass
        """
        with open(yaml_path, "r") as file:
            yaml_data = yaml.safe_load(file)

        return cls(
            group_id=yaml_data.get("group_id"),
            service=yaml_data.get("service"),
            trust_certificates=yaml_data.get("trust_certificates"),
            trust_fingerprints=yaml_data.get("trust_fingerprints"),
            run_setup_tests=yaml_data.get("run_setup_tests"),
            paused=yaml_data.get("paused"),
            pause_after_trial=yaml_data.get("pause_after_trial"),
            sync_frequency=yaml_data.get("sync_frequency"),
        )


# lets do our script
if __name__ == "__main__":
    # convert from yaml to dataclass
    yaml_path = os.path.join(os.path.dirname(__file__), "exmaple_connector.yaml")
    connector = Connector.from_yaml(yaml_path)
    lger.info(connector)

    # instantiate fivetran
    client = FivetranClient(
        api_key=os.environ.get("FIVETRAN_API_KEY"),
        api_secret=os.environ.get("FIVETRAN_API_SECRET"),
    )

    # create connector
    response = client.connector_endpoint.create_connector(connector=connector.__dict__)
