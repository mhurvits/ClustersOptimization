# from typing import List
# from service import Service


class Cluster:
    # def __init__(self, price, service_list: List[Service], properties: List[float]):
    def __init__(self, price, service_list, properties):
        self.Price = price
        self.Services = service_list
        self.Properties = properties
        self.Is_Open = True

    def close_cluster(self):
        self.Is_Open = False

