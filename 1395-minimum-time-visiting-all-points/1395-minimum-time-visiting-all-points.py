class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        idx = 1
        length = len(points)
        total_time = 0
        while idx < length:
            total_time += max(abs(points[idx][0] - points[idx - 1][0]), abs(points[idx][1] - points[idx - 1][1]))
            idx += 1
        return total_time