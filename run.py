# Search methods

import search


def searchPathBetweenCities(firstCity, secondCity):
    cities = search.GPSProblem(firstCity, secondCity, search.romania)
    nodeBB, expandedNodesBB = search.branch_and_bound_graph_search(cities)
    nodeBBE, expandedNodesBBE = search.branch_and_bound_estimate_graph_search(cities)

    print("Without heuristic: " + str(nodeBB.path()) + "\nWith heuristic: " + str(nodeBBE.path()))
    print("Without heuristic: " + str(expandedNodesBB) + "\nWith heuristic: " + str(expandedNodesBBE))

    return expandedNodesBB, expandedNodesBBE


testCities = [('A', 'B'), ('O', 'E'), ('D', 'N'), ('S', 'B'), ('O', 'T')]

averageBB = 0
averageBBE = 0
for a, b in testCities:
    resultBB, resultBBE = searchPathBetweenCities(a, b)
    averageBB += resultBB
    averageBBE += resultBBE

averageBB /= len(testCities)
averageBBE /= len(testCities)

print("The average of expanded nodes without heuristic is " + str(averageBB) +
      " and with heuristic is " + str(averageBBE))

