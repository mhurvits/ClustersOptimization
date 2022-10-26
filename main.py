from cluster import Cluster
from service import Service
from copy import deepcopy
from strategy import *

"""
1. creates active clusters list from ACTIVE_CLUSTERS file - V
2. receives from user the properties of the services to enter and creates service object for each property entered  - V 
3. calculate the best strategy for minimizing the total price
4. return best strategy description to the user

"""
# 1 - creates list of clusters from file
with open('ACTIVE_CLUSTERS') as f:
    lines = f.readlines()
    clusters_data = [line.strip().split(',') for line in lines]

clusters_list = []
for c in clusters_data:
    name = c[0]
    price = int(c[1])
    properties = [float(c[i]) for i in range(2, len(c))]
    clusters_list.append(Cluster(name, price, [], properties))

# 2 - creates list of services from file
with open('SERVICE_LIST') as f:
    lines = f.readlines()
    services_data = [line.strip().split(',') for line in lines]

services_list = []
for c in services_data:
    name = c[0]
    properties = [float(c[i]) for i in range(1, len(c))]
    services_list.append(Service(name, properties))


# 3 - calculate placing for each strategy
for st in Strategy.__subclasses__():
    strategy = st(st.__name__, deepcopy(clusters_list))
    strategy.calculate_new_placing(services_list)
    placing = strategy.export_placing_to_list()
    total_price = strategy.calculate_price()
    running_time = strategy.calculate_running_time()
    print("-----------------------------------------------------------------------------------------------------------")
    print(f"{strategy.Name} costs {total_price}$ in total and takes {running_time} seconds to run.\n it's placing is: "
          f"\n {placing}")


