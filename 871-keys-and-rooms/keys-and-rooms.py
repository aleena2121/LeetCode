class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        havekey = set()
        havekey.add(0)
        def dfs(room):
            for key in rooms[room]:
                if key not in havekey:
                    havekey.add(key)
                    dfs(key)
        
        dfs(0)
        return len(havekey) == len(rooms)
        