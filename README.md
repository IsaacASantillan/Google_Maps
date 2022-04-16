## Shortest Path Between Cities
I wrote a Python program that calculates and prints the shortest path between two vertices in an e-roads graph. In order to determine the shortest path, I assigned weights to each edge that represent the https://en.wikipedia.org/wiki/Great-circle_distance-great-circle distance between the two geographic coordinates as per the https://en.wikipedia.org/wiki/Haversine_formula-haversine formula. I also used Dijkstra's shortest 
path algorithm in order to see all possible routes. If either city name does not exist in the dataset, or there 
is no path between the two cities, an informative one-line message to standard error is printed.
