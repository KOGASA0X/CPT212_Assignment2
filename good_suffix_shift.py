def good_suffix_shift(pattern):
    pattern_length = len(pattern)
    suffix = [0] * pattern_length
    goodSuffix = [pattern_length] * pattern_length  # 初始化gs数组，假设在没有好后缀的情况下，移动整个模式长度

    # 计算suffix数组

    # 设置模式串最后一个字符的suffix值为模式串的长度，因为整个模式串都是自身的后缀
    suffix[pattern_length-1] = pattern_length
    # 初始化f为模式串的最后一个索引
    f = pattern_length-1

    # 从模式串的倒数第二个字符开始向前遍历
    for i in range(pattern_length-2, -1, -1):
        # 如果当前索引i大于f且通过之前的计算得到的suffix长度小于从i到f的距离
        # 这表明当前的后缀可以通过之前计算的更长的后缀来简化
        if i > f and suffix[i + pattern_length - 1 - f] < i - f:
            suffix[i] = suffix[i + pattern_length - 1 - f]
        else:
            # 如果当前索引i不满足上述条件，重新设置f为i，重新计算最长公共后缀
            if i < f:
                f = i
            # 从i开始向左对比，计算从i开始的后缀与模式串的后缀的最长公共部分
            # f与模式串的后缀的比较位置同步向左移动
            while f >= 0 and pattern[f] == pattern[f + pattern_length - 1 - i]:
                f -= 1
            # 最长公共后缀的长度为i-f
            suffix[i] = i - f


    # 计算好后缀移动数组gs
    j = 0
    for i in range(pattern_length-1, -1, -1):
        if suffix[i] == i + 1:  # 全后缀匹配的情况
            while j < pattern_length - 1 - i:
                if goodSuffix[j] == pattern_length:  # 只有当gs[j]未被设置时才更新
                    goodSuffix[j] = pattern_length - 1 - i
                j += 1

    # 其他情况，根据suffix值设置gs值
    for i in range(pattern_length - 1):
        goodSuffix[pattern_length - 1 - suffix[i]] = pattern_length - 1 - i

    return goodSuffix


def calculate_shift(pattern, text):
    if len(pattern) != len(text):
        raise ValueError("Pattern and text must be of the same length")
    
    goodSuffix = good_suffix_shift(pattern)
    
    pattern_length = len(pattern)
    
    # 从模式串的末尾开始匹配
    j = pattern_length - 1
    while j >= 0 and pattern[j] == text[j]:
        j -= 1
    
    if j < 0:
        return 0  # 完全匹配
    
    # 如果不匹配，使用好后缀规则来计算移动量
    return goodSuffix[j]

# 使用示例
pattern = "TEXST"
text = "TEXTT"
shift_amount = calculate_shift(pattern, text)
print("Shift amount:", shift_amount)
