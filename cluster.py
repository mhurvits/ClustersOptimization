from typing import List
from service import Service


class Cluster:
    def __init__(self, name, price, service_list: List[Service], properties: List[float]):
        self.Name = name
        self.Price = price
        self.Services = service_list
        self.Properties = properties
        self.Is_Open = True

    def close_cluster(self):
        self.Is_Open = False

    def update_cluster_with_service(self, service: Service):
        i = 0
        for prop1, prop2 in zip(self.Properties, service.Properties):
            new_prop = prop1 - prop2
            self.Properties[i] = new_prop
            if new_prop <= 0:
                self.close_cluster()
            i += 1
        self.Services.append(service)
        return

