from solution import Solution

def test_solution():
    s = Solution()

    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
    assert s.rob([2,1,1,4]) == 6
    assert s.rob([0,0,0,0]) == 0
    assert s.rob([1,3,1,3,100]) == 103