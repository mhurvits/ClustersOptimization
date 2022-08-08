from cluster import Cluster
from service import Service
from copy import deepcopy
from context import Context
from strategy import *


def calculate_best_strategy(service_list, list_of_clusters):
    strategies_total_prices = []
    for st_j in Strategy.__subclasses__():
        clusters_list_st_j = deepcopy(list_of_clusters)  # for not changing the input
        service_list_st_j = deepcopy(service_list)  # for not changing the input
        context_st_j = Context(service_list_st_j, clusters_list_st_j, st_j())
        price_st_j = context_st_j.do_some_business_logic()
        strategies_total_prices.append((st_j, price_st_j))
    return min(strategies_total_prices, key=lambda x: x[1])


"""
1. creates active clusters list from ACTIVE_CLUSTERS file - V
2. receives from user the properties of the services to enter and creates service object for each property entered  - V 
3. calculate the best strategy for minimizing the total price
4. return best strategy description to the user

"""
# 1 - creates list of clusters from file
with open('ACTIVE_CLUSTERS') as f:
    lines = f.readlines()
    cd = [line.strip().split(',') for line in lines]

clusters_list = []
for c in cd:
    name = c[0]
    price = int(c[1])
    properties = [float(c[i]) for i in range(2, len(c))]
    clusters_list.append(Cluster(name, price, [], properties))

# 2 - creates list of services from user
user_services = []
service_cnt = int(input('How many services would you like to add? '))
print('\n')
for s in range(1, service_cnt + 1):
    name = input('Enter {}\'st service name '.format(s))
    cpu = input('Enter {}\'st service CPU need '.format(s))
    network = input('Enter {}\'st service network need '.format(s))
    memory = input('Enter {}\'st service memory need '.format(s))
    service = Service(name, [float(cpu), float(network), float(memory)])
    user_services.append(service)
    print('-----------------------------------------------')

# 3 - calculate the total price of each strategy
best_st = calculate_best_strategy(user_services, clusters_list)


