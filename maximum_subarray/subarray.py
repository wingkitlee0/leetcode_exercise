"""
Find the subarray with maximum sum
"""


class Subarray:
    def find_maximum_sum(self, arr):

        curr = arr[0]
        maximum = curr
        jmax = 1
        i = 0
        for j in range(1, len(arr)):
            #print(i, j, curr)
            if curr > 0:
                curr += arr[j]
            else:
                curr = arr[j]
                i = j

            if curr >= maximum:
                maximum = curr
                jmax = j

        jmax += 1

        return maximum, i, jmax


def example(arr):
    subarray = Subarray()
    result, i, j = subarray.find_maximum_sum(arr)
    print("{} -> {} -> {}".format(arr, arr[i:j], result))
    print("sum(A[{:2d},{:2d}]) = {}\n".format(i, j, sum(arr[i:j])))


if __name__ == '__main__':
    example([1, 6, 5, -8, 4, 9])  # 17
    example([-8, -1, -1])  # -1
    example([1, 6, 5, -8, 4, 9, -3, -2])  # 17
    example([6, 5, -16, 4, 9, -3, -2])  # 13
