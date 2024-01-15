# Finding the Optimal Routing Scheme for a Fullly-Automated Urban Traffic Optimization System

## Author

* NTPU Student ID: 711281105
* Name: 陳奕光 / Evan Chen

## Introduction

The V2X (vehicle-to-everything) concept is currently a focal point in technology development. Beyond advancements in self-driving capabilities, such as Tesla's Full Self-Driving (FSD), the ultimate objective is to equip every vehicle on the road with the ability to "communicate" with one another and the cloud. This connectivity opens up a myriad of possibilities for future applications. In my opinion, one of the most crucial aspects is the optimization of traffic during urban rush hours. Hence, apart from the various advanced V2X technologies, there is a pressing need for an algorithm to determine an optimal routing scheme for vehicles operating within a specific urban area.


## The Problem

Design a routing algorithm that is systematically optimal for a specific area.


## Problem Modeling

1. First of all, we use a graph to model the "map" of this certain area, where each vertex represents the intersection of two(or more) roads, and each edge represents the road connecting two vertices. For example:

     ![Map-as-Graph Example](./docs/maps-as-graph.jpg?raw=1)
     From the example above, the blue dots are vertices that represents intersections, and red lines are the edges that represent the road connecting vertices.
     (Map content credit: [OpenStreetMap](https://openstreetmap.org/)

2. Each edge has a property $K_{throughput}$ indicating how much traffic it could deal with
3. Use optimal multihop routing to achieve global optimum to avoid routing paradox that leads to a congestion in a certain area
4. Traffic may come from any vertex $x_n$ modeled as a homogeneous Poisson Process with rate $\lambda$ to a destination vertex $x_d$
5. Each edge has its own weight $w(x_i, x_j)$ defined as $\frac{1}{K_{throughput} - N_{traffic}}$
6. Everytime a vehicle starts traveling from vertex $x_n$, the system uses the snapshot of the current traffic and makes a routing decision for this vehicle.

## Assumptions

1. Every single vehicle running on/into this area is connected to our system
2. By assumption 1, our system knows the location and destination of every single vehicle
3. To avoid dealing with the prisoner's dilemma, each vehicle driver is rational and refrains from intervening to alter the routing outcome.
4. The computing power is enough for (near) realtime route planning for each time unit
5. To simplify to problem, we assume that each vehicle can go through an edge in a single time unit

## The Algorithm

1. Construct the graph
2. Loop (main iteration)

     1. Use Dijkstra's Algorithm to plan a route under current traffic
     2. Loop: All vehicles in the map advance to next hop

          1. Substract 1 to "load" of the edge to last node
          2. Set current node to next hop
          3. Add 1 to "load" of the edge connecting last and current node
          4. If current node equals to the destination, remove this vehicle from the map

     2. Sample from a Poisson RV with rate $\lambda$ to decide number of arriving vehicles and apply a loop to initialize these vehicles

          1. Randomly pick two nodes as starting and destination node with uniform distrubution
          2. Add the newly created vehicle to the map

The weight function for edges will be varying according to the current traffic. Therefore, this algorithm will adapt to the current situation and find the best routing scheme.


## Source Code

* Hosted on GitHub: https://github.com/twolights/ntpu-random-process-project-2

## Future Work/Further Discussions

1. The assumption #5 is not practical in real world scenario. We might give each edge a property "length" and use a queue to model the real traffic going through the edge(road).
2. Currently I am not able to describe/approximate an upper bound for capacities, time cost... etc with mathematics. Further derivation is needed.

## References

* [1] François Baccelli, Bartlomiej Blaszczyszyn. Stochastic Geometry and Wireless Networks, Volume II - Applications. Baccelli, F. and Blaszczyszyn, B. NoW Publishers, 2, pp.209, 2009, Founda- tions and Trends in Networking: Vol. 4: No 1-2, pp 1-312, 978-1-60198-266-7, 978-1-60198-267-4. 10.1561/1300000026. inria-00403040v4
* [2] Dijkstra's Algorithm implementation reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
