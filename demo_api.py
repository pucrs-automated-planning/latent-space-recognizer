#!/usr/bin/python

import sys
import time

import generate_domain as gd
from subprocess import call
global nets
import numpy as np
from encode_decode import *
import subprocess


class Demo():

    def __init__(self, network='samples/puzzle_mnist_3_3_36_20000_conv/', domain='demo/domain.pddl' , problem='demo/template.pddl', hyp='demo/hyps.dat', obs='demo/obs.dat', real_hyp='demo/real_hyp.dat'):
        print(network)
        self.sae = self.initialize_demo(network)
        self.recognizer = subprocess.Popen(['java', '-jar', 'gc_stop.jar'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.scores = None
        self.obs_list = []
        self.obs_size = 10


    def set_candidate_goals(self):
        candidates = []
        for x in range(1,7):
            candidates.append('demo/c' + str(x) +'.png' )
        return candidates

    def initialize_demo(self, network='samples/puzzle_mnist_3_3_36_20000_conv/'):
        self.candidate_goals = self.set_candidate_goals()
        
        network = gd.set_networks(network)
        curr = time.time()    
        #gd.set_grp('demo/init.png', 'demo/goal.png', self.candidate_goals, network, 'domains/mnist_domain.pddl')
        data = open('demo/obs.dat', 'w')
        data.write('')
        data.close()
        print(time.time() - curr)
        print('networks are ready')
        return network

    def set_initial_state(self, file, path):
        print('Setting', file)
        state = self.sae.encode(file, True)
        gd.export_problem_pgr(state, path)



    def add_obs(self, obs_image, output='demo/obs.dat'):
        print('Adding:', obs_image)
        state = self.sae.encode(obs_image, True)
        print('State:', state)
        txt = ''
        first = True
        for pre in range(len(state)):
                if not first: txt+= ','
                if state[pre]:  txt+='('+ 'p' + str(pre) + ')'
                else: txt+='(not ('+ 'p' + str(pre) + '))'
                first = False
        self.obs_list.append(txt)
        if len(self.obs_list) > self.obs_size: 
            self.obs_list.pop(0)
        data = open(output, 'w')
        for obs in self.obs_list:            
            data.write(obs+ '\n')
        data.close()


  
        #call(['java -jar goalrecognizer1.1.jar -uniqueness', domain, problem, hyp, obs, real_hyp])

    def main_loop(self):
        while 1:
            add_obs('demo/init.png', 'demo/obs.dat')
            call_recognizer('demo/domain.pddl', 'demo/template.pddl', 'demo/hyps.dat', 'demo/obs.dat','demo/real_hyp.dat',)
            time.sleep(0.1)
            sys.exit()

    def predict_best_goal(self, domain='demo/domain.pddl' , problem='demo/template.pddl', hyp='demo/hyps.dat', obs='demo/obs.dat', real_hyp='demo/real_hyp.dat'):
        sp = self.call_recognizer(domain , problem, hyp, obs, real_hyp)
        best_goal = sp[0].split(':')[0]
        binary_goal = []
        for i in range(0,36):
            pred = 'not (p'+str(i)+'))'
            if pred in best_goal:
                binary_goal.append(0)
            else:
                binary_goal.append(1)
        return np.array(binary_goal)

    def call_recognizer(self, domain='demo/domain.pddl' , problem='demo/template.pddl', hyp='demo/hyps.dat', obs='demo/obs.dat', real_hyp='demo/real_hyp.dat'):
       #a = call(['java', '-jar', 'goalrecognizer-obsfacts.jar' ,'-goalcompletion' , domain, problem, hyp, obs, real_hyp, '0.0'])
        from subprocess import Popen, PIPE
        curr = time.time()    
        p = Popen(['java', '-jar', 'looking_better.jar' ,'-goalcompletion' , domain, problem, hyp, obs, real_hyp, '0.0'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output = p.stdout.read()
        print('Rec time:', time.time() - curr)
        sp = str(output).replace('\'', '').replace('b','').split('\\n')
        goals = []
        #print(sp)
        for rank in sp:
            goal = rank.split(':')[0]
            if 'p' not in rank:
                continue 
            binary_goal = []
            for i in range(0,36):
                pred = 'not (p'+str(i)+'))'
                if pred in goal:
                    binary_goal.append(0)
                else:
                    binary_goal.append(1)
            goals.append((np.array(binary_goal),rank.split(':')[1]))
        print('Goals old', goals)
        return goals

    def call_recognizer_static_jar(self):
        self.recognizer.stdin.write(b"r\r\n")
        self.recognizer.stdin.write(b"x\r\n")
        self.recognizer.stdin.flush()
        line = self.recognizer.stdout.readline()
       # print("Line:", line)
        sp = []
        while (line != b"x\n"):
           # print("Line:", line)
            sp.append(str(line).replace('\'', '').replace('\\n',('')))
            #time.sleep(1.0)
            #print('Line:', line)
            line = self.recognizer.stdout.readline()
            if line == b'EOF\n':
             #   print("Line EOF:", line)
                self.recognizer.stdin.write(b"x\r\n")
                self.recognizer.stdin.flush()
                break;
        #print(sp)
        return sp
        #print('Donzo')

    def rank_all_goals(self, domain='demo/domain.pddl' , problem='demo/template.pddl', hyp='demo/hyps.dat', obs='demo/obs.dat', real_hyp='demo/real_hyp.dat'):
        sp = self.call_recognizer_static_jar()
        #sp = self.call_recognizer(domain , problem, hyp, obs, real_hyp)
        goals = []
        for rank in sp:
            goal = rank.split(':')[0]
            if 'p' not in rank:
                continue 
            binary_goal = []
            for i in range(0,36):
                pred = 'not (p'+str(i)+'))'
                if pred in goal:
                    binary_goal.append(0)
                else:
                    binary_goal.append(1)
            goals.append((np.array(binary_goal),rank.split(':')[1]))
        print('Goals', goals)
        return goals

if __name__ == '__main__':
    #demo_api = Demo()
    enc_dec = EncoderDecoder(network_folder)
    init = enc_dec.encode('demo/init.png', True)
    print(init)
    #demo_api.add_obs('demo/init.png','demo/obs.dat')
    #ec = demo_api.predict_best_goal()
    #print(demo_api.sae.decode(ec,False).shape)
    #print(demo_api.rank_all_goals())
    #misc.imsave('demo/predicted_goal.png', demo_api.sae.decode(ec,False)[0])

