import random
import time

import mt19937

def reverse_xor_leftshift_mask(y, shift, nbits, mask):
        '''
        solves an equation of the form "y = ((x << c) & mask) ^ x

        args:
                y:      y in the above equation
                shift:  c in the above equation
                nbits:  number of bits in x and y in the above equation
                mask:   mask in above equation

        returns:
                x such that ((x << c) & mask) ^ x = y
        '''

        x = 0
        for b in range(nbits):
                if b < shift or not (mask & _BIT_0RIGHT(b)):
                        x = x | (y & _BIT_0RIGHT(b))
                elif mask & _BIT_0RIGHT(b):
                        x = x | ((y & _BIT_0RIGHT(b)) ^ ((x << shift) & _BIT_0RIGHT(b)))

        return x


def reverse_xor_rightshift(y, shift, nbits):
        '''
        solves an equation of the form "y = (x >> c) ^ x"

        args:
                y:      y in the above equation
                shift:  c in the above equation
                nbits:   number of bits in x and y in the above equation

        returns:
                x such that (x >> c) ^ x = y
        '''

        x = 0
        for b in range(nbits):
                if b - shift < 0:
                        x = x | (y & _BIT_0LEFT(b, nbits))
                else:
                        x = x | ((y & _BIT_0LEFT(b, nbits)) ^ ((x >> shift) & _BIT_0LEFT(b, nbits)))

        return x

def _BIT_0LEFT(x, nbits):
        '''
        helper function, used for calculating masks

        generates a value b0b1b2...b_nbits such that b_i = 0 for all i
        except i=x
        '''

        return 1 << (nbits - x - 1)

def _BIT_0RIGHT(x):
        '''
        helper function, used for calculating masks
        
        generates a value (b_x)(b_x-1)...b1b0 such that b_i = 0 for all i
        except i=x
        '''

        return 1 << x

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

        for shift in range(1, 16):
                x = reverse_xor_leftshift_mask(0xdead, shift, 16, 0x1234)
                print hex((((x << shift) & 0x1234) ^ x) & 0xffff)
        

if __name__ == '__main__':
        main()
