from typing import List
from Cluster import Cluster,ClustersList
import Kafka

"""
all the different possible policies to choose cluster for the given kafka.
As for now, contains only very trivial one. 
"""

def choose_cluster_policy(kafka: Kafka, list_of_clusters: ClustersList):
    chosen_clusters_list = list_of_clusters.get_suitable_list(kafka.Size)
    return chosen_clusters_list  # return the head of the clusters list