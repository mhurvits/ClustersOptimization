import copy
from typing import List
from Cluster import Cluster
from Service import Service
import Strategy
# from __future__ import annotations


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, service_list: List[Service], clusters_list: List[Cluster], strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self.services = service_list
        # self.clusters = copy.deepcopy(clusters_list)
        self.clusters = clusters_list
        self._strategy = strategy

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
        return self._strategy.do_algorithm(self.services, self.clusters)

