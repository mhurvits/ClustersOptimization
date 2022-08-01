from typing import List, Any
import Service


class Cluster:


    def __init__(self, price, max_service_count, service_list, properties: List[float]):
        self.Price = price
        self.Max_Service_count = max_service_count
        self.Service_Count = len(service_list)
        self.Services = service_list
        self.Properties = properties
        self.Is_Open = True

    def close_cluster(self):
        self.Is_Open = False

    # def update_cluster(self, service: Service):
    #     i = 0
    #     for prop1, prop2 in zip(self.Properties, service.Properties):
    #         new_prop = prop1 - prop2
    #         self.Properties[i] = new_prop
    #         if new_prop == 0:  # notice that new_prop can't be lower than 0 according to the "Choose Cluster Policy"
    #             self.close_cluster()
    #         i += 1

    def update_cluster(self, service: Service):
        # assuming that this cluster has enough space (Service_Count > 0)
        self.Service_Count -= 1
        if self.Service_Count == 0:
            self.Is_Open = False
        self.Services.append(service)
        return

