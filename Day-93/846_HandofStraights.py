class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        counter = Counter(hand)

        while counter:
            curr = min(counter)

            for i in range(groupSize):
                if counter[curr + i] == 0:
                    return False

                counter[curr + i] -= 1
                if counter[curr + i] < 1:
                    del counter[curr + i]

        return True
