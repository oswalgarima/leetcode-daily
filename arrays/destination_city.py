"""
1436. Destination City
https://leetcode.com/problems/destination-city/


You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.

Example:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
"""


# Runtime: 80ms (11,17%)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        hash_map = {}

        for _, cities in enumerate(paths):
            # key city A as the key and city B as the val
            hash_map[cities[0]] = cities[1]

        # since destination city leads to nowhere (the end)
        for val in hash_map.values():
            # the dest city will never be in the key
            # hence we return the key not in the hash_map
            if val not in hash_map.keys():
                return val
