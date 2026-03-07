from typing import List


def generate(num_rows: int) -> List[List[int]]:
        triangle = []

        for i in range(0, num_rows):
            row = [0] * (i + 1)
            for col in range(0, i + 1):
                if col == 0 or col == i:
                    row[col] = 1

                else:
                    row[col] = triangle[i - 1][col - 1] + triangle[i - 1][col]
            triangle.append(row)

        return triangle



"""or"""


def generate_1(num_rows: int) -> List[List[int]]:
    triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)
        for col in range(1, i):
             row[col] = triangle[i - 1][col - 1] + triangle[i - 1][col]
        triangle.append(row)

    return triangle

res=generate_1(5)
print(res)






