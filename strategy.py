from typing import List
from cluster import Cluster
from service import Service
from DefaultClusters import *
import time


class Strategy(object):

    def __init__(self, name: str, clusters_list: List[Cluster]):
        self.Name = name
        self.Clusters = clusters_list
        self.RunningTime = 0
        # self.Clusters_Names_List = [cluster.Name for cluster in clusters_list]

    def calculate_new_placing(self, service_list: List[Service]):
        pass

    def export_placing_to_list(self):
        placing_list = []
        for cluster in self.Clusters:
            services_name_list = [service.Name for service in cluster.Services]
            placing_list.append(services_name_list)
        return placing_list

    def calculate_price(self):
        total_strategy_price = 0
        for cluster in self.Clusters:
            total_strategy_price += cluster.Price
        return total_strategy_price

    def calculate_running_time(self):
        return self.RunningTime

# ---------------------------------------------------------------------------------------------------------------------

class ConcreteStrategyA(Strategy):
    """
        At this Strategy we First check if there already exists a cluster that can contain this service.
        Otherwise, we open a new large Cluster
    """

    def choose_cluster_strategy(self, service: Service):
        is_found = False
        for cluster in self.Clusters:
            if service.check_match_to_cluster(cluster):
                service.Cluster = cluster
                cluster.update_cluster_with_service(service)
                is_found = True
                break
        return is_found

    def open_new_cluster_strategy(self, service: Service):
        new_cluster = Cluster('NewCluster', Price.LARGE.value, [], Properties.LARGE.value)
        new_cluster.update_cluster_with_service(service)
        self.Clusters.append(new_cluster)
        return

    def calculate_new_placing(self, service_list: List[Service]):
        start = time.time()
        for service in service_list:
            outcome = self.choose_cluster_strategy(service)
            if not outcome:
                self.open_new_cluster_strategy(service)
        end = time.time()
        self.RunningTime = end - start
        return self.Clusters


# ----------------------------------------------------------------------------------------------------------------------
class ConcreteStrategyB(Strategy):
    """
        At this Strategy we open a new small cluster immediately for each service without considering the existing ones
        and their attributes. This Strategy is for the purpose of testing and checking
    """

    def calculate_new_placing(self, service_list: List[Service]):
        start = time.time()
        for service in service_list:
            new_cluster = Cluster('NewCluster', Price.SMALL.value, [], Properties.SMALL.value)
            service.Cluster = new_cluster
            new_cluster.update_cluster_with_service(service)
            self.Clusters.append(new_cluster)
        end = time.time()
        self.RunningTime = end - start
        return self.Clusters
