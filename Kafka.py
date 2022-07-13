from typing import List


class Kafka:

    def __init__(self, size: int, properties: List[float]):
        self.Size = size
        self.Properties = properties
        self.Cluster = None  # do we want each Kafka to know its cluster?
