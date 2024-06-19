def good_suffix_shift(pattern):
    pattern_length = len(pattern)
    suffix = [0] * pattern_length
    gs = [pattern_length] * pattern_length  # 初始化gs数组，假设在没有好后缀的情况下，移动整个模式长度

    # 计算suffix数组
    suffix[pattern_length-1] = pattern_length
    f = pattern_length-1
    for i in range(pattern_length-2, -1, -1):
        if i > f and suffix[i + pattern_length - 1 - f] < i - f:
            suffix[i] = suffix[i + pattern_length - 1 - f]
        else:
            if i < f:
                f = i
            while f >= 0 and pattern[f] == pattern[f + pattern_length - 1 - i]:
                f -= 1
            suffix[i] = i - f

    # 计算好后缀移动数组gs
    j = 0
    for i in range(pattern_length-1, -1, -1):
        if suffix[i] == i + 1:  # 全后缀匹配的情况
            while j < pattern_length - 1 - i:
                if gs[j] == pattern_length:  # 只有当gs[j]未被设置时才更新
                    gs[j] = pattern_length - 1 - i
                j += 1

    # 其他情况，根据suffix值设置gs值
    for i in range(pattern_length - 1):
        gs[pattern_length - 1 - suffix[i]] = pattern_length - 1 - i

    return gs



def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    gs = good_suffix_shift(pattern)  # 获取好后缀移动表
    print("Good suffix shifts:", gs)
    i = 0  # 文本的索引

    while i <= n - m:
        j = m - 1
        # 从模式串的末尾开始匹配
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            print(f"Pattern occurs at index {i}")
            # 如果完全匹配，根据好后缀规则移动
            i += gs[0]  # 如果模式串完全匹配，使用gs表的第一个元素来决定下一步的移动
        else:
            # 如果不匹配，使用好后缀规则来移动
            i += max(1, gs[j])  # 确保至少移动1位

# 使用示例
text = "TTTESTESTTT"
pattern = "TEST"
boyer_moore_search(text, pattern)
