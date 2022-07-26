from typing import List
import Cluster


class Kafka:

    def __init__(self, properties: List[float]):
        self.Properties = properties
        self.Cluster = None  # do we want each Kafka to know its cluster?


    def check_match_to_cluster(self, cluster: Cluster):
        """
        :param cluster:
        assuming that if the property of the kafka is bigger, then the cluster doesn't have enough resources to obtain this kafka
        :return: if this kafka can fit in the input cluster
        """
        for prop1, prop2 in zip(self.Properties, cluster.Properties):
            if prop1 > prop2:
                return False
        return True

