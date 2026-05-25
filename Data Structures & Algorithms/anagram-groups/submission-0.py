class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)    # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26    # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

                #   a = 80 -> 0, 80 - 80
                #   b = 81 -> 1, 81 - 80

            res[tuple(count)].append(s)

        return list(res.values())

        #   O(m * n), where m = number of strings and n = avg. length of each string
