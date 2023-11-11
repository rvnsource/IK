def count_phone_numbers_of_given_length(start_digit, phone_number_length):
    list_of_neighbors = [
        [4, 6],  # 0
        [6, 8],  # 1
        [7, 9],  # 2
        [4, 8],  # 3
        [3, 9, 0],  # 4
        [],  # 5
        [1, 7, 0],  # 6
        [2, 6],  # 7
        [1, 3],  # 8
        [2, 4]  # 9
    ]

    numbers_till = [[0] * 10 for _ in range(phone_number_length)]
    numbers_till[0][start_digit] = 1

    for i in range(1, phone_number_length):
        for num in range(10):
            for to in list_of_neighbors[num]:
                numbers_till[i][num] += numbers_till[i - 1][to]

    ans = sum(numbers_till[phone_number_length - 1])
    return ans


start_digit = 1
phone_number_length = 2
print(count_phone_numbers_of_given_length(start_digit, phone_number_length))
