import random
import time

import mt19937

def reverse_xor_rightshift(y, shift, nbits):
        '''
        solves an equation of the form "y = (x << c) ^ x"

        args:
                y:      y in the above equation
                shift:  c in the above equation
                bits:   number of bits in x and y in the above equation

        returns:
                x such that (x << c) ^ x = y
        '''

        chunk_len = shift
        chunk_mask = (1 << chunk_len) - 1
        x = 0
        nbits_recovered = 0
        while nbits_recovered + chunk_len <= nbits:
                chunk = (y >> (nbits - nbits_recovered - chunk_len)) & chunk_mask
                x = (x << chunk_len) | ((x & chunk_mask) ^ chunk)
                nbits_recovered = nbits_recovered + chunk_len

        nbits_remaining = (nbits - nbits_recovered)
        last_mask = (1 << (nbits_remaining)) - 1
        last_chunk = y & last_mask
        x = (x << nbits_remaining) | (((x >> (chunk_len - nbits_remaining)) & last_mask) ^ last_chunk)

        return x


def generate_target():
        time.sleep(random.randint(40, 1000))
        mt19937.srand(int(time.time()))
        time.sleep(random.randint(40, 1000))

        return mt19937.rand()

def main():
        # target = generate_target()
        for shift in range(1, 16):
                x = reverse_xor_rightshift(0xbeef, shift, 16)
                print hex(((x >> shift) ^ x) & 0xffff)
        

if __name__ == '__main__':
        main()
