from Cluster import Cluster
import Kafka


def open_new_cluster_policy(kafka: Kafka):
    return Cluster([kafka], kafka.Properties)
