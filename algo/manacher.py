r"""















"""


def manacher_len(s):
    if len(s) < 2:
        return s

    n_str = '#' + '#'.join(s) + '#'
    print(f'nstr: {s} {n_str}')

    # 回文半径数组
    p_arr = [0] * len(n_str)
    # 回文最右坐标 + 1
    p_r = -1
    # 回文中心坐标
    index = -1
    ans = -1
    print(p_arr)

    for i in range(len(n_str)):
        p_arr[i] = min(p_arr[2 * index - i], p_r - i) if p_r > i else 1

        # 开始扩的过程
        while (i + p_arr[i] < len(n_str) and i - p_arr[i] > -1):
            print(p_arr, i, p_arr[i], i + p_arr[i], i - p_arr[i])
            if (n_str[i + p_arr[i]] == n_str[i - p_arr[i]]):
                p_arr[i] += 1
            else:
                break

        # 更新回文最右坐标以及中心坐标
        if (i + p_arr[i] > p_r):
            p_r = i + p_arr[i]
            index = i
        ans = max(ans, p_arr[i])

    return ans - 1


def manacher_substr(s):
    return ''


def longest_palindrome_length(s):
    return manacher_len(s)


def longest_palindrome(s):
    return manacher_substr(s)


import unittest


class TestLongestPalindromicLength(unittest.TestCase):
    """[summary]
    Test for the file longest_palindromic_substring.py
    Arguments:
        unittest {[type]} -- [description]
    """

    def test_longest_palindromic_substring(self):
        self.assertEqual(len("bb"), longest_palindrome_length("cbbd"))
        self.assertEqual(len("abba"), longest_palindrome_length("abba"))
        self.assertEqual(len("asdadsa"),
                         longest_palindrome_length("dasdasdasdasdasdadsa"))
        self.assertEqual(len("abba"), longest_palindrome_length("cabba"))


class TestLongestPalindromicSubstring(unittest.TestCase):
    """[summary]
    Test for the file longest_palindromic_substring.py
    Arguments:
        unittest {[type]} -- [description]
    """

    def test_longest_palindromic_substring(self):
        self.assertEqual("bb", longest_palindrome("cbbd"))
        self.assertEqual("abba", longest_palindrome("abba"))
        self.assertEqual("asdadsa", longest_palindrome("dasdasdasdasdasdadsa"))
        self.assertEqual("abba", longest_palindrome("cabba"))


def main():
    pass


if __name__ == '__main__':
    main()
