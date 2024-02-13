from solution import Solution

def test_solution():
    s = Solution()

    assert s.canJump([1,2,3]) == True
    assert s.canJump([4,3,2,1,0,5,0]) == False
    assert s.canJump([2,5,0,0]) == True
    assert s.canJump([3,0,8,2,0,0,1]) == True
    assert s.canJump([1,2]) == True
    assert s.canJump([2,3,0,1,4]) == True
    assert s.canJump([5,9,3,2,1,0,2,3,3,1,0,0]) == True
    assert s.canJump([3,2,1,0,4]) == False
