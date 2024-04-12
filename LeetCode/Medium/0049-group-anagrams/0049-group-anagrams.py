class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s in dic:
                dic[s].append(strs[i])
            else:
                dic[s] = [strs[i]]
        anagrams_list = list(dic.values())
        for i in range(len(anagrams_list)):
            anagrams_list[i].sort()
        return sorted(anagrams_list, key=lambda x: len(x))