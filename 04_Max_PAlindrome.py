def around_centre(left, right, s):
        while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1
        return [left + 1, right - 1]

def longest_pal (s):
    cur_max_left = 0
    cur_max_right = 0

    for i in range(len(s)):

        left, right = around_centre(i, i, s)
        if (right - left) > (cur_max_right - cur_max_left):
            cur_max_left, cur_max_right = left, right

        left, right = around_centre(i, i+1, s)
        if (right - left) > (cur_max_right - cur_max_left):
            cur_max_left, cur_max_right = left, right

    return s[cur_max_left : cur_max_right + 1]


# Подход с расширением от центра
# Сложность: O(n^2), где n - длина s
# В цикле for итерируемся n раз, а внутри цикла дважды по n/2 (в худшем случае) => n^2 / 2 = O(n^2)
