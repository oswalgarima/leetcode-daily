"""
1108. Defanging an IP Address
https://leetcode.com/problems/defanging-an-ip-address/

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""


# Runtime: 28ms
class Solution:
    def defangIPaddr(self, address: str) -> str:

        return address.replace('.', '[.]')
