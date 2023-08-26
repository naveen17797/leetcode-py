class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t_map = {}
        s_map = {}

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        m1, m2 = None, None
        if len(s_map) > len(t_map):
            m1, m2 = s_map, t_map
        else:
            m1, m2 = t_map, s_map

        for c, value in m1.items():
            if m2.get(c, 0) != value:
                return False

        return True
