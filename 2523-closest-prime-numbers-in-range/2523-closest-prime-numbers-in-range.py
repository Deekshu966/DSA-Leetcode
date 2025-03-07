class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Sieve of Eratosthenes to find primes up to right
        n = right + 1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Collect all primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # If there are fewer than 2 primes, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]
        
        # Find the closest pair
        min_diff = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i - 1], primes[i]]
        
        return result
