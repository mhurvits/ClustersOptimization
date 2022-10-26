from typing import List
# from cluster import Cluster


class Service:

    def __init__(self, name: str, properties: List[float]):
        self.Name = name
        self.Properties = properties
        self.Cluster = None

    def check_match_to_cluster(self, cluster):
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

