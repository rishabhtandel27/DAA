class Solution:
    def findContentChildren(self, g, s):
        # Sort both greed factors and cookie sizes
        g.sort()
        s.sort()

        i, j = 0, 0  # pointers for g (children) and s (cookies)
        satisfied_children = 0

        # Loop through the greed factors and cookie sizes
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If cookie j can satisfy child i
                satisfied_children += 1
                i += 1  # Move to the next child
            # Always move to the next cookie, regardless of whether we satisfied the child or not
            j += 1

        return satisfied_children
