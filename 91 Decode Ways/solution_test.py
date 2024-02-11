from solution import Solution

def test_solution():
    inst = Solution()

    assert inst.numDecodings('1111') == 5
    assert inst.numDecodings('11111') == 8
    assert inst.numDecodings('111111') == 13
    assert inst.numDecodings('60111111') == 0
    assert inst.numDecodings('12') == 2
    assert inst.numDecodings('226') == 3
    assert inst.numDecodings('06') == 0
    assert inst.numDecodings('1201234') == 3