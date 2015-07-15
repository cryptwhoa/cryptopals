import random
import time

import mt19937

def generate_target():
        time.sleep(random.randint(40, 1000))
        mt19937.srand(int(time.time()))
        time.sleep(random.randint(40, 1000))

        return mt19937.rand()

def main():
        target = generate_target()
        now = int(time.time())
        print "now = %d" % (now)
        for i in range(3000):
                mt19937.srand(now - i)
                candidate = mt19937.rand()
                if candidate == target:
                        print "possible match: %d" % (now - i)

if __name__ == '__main__':
        main()
