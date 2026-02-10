def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x > 0:
            temp = x % 10
            x = x // 10

            rev = rev * 10 + temp

        rev = sign * rev

        if (-2 ** 31) < rev < ((2 ** 31) - 1):
            return rev
        else:
            return 0

        """hacked approach"""


"""use
strings and reverse"""



def reverse_optimal(self, x: int) -> int:
        x = str(x)

        if x[0] == '-':
            x = "-" + x[:0:-1]


        else:
            x = x[::-1]

        g = int(x)

        if g < -2 ** 31 or g > 2 ** 31 - 1:
            return 0
        return g