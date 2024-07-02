import random
#  1 Задача
#  a = len(arr) - 1
#  out = list()
#  while a > 0:             O(n)?
#       out.append(arr[a])
#       a = a // 1.7        O(log1.7(n))?
# out.merge_sort()          O(n*log(n))
#  ответ n*log(n)

#  2 Считалочка


def reader(n: int, k: int) -> int:
    if n <= 0 or k <= 0:
        raise ValueError()
    if n == 1:
        return 0
    res = (reader(n-1, k) + k) % n
    print(res)
    return res

# 7 Сортировка


def counting_sort(massive):
    min_val = 13
    max_val = 25

    count = [0] * (max_val - min_val + 1)
    for i in massive:
        count[i - min_val] += 1

    # index = 0
    # for i in range(max_val - min_val + 1):
    #     while count[i] > 0:
    #         massive[index] = i + min_val
    #         index += 1
    #         count[i] -= 1
    #
    # return massive

    for i in range(1, 13):
        count[i] += count[i - 1]
    print(count)

    sort_massive = [0] * len(massive)

    for i in reversed(massive):
        sort_massive[count[i - min_val]-1] = i
        count[i - min_val] -= 1

    return sort_massive


if __name__ == '__main__':

    print(reader(10, 4))
    print(reader(1, 5))

    print(counting_sort([random.randint(13, 25) for _ in range(100)]))
