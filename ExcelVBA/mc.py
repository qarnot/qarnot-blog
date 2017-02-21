#!/usr/bin/python

import random, sys, os
import numpy as np

parameterFile = sys.argv[1]
frameId = int(sys.argv[2])

LENGTH = 10**5
CENTER = [LENGTH/2,LENGTH/2]

def in_circle(point):
    x = point[0]
    y = point[1]
    center_x = CENTER[0]
    center_y = CENTER[1]
    radius = LENGTH/2
    return (x - center_x)**2 + (y - center_y)**2 < radius**2

def piMc(seed, samples):
    random.seed(seed)
    count = inside_count = 0
    i = samples
    while i>0:
        if i % (samples / 100) == 0:
            print str(((samples - i)*100)/samples) + "/100"  #display progress
        point = random.randint(1,LENGTH),random.randint(1,LENGTH)
        if in_circle(point):
            inside_count += 1
        count += 1
        i = i-1
    return 4.0 * (inside_count * 1.0 / count)


def main(parameterFile, frameId):
#    if random.randint(0, 10) % 4 == 0:
#        raise Exception('Error simulation')
    with open(parameterFile) as fp:
        for lineNb, line in enumerate(fp):
            if lineNb == frameId+1:
                params = line.split()
                result = piMc(int(params[0]), int(params[1]))
                with open(str(frameId) + ".txt", "w+") as fpResult:
                    fpResult.write(str(result) + "\n")
            elif lineNb > frameId:
                break

if __name__ == "__main__":
    main(parameterFile, frameId)
