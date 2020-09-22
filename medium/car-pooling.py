from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        smart_trips = []
        for trip in trips:
            smart_trips.append([-1*trip[0], trip[2]])
            smart_trips.append([trip[0], trip[1]])
        smart_trips.sort(key=lambda x: x[1])
        print(smart_trips)
        passengers = 0
        for trip in smart_trips:
            passengers += trip[0]
            if passengers > capacity:
                return False

        return True

    def solution2(self, trips: List[List[int]], capacity: int) -> bool:
        trips_dict = defaultdict(int)
        for trip in trips:
            trips_dict[trip[1]] += trip[0]
            trips_dict[trip[2]] -= trip[0]

        sorted_trips = sorted(trips_dict.items())
        passengers = 0
        for trip, boarders in sorted_trips:
            passengers += boarders
            if passengers > capacity:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.solution2(trips = [[2,1,5],[3,3,7]], capacity = 4))
    print(sol.solution2(trips = [[2,1,5],[3,3,7]], capacity = 5))
    print(sol.solution2(trips=[[4,5,6],[6,4,7],[4,3,5],[2,3,5]], capacity=13))
    print(sol.solution2(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11))

