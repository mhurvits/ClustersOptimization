from context import Context
from strategy import *
from copy import deepcopy
"""                 
    property list containes : [CPU, memory, network]   
    memory in MB, network in mbps               
"""

kafka1 = Service([12, 500, 2])
kafka2 = Service([5, 200, 1])
kafka3 = Service([10, 400, 7])


def print_c(clusters):
    print([c.Properties for c in clusters])
    return None

# Cluster initialization: (price, max_service_count, service_list, properties: List[float])

def one_kafka_basic_test_1():
    cluster1 = Cluster(10, [], [12, 1000, 3])
    cluster2 = Cluster(20, [], [10, 500, 7])
    cluster3 = Cluster(30, [], [5, 1000, 2])
    clusters_list = [cluster1, cluster2, cluster3]
    context = Context([kafka1], clusters_list, ConcreteStrategyA())
    context.do_some_business_logic()
    assert [c.Properties for c in clusters_list] == [[0, 500, 1], [10, 500, 7], [5, 1000, 2]]
    assert not clusters_list[0].Is_Open


def one_kafka_basic_test_2():
    cluster1 = Cluster(10, [], [0, 500, 1])
    cluster2 = Cluster(20, [], [10, 500, 7])
    cluster3 = Cluster(30, [], [5, 1000, 2])
    clusters_list = [cluster1, cluster2, cluster3]
    context = Context([kafka2], clusters_list, ConcreteStrategyA())
    context.do_some_business_logic()
    assert [c.Properties for c in clusters_list] == [[0, 500, 1], [5, 300, 6], [5, 1000, 2]]


def two_kafka_basic_test_1():
    cluster1 = Cluster(10, [], [12, 1000, 3])
    cluster2 = Cluster(20, [], [10, 500, 7])
    cluster3 = Cluster(30, [], [5, 1000, 2])
    clusters_list = [cluster1, cluster2, cluster3]
    context = Context([kafka1, kafka2], clusters_list, ConcreteStrategyA())
    context.do_some_business_logic()
    assert [c.Properties for c in clusters_list] == [[0, 500, 1], [5, 300, 6], [5, 1000, 2]]


def open_new_cluster_basic_test_1():
    cluster1 = Cluster(10, [], [0, 500, 1])
    cluster2 = Cluster(20, [], [0, 500, 7])
    cluster3 = Cluster(30, [], [0, 1000, 2])
    clusters_list = [cluster1, cluster2, cluster3]
    context = Context([kafka1], clusters_list, ConcreteStrategyA())
    context.do_some_business_logic()
    assert [c.Properties for c in clusters_list] == [[0, 500, 1], [0, 500, 7], [0, 1000, 2], [8, 13, 18]]


def strategy_comparison_basic_test_1():
    cluster1 = Cluster(10, [], [12, 1000, 3])
    cluster2 = Cluster(20, [], [5, 500, 7])
    cluster3 = Cluster(30, [], [0, 1000, 2])
    clusters_list_A = [cluster1, cluster2, cluster3]
    clusters_list_B = deepcopy([cluster1, cluster2, cluster3])
    context_st_A = Context([kafka1, kafka2], clusters_list_A, ConcreteStrategyA())
    context_st_B = Context([kafka1, kafka2], clusters_list_B, ConcreteStrategyB())

    price_st_A = context_st_A.do_some_business_logic()
    price_st_B = context_st_B.do_some_business_logic()

    print_c(clusters_list_A)
    print(price_st_A)
    print_c(clusters_list_B)
    print(price_st_B)



if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    one_kafka_basic_test_1()
    one_kafka_basic_test_2()
    two_kafka_basic_test_1()
    open_new_cluster_basic_test_1()
    strategy_comparison_basic_test_1()
    print("Everything passed")
