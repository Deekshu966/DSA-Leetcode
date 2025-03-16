class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def canRepairInTime(mid):
            """Check if we can repair `cars` within `mid` minutes."""
            total_cars = 0
            for r in ranks:
                # Solve equation `r * x^2 <= mid` for x (max cars this mechanic can fix)
                max_cars = int((mid // r) ** 0.5)
                total_cars += max_cars
                if total_cars >= cars:  
                    return True
            return False

        # Binary search on time
        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try for a smaller time
            else:
                left = mid + 1  # Increase time
        
        return left