class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        fleet, cur = 0, 0 

        for dis, speed in sorted(pairs)[::-1]:
            destT = (target - dis) / speed
            if destT > cur:
                fleet += 1
                cur = destT
        return fleet
                







        