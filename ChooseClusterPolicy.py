from typing import List
from Cluster import Cluster
import Kafka

"""
all the different possible policies to choose cluster for the given kafka.
As for now, contains only very trivial one that chooses the first cluster that is available . 
"""

def choose_cluster_policy(kafka: Kafka, list_of_clusters: List[Cluster]):
    is_found = False
    for cluster in list_of_clusters:
        if not cluster.Is_Open:
            continue
        if kafka.check_match_to_cluster(cluster):
            kafka.Cluster = cluster
            cluster.update_cluster(kafka)
            is_found = True
            break
    return is_found



