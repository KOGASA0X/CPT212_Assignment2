def good_suffix_shift(pattern):
    m = len(pattern)
    suffix = [0] * m
    gs = [m] * m  # 初始化gs数组，假设在没有好后缀的情况下，移动整个模式长度

    # 计算suffix数组
    suffix[m-1] = m
    f = m-1
    for i in range(m-2, -1, -1):
        if i > f and suffix[i + m - 1 - f] < i - f:
            suffix[i] = suffix[i + m - 1 - f]
        else:
            if i < f:
                f = i
            while f >= 0 and pattern[f] == pattern[f + m - 1 - i]:
                f -= 1
            suffix[i] = i - f

    # 计算好后缀移动数组gs
    j = 0
    for i in range(m-1, -1, -1):
        if suffix[i] == i + 1:  # 全后缀匹配的情况
            while j < m - 1 - i:
                if gs[j] == m:  # 只有当gs[j]未被设置时才更新
                    gs[j] = m - 1 - i
                j += 1

    # 其他情况，根据suffix值设置gs值
    for i in range(m - 1):
        gs[m - 1 - suffix[i]] = m - 1 - i

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
