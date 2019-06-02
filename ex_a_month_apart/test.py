class Solution:
    LENGTH_OF_MONTH = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    @staticmethod
    def func(date1, date2):
        m1, d1, y1 = [int(x) for x in date1.split('/')]
        m2, d2, y2 = [int(x) for x in date2.split('/')]

        print(m1, d1, y1)
        print(m2, d2, y2)

        if y2 < y1:
            return False
        elif y2 == y1: # same year
            if m2 <= m1:
                return False
            elif m2 > m1 + 1:
                return True
            else: # m2 = m1 + 1
                return d2 >= d1

        else: # y2 > y1
            if y2 == y1+1 and m2 == 1 and m1 == 12:
                return d2 >= d1
            else:
                return False

def main():
    input1 = {'date1' : '2/15/2018',
              'date2' : '2/18/2018'}

    input2 = {'date1' : '3/4/2018',
              'date2' : '4/5/2018'}

    input3 = {'date1' : '12/2/2017',
              'date2' : '1/1/2018'}

    input_list = [input1, input2, input3]

    sol = Solution()
    for inp in input_list:
        print(sol.func(**inp))


if __name__ == "__main__":
    main()