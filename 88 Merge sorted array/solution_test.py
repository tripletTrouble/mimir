from solution import Solution

def test_solution():
    s = Solution()

    assert s.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]
    assert s.merge([2,5,6,0,0,0], 3, [1,2,3], 3) == [1,2,2,3,5,6]
    assert s.merge([1,2,7,0,0], 3, [2,5], 2) == [1,2,2,5,7]
    assert s.merge([0], 0, [2], 1) == [2]
    assert s.merge([2,0], 1, [1], 1) == [1,2]
    assert s.merge([-1,0,0,0,3,0,0,0,0,0,0], 5, [-1,-1,0,0,1,2], 6) == [-1,-1,-1,0,0,0,0,0,1,2,3]