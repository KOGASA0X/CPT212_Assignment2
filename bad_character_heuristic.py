def bad_character_heuristic(pattern, text):
    """
    Computes the shift for the pattern based on the bad character rule in the Boyer-Moore algorithm.

    Args:
        pattern (str): The pattern string.
        text (str): The text string, which should be the same length as the pattern.

    Returns:
        int: The number of positions the pattern needs to be shifted to the right.
    """
    # 构建一个字典包含 pattern 中每个字符的最右位置
    rightmost = {c: -1 for c in pattern}
    for i, c in enumerate(pattern):
        rightmost[c] = i

    # 从右向左比较 pattern 和 text
    patternLength = len(pattern)
    for i in range(patternLength - 1, -1, -1):
        if pattern[i] != text[i]:
            # 不匹配的情况
            bad_char = text[i]
            if bad_char in rightmost:
                # 如果 text 中的不匹配字符存在于 pattern 中
                # 计算移动距离: 目标位置 - 当前位置
                shift = max(1, i - rightmost[bad_char])
            else:
                # 如果 text 中的不匹配字符不在 pattern 中
                # 移动距离：整个 pattern 右移至不匹配字符后一位
                shift = i + 1
            return shift

    # 如果字符串完全匹配
    return 0