from typing import List
import Kafka


class Cluster:
    """
    if the Kafkas_list is empty then this is a dummy Cluster
    """

    def __init__(self, kafkas_list: List[Kafka] = [], max_capacity: float = 0, used_capacity: float = 0,
                 properties: List[float] = None):
        self.Kafkas_list = kafkas_list
        self.Capacity_Remained = max_capacity - used_capacity
        self.Properties = properties
        self.Is_Open = True
        self.next = None

    def close_cluster(self):
        self.Is_Open = False


class ClustersList:
    """
    Consists of several pointers, each for different size of cluster.
    An example of using this partition (small, medium, large) is for representing a trait that can't necessarily
    be quantified, such as: the credibility of a cluster.
    """

    def __init__(self):
        self.length = 0
        self.Closed_Clusters = ClustersList()
        self.Small_Size_Open_Clusters = ClustersList()
        self.Medium_Size_Open_Clusters = ClustersList()
        self.Large_Size_Open_Clusters = ClustersList()

    def get_suitable_list(self, size: int):
        if size == 0:
            return self.Small_Size_Open_Clusters
        elif size == 1:
            return self.Medium_Size_Open_Clusters
        elif size == 2:
            return self.Large_Size_Open_Clusters
        else:
            raise Exception("Size type is not defined. only 0, 1, 2 are possible")

    # to be continued...
    # def add_new_cluster_to_list(self, kafkas_list, max_capacity, used_capacity, properties):
    #     new_cluster = Cluster(kafkas_list, max_capacity, used_capacity, properties)
