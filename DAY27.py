#https://www.hackerrank.com/challenges/30-testing
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues:
    @staticmethod
    def get_array():
        return [7, 3, 5, 1, 9, 2]

    @staticmethod
    def get_expected_result():
        return 3

class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        return [7, 3, 5, 1, 9, 1, 2]

    @staticmethod
    def get_expected_result():
        return 3

