class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        fleet = 0
        curTime = 0

        for dest, speed in sorted(pairs)[::-1]:
            destTime = (target - dest) / speed
            if destTime > curTime:
                fleet += 1
                curTime = destTime
        return fleet








        