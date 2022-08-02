from typing import List
from cluster import Cluster


class Service:

    def __init__(self, properties: List[float]):
        self.Properties = properties
        self.Cluster = None  # do we want each Kafka to know its cluster?

    def check_match_to_cluster(self, cluster: Cluster):
        """
        :param cluster:
        assuming that if the property of the kafka is bigger, then the cluster doesn't have enough resources to obtain this kafka
        :return: if this kafka can fit in the input cluster
        """
        if not cluster.Is_Open:
            return False
        for prop1, prop2 in zip(self.Properties, cluster.Properties):
            if prop1 > prop2:
                return False
        return True

    def update_cluster_with_service(self, cluster: Cluster):
        i = 0
        for prop1, prop2 in zip(cluster.Properties, self.Properties):
            new_prop = prop1 - prop2
            cluster.Properties[i] = new_prop  # bad coding: Need to define setter function
            if new_prop == 0:  # notice that new_prop can't be lower than 0 according to the "Choose Cluster Policy"
                cluster.close_cluster()
            i += 1
