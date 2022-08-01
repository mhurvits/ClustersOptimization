from abc import ABC, abstractmethod
from typing import List
from Cluster import Cluster
import Service
import copy
from config import *

"""
all the different possible policies to choose cluster for the given kafka.
As for now, contains only very trivial one that chooses the first cluster that is available . 
"""


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def choose_cluster_strategy(self, service: Service, clusters_list: List[Cluster]) -> (bool, List[Cluster]):
        pass

    @abstractmethod
    def open_new_cluster_strategy(self, service: Service, clusters_list: List[Cluster]) -> Cluster:
        pass

    def do_algorithm(self, service_list, clusters_list: List[Cluster]):
        outcome = (False, [])
        for service in service_list:
            outcome = self.choose_cluster_strategy(service, clusters_list)
            if not outcome[0]:
                self.open_new_cluster_strategy(service, outcome[1])
        return outcome[1]



"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):

    def choose_cluster_strategy(self, service: Service, clusters_list: List[Cluster]):
        # clusters_list_copy = copy.deepcopy(clusters_list)  # for not changing the input
        is_found = False
        for cluster in clusters_list:
            if service.check_match_to_cluster(cluster):
                service.Cluster = cluster
                cluster.update_cluster(service)
                is_found = True
                break
        return is_found, clusters_list

    def open_new_cluster_strategy(self, service: Service, clusters_list: List[Cluster]):
        # At this time, no need to create deepcopy here because this function
        # will always work on the copy created in choose_cluster_strategy function
        new_cluster = Cluster(CLUSTER_MAX_PRICE, CLUSTER_MAX_SERVICE_COUNT, [service], service.Properties)
        clusters_list.append(new_cluster)
        return clusters_list  # the change is "in-place" so this line is only for future use


class ConcreteStrategyB(Strategy):

    def choose_cluster_strategy(self, service: Service, clusters_list: List[Cluster]):
        return

    def open_new_cluster_strategy(self, service: Service, clusters_list: List[Cluster]):
        return
