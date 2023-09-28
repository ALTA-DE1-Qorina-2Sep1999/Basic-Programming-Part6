def find_max_sum_sub_array(k, arr):
    a = 0
    n = len(arr)
    for i in range(k):
        a += arr[i]
    curr_sum = a
    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        a = max(a, curr_sum)
    return a

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8