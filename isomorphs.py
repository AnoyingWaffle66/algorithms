import collections as c
from algorithms import Algorithm as a

class Isomorph:
    @staticmethod
    def group_isomorphs(string_array):
        exact_iso_map = c.defaultdict(list)
        loose_iso_map = c.defaultdict(list)
        for string in string_array:
            exact = Isomorph.exact_isomorph_pattern(string)
            loose = Isomorph.loose_isomorph_pattern(string)
            exact_iso_map[exact].append(string)
            loose_iso_map[loose].append(string)
        
        non_exact_isomorphs = []
        non_loose_isomorphs = []
        exact_keys_delete = []
        loose_keys_delete = []
        for morph, strings in exact_iso_map.items():
            if len(strings) == 1:
                non_exact_isomorphs.append(strings[0])
                exact_keys_delete.append(morph)
        
        for morph, strings in loose_iso_map.items():
            if len(strings) == 1:
                non_loose_isomorphs.append(strings[0])
                loose_keys_delete.append(morph)
        for key in exact_keys_delete:
            del exact_iso_map[key]
        for key in loose_keys_delete:
            del loose_iso_map[key]
        return {"exact" : dict(exact_iso_map), "loose" : dict(loose_iso_map), "non_exact" : non_exact_isomorphs, "non_loose" : non_loose_isomorphs}

    @staticmethod
    def exact_isomorph_pattern(string) -> tuple:
        string_map = Isomorph.make_string_map(string)
        numberify = []
        for char in string:
            numberify.append(string_map[char])
        return tuple(numberify)
    
    @staticmethod
    def loose_isomorph_pattern(string) -> tuple:
        string_counts = Isomorph.count_string_map(string)
        numberify = []
        for char in string_counts:
            numberify.append(string_counts[char])
        a.insertion(numberify)
        return tuple(numberify)
    
    @staticmethod
    def count_string_map(string) -> dict:
        counted_map = c.defaultdict(int)
        for char in string:
            counted_map[char] += 1
        return dict(counted_map)
    
    @staticmethod
    def make_string_map(string) -> dict:
        string_map = c.defaultdict()
        for char in string:
            if char not in string_map:
                string_map[char] = len(string_map)
        return string_map


if __name__ == "__main__":
    print(Isomorph.group_isomorphs([123, 456, 789]))
    # groupings = Isomorph.group_isomorphs(["aaa", "fear", "mates", "gag", "egg", "add", "foo", "sap", "yay", "tot", "look", "meet", "took", "seer", "seep", "ate", "bar", "eat", "fit", "aaabbbzzz", "bbbaaazzz", "abzzbabaz", "bazzababz", "warrior", "aedor", "eiruw", "aa", "bb", "cacccdaabc", "cdcccaddbc", "dcdddbccad", "bdbbbaddcb", "bdbcadbbdc", "abaadcbbda", "babcdabbac", "cacdbaccad", "dcddabccad", "cacccbaadb", "bbcdcbcbdd", "bcbadcbbca"])
    # print("\nexact isomorphic patterns")
    # print(groupings["exact"])
    # print("\nnon exact isomorphs")
    # print(groupings["non_exact"])
    # print("\nloose isomorphic patterns")
    # print(groupings["loose"])
    # print("\nnon loose isomorphs")
    # print(groupings["non_loose"])
    # print()