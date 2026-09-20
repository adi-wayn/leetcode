class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {} # sorted str : list(str)

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in values.keys():
                values[sorted_s] = [s]

            else:
                values[sorted_s].append(s)

        return (list(values.values()))