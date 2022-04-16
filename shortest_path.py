"""Isaac Santillan As13 Code"""
import math
import sys
from collections import defaultdict
from decimal import Decimal
    	
    	
def haversine(s, d):
    latitude1, lon1 = coord[s]
    latitude2, lon2 = coord[d]
    radius = 6371
    dlat = math.radians(latitude2 - latitude1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(latitude1)) \
        * math.cos(math.radians(latitude2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = radius * c
    return dist


fi = open("/srv/datasets/e-roads/vertex_locations.txt")
coord = {int(a): (float(la), float(lo)) for line in fi for a, la, lo in [line.strip().split()]}

edict = defaultdict(dict)
for line in open("/srv/datasets/e-roads/network.txt"):
    src, dst = line.strip().split()
    src, dst = int(src), int(dst)
    if src in coord and dst in coord:
        distance = haversine(src, dst)
        edict[src][dst] = distance
        edict[dst][src] = distance


def shortest_path(start):
    q = [(start, start, 0)]
    d = {start: (start, 0)}
    while len(q) > 0:
        st, stop, weight = q.pop(0)
        if st in d and not (d[st][1] < weight) and st in edict:
            for m in edict[st]:
                if m != stop:
                    if m not in d or (weight + edict[st][m] < d[m][1]):
                        d[m] = (st, edict[st][m] + weight)
                        q.append((m, st, edict[st][m] + weight))
    return d


file = open("/srv/datasets/e-roads/vertex_names.txt")
dest_names = {int(a): b for line in file for a, b in [line.strip().split("\t")]}


def get_key(val):
    for key, value in dest_names.items():
        if val == value:
            return key
    return None


path_dict = shortest_path(get_key((sys.argv[1])))


def printer2(s, destin):
    if path_dict[destin][0] == s:
        return [s]
    else:
        return [path_dict[destin][0]] + printer2(s, path_dict[destin][0])


final_list = [get_key(sys.argv[2])] + printer2(get_key(sys.argv[1]), get_key(sys.argv[2]))
link = "https://www.google.com/maps/dir/"

final_coord1 = str(round(Decimal(coord[final_list[0]][0]), 3))
final_coord2 = str(round(Decimal(coord[final_list[0]][1]), 3))
if len(sys.argv) > 3 and (sys.argv[1] == sys.argv[2]):
    link += final_coord1 + "," + final_coord2 + "/"
    print(link[:-1])


if len(sys.argv) > 3 and (sys.argv[1] != sys.argv[2]):
    for w in final_list[::-1]:
        link += str(round(Decimal(coord[w][0]), 3)) + "," + str(round(Decimal(coord[w][1]), 3)) + "/"
    print(link[:-1])

if len(sys.argv) < 4 and get_key(sys.argv[1]) == get_key(sys.argv[2]):
    print(sys.argv[1])
else:
    for x in final_list[::-1]:
        if len(sys.argv) < 4 and get_key(sys.argv[1]) != get_key(sys.argv[2]):
            print(dest_names[x])