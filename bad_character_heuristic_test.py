import bad_character_heuristic

def test_bad_character_heuristic():
    # Test case 1: Pattern and text are the same
    pattern = "abc"
    text = "abc"
    assert bad_character_heuristic.bad_character_heuristic(pattern, text) == 0

    # Test case 2: Pattern and text have one different character
    pattern = "abc"
    text = "abd"
    assert bad_character_heuristic.bad_character_heuristic(pattern, text) == 3

    # Test case 3: Pattern and text have multiple different characters
    pattern = "abb"
    text = "aba"
    assert bad_character_heuristic.bad_character_heuristic(pattern, text) == 2

    pattern = "abb"
    text = "aab"
    assert bad_character_heuristic.bad_character_heuristic(pattern, text) == 1

    print("All test cases pass")

test_bad_character_heuristic()
