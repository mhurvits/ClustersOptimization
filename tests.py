import Context
from Strategy import *

"""                 
    property list containes : [CPU, memory, network]   
    memory in MB, network in mbps               
"""

kafka1 = Service.Service([12, 500, 2])
kafka2 = Service.Service([5, 200, 1])
kafka3 = Service.Service([10, 400, 7])


def print_c(clusters):
    print([c.Properties for c in clusters])
    return None

# Cluster initialization: (price, max_service_count, service_list, properties: List[float])

def one_kafka_basic_test_1():
    cluster1 = Cluster(10, 30, [], [12, 1000, 3])
    cluster2 = Cluster(20, 30, [], [10, 500, 7])
    cluster3 = Cluster(30, 30, [], [5, 1000, 2])
    context = Context.Context([kafka1], [cluster1, cluster2, cluster3], ConcreteStrategyA())
    clusters = context.do_some_business_logic()
    assert [c.Properties for c in clusters] == [[0, 500, 1], [10, 500, 7], [5, 1000, 2]]
    assert not clusters[0].Is_Open


def one_kafka_basic_test_2():
    cluster1 = Cluster(10, 30, [], [0, 500, 1])
    cluster2 = Cluster(20, 30, [], [10, 500, 7])
    cluster3 = Cluster(30, 30, [], [5, 1000, 2])
    context = Context.Context([kafka2], [cluster1, cluster2, cluster3], ConcreteStrategyA())
    clusters_first_update = context.do_some_business_logic()
    assert [c.Properties for c in clusters_first_update] == [[0, 500, 1], [5, 300, 6], [5, 1000, 2]]


def two_kafka_basic_test_1():
    cluster1 = Cluster(10, 30, [], [12, 1000, 3])
    cluster2 = Cluster(20, 30, [], [10, 500, 7])
    cluster3 = Cluster(30, 30, [], [5, 1000, 2])
    context = Context.Context([kafka1, kafka2], [cluster1, cluster2, cluster3], ConcreteStrategyA())
    clusters_combined = context.do_some_business_logic()
    assert [c.Properties for c in clusters_combined] == [[0, 500, 1], [5, 300, 6], [5, 1000, 2]]


# def open_new_cluster_basic_test_1():


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    one_kafka_basic_test_1()
    one_kafka_basic_test_2()
    two_kafka_basic_test_1()
    print("Everything passed")
