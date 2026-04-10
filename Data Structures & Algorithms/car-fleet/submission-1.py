class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleets, curtime = 0, 0

        for dis, speed in sorted(pairs)[::-1]:
            dest_time = (target - dis) / speed
            if curtime < dest_time:
                fleets += 1
                curtime = dest_time

        return fleets






        