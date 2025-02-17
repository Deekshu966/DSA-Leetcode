class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def backtrack(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    # Use this tile
                    counter[tile] -= 1
                    total += 1  # Count the current sequence

                    # Explore further sequences
                    total += backtrack(counter)

                    # Backtrack: undo the choice
                    counter[tile] += 1
            return total

        # Count frequency of each tile
        counter = Counter(tiles)
        return backtrack(counter)
