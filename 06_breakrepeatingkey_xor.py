'''
Matasano Crypto Pals
Challenge 6
Jonathan Eskeldson

Takes a filename via commandline.  base64-decodes the file, and attempts to
break a repeating-key XOR encryption.
'''

import sys
from common import *
import operator

SAMPLE_FILENAME = "06_txt"

def main():
        if len(sys.argv) < 2:
                f = open (SAMPLE_FILENAME, "r")
        else:
                f = open (sys.argv[1], "r")

        ct = ""
        for line in f:
                ct += line.rstrip()

        ct = b64decode(ct)

        assert hamming_distance("this is a test", "wokka wokka!!!") == 37

        keysize_distances = dict()
        for poss_keysize in range(2, 50):
                dists = []
                # average edit distance over first 5 blocks
                for i in range(0, 5):
                        dists.append(hamming_distance (ct[2*i*poss_keysize:(2*i+1)*poss_keysize], ct[(2*i+1)*poss_keysize:(2*i+2)*poss_keysize]) / float(poss_keysize))
                keysize_distances[poss_keysize] = sum(dists) / float(len(dists))

        best_candidates = sorted(keysize_distances.iteritems(), key=operator.itemgetter(1))[0:5]

        best_score = 9999
        for candidate in best_candidates:
                poss_keysize = candidate[0]
                blocks = [""] * poss_keysize
                for i in range(len(ct)):
                        blocks[i % poss_keysize] += ct[i]

                key = ""
                for b in blocks:
                        key += chr(break_single_xor(b)[0])
                poss_string = repeat_xor_cipher(key, ct)
                poss_score = score_string(poss_string)
                if poss_score < best_score:
                        best_score = poss_score
                        best_string = poss_string
                        best_candidate = candidate
                        best_key = key

        print best_string
        print best_score
        print best_key
        print best_candidate



if __name__ == '__main__':
        main()
