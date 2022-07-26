from typing import List, Any
import Kafka


class Cluster:
    """
    if the Kafkas_list is empty then this is a dummy Cluster
    """

    def __init__(self, kafkas_list, properties: List[float]):
        self.Kafkas_list = kafkas_list
        self.Properties = properties
        self.Is_Open = True

    def close_cluster(self):
        self.Is_Open = False

    def update_cluster(self, kafka: Kafka):
        i = 0
        for prop1, prop2 in zip(self.Properties, kafka.Properties):
            new_prop = prop1 - prop2
            self.Properties[i] = new_prop
            if new_prop == 0:  # notice that new_prop can't be lower than 0 according to the "Choose Cluster Policy"
                self.close_cluster()
            i += 1

