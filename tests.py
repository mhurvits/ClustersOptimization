from Cluster import Cluster
from Kafka import Kafka
import main

"""                 
    property list containes : [CPU, memory, network]   
    memory in MB, network in mbps               
"""

cluster1 = Cluster([], [12, 1000, 3])
cluster2 = Cluster([], [10, 500, 7])
cluster3 = Cluster([], [5, 1000, 2])

kafka1 = Kafka([12, 500, 2])
kafka2 = Kafka([5, 200, 1])
kafka3 = Kafka([10, 400, 7])


def one_kafka_basic_test_1():
    clusters = main.online_bin_packing([kafka1], [cluster1, cluster2, cluster3])
    assert [c.Properties for c in clusters] == [[0, 500, 1], [10, 500, 7], [5, 1000, 2]]
    assert not clusters[0].Is_Open

    clusters_first_update = main.online_bin_packing([kafka2], clusters)
    assert [c.Properties for c in clusters_first_update] == [[0, 500, 1], [5, 300, 6], [5, 1000, 2]]

    # clusters_combined = main.online_bin_packing([kafka1, kafka2], [cluster1, cluster2, cluster3])
    # print([c.Properties for c in clusters_combined])
    # assert [c.Properties for c in clusters_combined] == [c.Properties for c in clusters_first_update]

# def open_new_cluster_basic_test_1():





if __name__ == "__main__":
    one_kafka_basic_test_1()
    print("Everything passed")


