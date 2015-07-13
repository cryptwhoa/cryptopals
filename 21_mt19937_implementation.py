import common
import random
import sys

_MT = [0] * 624
_index = 0

def srand(seed):
        global _MT
        global _index

        _index = 0
        _MT[0] = seed & 0xffffffffL
        for i in range(1, 624):
                _MT[i] = (0x6c078965L * (_MT[i-1] ^ (_MT[i-1] >> 30)) + i) & 0xffffffffL

def _gen():
        global _MT

        for i in range(624):
                y = (_MT[i] & 0x80000000L) + (_MT[(i+1) % 624] & 0x7fffffffL)
                _MT[i] = _MT[(i+397) % 624] ^ (y >> 1)
                if y % 2 != 0:
                        _MT[i] = _MT[i] ^ 0x9908b0dfL

def rand():
        global _MT
        global _index

        if _index == 0:
                _gen()

        y = _MT[_index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 0x9d2c5680L)
        y = y ^ ((y << 15) & 0xefc60000L)
        y = y ^ (y >> 18)

        _index = (_index + 1) % 624
        return y

def main():
        seed = int(sys.argv[1])

        srand(seed)

        for i in range(1000):
                print "%08x" % (rand())

if __name__ == '__main__':
        main()
