class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            if mp.get("".join(sorted(s))) == None:
                mp["".join(sorted(s))] = [s]
            else:
                mp["".join(sorted(s))].append(s)
        ans = []
        for key in mp:
            ans.append(mp[key])
        return ans
