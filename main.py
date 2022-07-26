from typing import List
from Cluster import Cluster
from Kafka import Kafka
from ChooseClusterPolicy import choose_cluster_policy
from OpenNewClusterPolicy import open_new_cluster_policy


def online_bin_packing(kafkas_list: List[Kafka], clusters: List[Cluster]):
    for kafka in kafkas_list:
        if not choose_cluster_policy(kafka, clusters):
            new_cluster = open_new_cluster_policy(kafka)
            clusters.append(new_cluster)
    return clusters





