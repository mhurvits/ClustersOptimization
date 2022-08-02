from typing import List
from cluster import Cluster
from service import Service
from strategy import Strategy, calculate_total_price


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, service_list: List[Service], clusters_list: List[Cluster], strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self.Services = service_list
        self.Clusters = clusters_list
        self.Total_Price = self.calculate_total_price()
        self._strategy = strategy

    def calculate_total_price(self):
        total = 0
        for cluster in self.Clusters:
            total += cluster.Price
        return total


    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def do_some_business_logic(self):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        updated_clusters_list = self._strategy.do_algorithm(self.Services, self.Clusters)
        return calculate_total_price(updated_clusters_list)
        # return updated_clusters_list  # maybe we should add the total price calculation here


