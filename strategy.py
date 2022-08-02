from abc import ABC, abstractmethod
from typing import List
from cluster import Cluster
from service import Service
from DefaultClusters import *

"""
all the different possible policies to choose cluster for the given kafka.
As for now, contains only very trivial one that chooses the first cluster that is available . 
"""

# has duplicate method in context
def calculate_total_price(clusters_list: List[Cluster]) -> float:
    """
    static method foe checking the total price of list of clusters
    """
    total = 0
    for cluster in clusters_list:
        total += cluster.Price
    return total


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, service_list: List[Service], clusters_list: List[Cluster]) -> List[Cluster]:
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    """
        At this Strategy we First check if there already exists a cluster that can contain this service.
        Otherwise, we open a new large Cluster

        For now, no need to create deepcopy here because this function
        will always work on the copy created in choose_cluster_strategy function
    """

    def choose_cluster_strategy(self, service: Service, clusters_list: List[Cluster]):
        # clusters_list_copy = copy.deepcopy(clusters_list)  # for not changing the input
        is_found = False
        for cluster in clusters_list:
            if service.check_match_to_cluster(cluster):
                service.Cluster = cluster
                service.update_cluster_with_service(cluster)
                is_found = True
                break
        return is_found, clusters_list

    def open_new_cluster_strategy(self, service: Service, clusters_list: List[Cluster]):
        new_cluster = Cluster(Price.LARGE.value, [service], Properties.LARGE.value)
        clusters_list.append(new_cluster)
        return clusters_list  # the change is "in-place" so this line is only for future use

    def do_algorithm(self, service_list, clusters_list: List[Cluster]):
        outcome = (False, [])
        for service in service_list:
            outcome = self.choose_cluster_strategy(service, clusters_list)
            if not outcome[0]:
                self.open_new_cluster_strategy(service, outcome[1])
        return outcome[1]  # the change is "in-place" so this line is only for future use


class ConcreteStrategyB(Strategy):
    """
        At this Strategy we open a new small cluster immediately for each service without considering the existing ones and their
        attributes. This Strategy is for the purpose of testing and checking

    """
    def do_algorithm(self, service_list, clusters_list: List[Cluster]):
        for service in service_list:
            new_cluster = Cluster(Price.SMALL.value, [service], Properties.SMALL.value)
            clusters_list.append(new_cluster)
        return clusters_list  # the change is done in place so this line is only for convenience and code arrangement
