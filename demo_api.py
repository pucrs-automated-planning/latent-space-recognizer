#!/usr/bin/python

import sys
import time

import generate_domain as gd
from subprocess import call

def set_candidate_goals():
    candidates = []
    for x in range(1,7):
        candidates.append('demo/c' + str(x) +'.png' )
    return candidates

def initialize_demo():
    global CANDIDATE_GOALS
    CANDIDATE_GOALS = set_candidate_goals()
    network = gd.set_networks('samples/puzzle_mnist_3_3_36_20000_conv/')
    curr = time.time()    
    gd.set_grp('demo/init.png', 'demo/goal.png', CANDIDATE_GOALS, network, 'domains/mnist_domain.pddl')
    data = open('demo/obs.dat', 'w')
    data.write('')
    data.close()
    print(time.time() - curr)
    print('networks are ready')
    return network

def add_obs(obs_image, network, output):
    state = network.encode(obs_image, True)
    txt = ''
    first = True
    for pre in range(len(state)):
            if not first: txt+= ','
            if state[pre]:  txt+='('+ 'p' + str(pre) + ')'
            else: txt+='(not ('+ 'p' + str(pre) + '))'
            first = False
    data = open(output, 'a')
    data.write(txt+ '\n')
    data.close()


def call_recognizer(domain, problem, hyp, obs, real_hyp):
    call(['java -jar goalrecognizer1.1.jar -uniqueness', domain, problem, hyp, obs, real_hyp])


def main_loop():
    while 1:
        add_obs('demo/init.png', nets, 'demo/obs.dat')
        time.sleep(0.1)
        sys.exit()

if __name__ == '__main__':
    global nets
    nets = initialize_demo()
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
