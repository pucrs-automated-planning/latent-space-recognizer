#!/bin/bash -x


#MNIST

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb01 output/pb01_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb02 output/pb02_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb03 output/pb03_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb04 output/pb04_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb05 output/pb05_mnist_out_10 domains/mnist_actions.csv 10

./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_100 domains/mnist_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_70 domains/mnist_actions.csv 70
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_50 domains/mnist_actions.csv 50
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_30 domains/mnist_actions.csv 30
./generate_domain.py recon samples/puzzle_mnist_3_3_36_20000_conv/ domains/mnist_domain.pddl problems/mnist/pb06 output/pb06_mnist_out_10 domains/mnist_actions.csv 10

#SPIDER

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb01 output/pb01_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb02 output/pb02_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb03 output/pb03_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb04 output/pb04_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb05 output/pb05_spider_out_10 domains/spider_actions.csv 10

./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_100 domains/spider_actions.csv 100 True
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_70 domains/spider_actions.csv 70
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_50 domains/spider_actions.csv 50
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_30 domains/spider_actions.csv 30
./generate_domain.py recon samples/puzzle_spider_3_3_36_20000_conv/ domains/spider_domain.pddl problems/spider/pb06 output/pb06_spider_out_10 domains/spider_actions.csv 10

#MANDRILL

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb01 output/pb01_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb02 output/pb02_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb03 output/pb03_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb04 output/pb04_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb05 output/pb05_mandrill_out_10 domains/mandrill_actions.csv 10

./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_100 domains/mandrill_actions.csv 100 True
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_70 domains/mandrill_actions.csv 70
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_50 domains/mandrill_actions.csv 50
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_30 domains/mandrill_actions.csv 30
./generate_domain.py recon samples/puzzle_mandrill_3_3_36_20000_conv/ domains/mandrill_domain.pddl problems/mandrill/pb06 output/pb06_mandrill_out_10 domains/mandrill_actions.csv 10

#LODIGITAL
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb01 output/pb01_lodigital_out_100 domains/lodigital_actions.csv 100 True
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb01 output/pb01_lodigital_out_70 domains/lodigital_actions.csv 70
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb01 output/pb01_lodigital_out_50 domains/lodigital_actions.csv 50
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb01 output/pb01_lodigital_out_30 domains/lodigital_actions.csv 30
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb01 output/pb01_lodigital_out_10 domains/lodigital_actions.csv 10

./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb02 output/pb02_lodigital_out_100 domains/lodigital_actions.csv 100 True
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb02 output/pb02_lodigital_out_70 domains/lodigital_actions.csv 70
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb02 output/pb02_lodigital_out_50 domains/lodigital_actions.csv 50
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb02 output/pb02_lodigital_out_30 domains/lodigital_actions.csv 30
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb02 output/pb02_lodigital_out_10 domains/lodigital_actions.csv 10

./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb03 output/pb03_lodigital_out_100 domains/lodigital_actions.csv 100 True
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb03 output/pb03_lodigital_out_70 domains/lodigital_actions.csv 70
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb03 output/pb03_lodigital_out_50 domains/lodigital_actions.csv 50
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb03 output/pb03_lodigital_out_30 domains/lodigital_actions.csv 30
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb03 output/pb03_lodigital_out_10 domains/lodigital_actions.csv 10

./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb04 output/pb04_lodigital_out_100 domains/lodigital_actions.csv 100 True
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb04 output/pb04_lodigital_out_70 domains/lodigital_actions.csv 70
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb04 output/pb04_lodigital_out_50 domains/lodigital_actions.csv 50
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb04 output/pb04_lodigital_out_30 domains/lodigital_actions.csv 30
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb04 output/pb04_lodigital_out_10 domains/lodigital_actions.csv 10

./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb05 output/pb05_lodigital_out_100 domains/lodigital_actions.csv 100 True
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb05 output/pb05_lodigital_out_70 domains/lodigital_actions.csv 70
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb05 output/pb05_lodigital_out_50 domains/lodigital_actions.csv 50
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb05 output/pb05_lodigital_out_30 domains/lodigital_actions.csv 30
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb05 output/pb05_lodigital_out_10 domains/lodigital_actions.csv 10

./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb06 output/pb06_lodigital_out_100 domains/lodigital_actions.csv 100 True
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb06 output/pb06_lodigital_out_70 domains/lodigital_actions.csv 70
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb06 output/pb06_lodigital_out_50 domains/lodigital_actions.csv 50
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb06 output/pb06_lodigital_out_30 domains/lodigital_actions.csv 30
./generate_domain.py recon samples/lightsout_digital_4_36_20000_conv/ domains/lodigital_domain.pddl problems/lodigital/pb06 output/pb06_lodigital_out_10 domains/lodigital_actions.csv 10


#LOTWISTED
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb01 output/pb01_lotwisted_out_100 domains/lotwisted_actions.csv 100 True
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb01 output/pb01_lotwisted_out_70 domains/lotwisted_actions.csv 70
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb01 output/pb01_lotwisted_out_50 domains/lotwisted_actions.csv 50
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb01 output/pb01_lotwisted_out_30 domains/lotwisted_actions.csv 30
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb01 output/pb01_lotwisted_out_10 domains/lotwisted_actions.csv 10

./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb02 output/pb02_lotwisted_out_100 domains/lotwisted_actions.csv 100 True
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb02 output/pb02_lotwisted_out_70 domains/lotwisted_actions.csv 70
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb02 output/pb02_lotwisted_out_50 domains/lotwisted_actions.csv 50
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb02 output/pb02_lotwisted_out_30 domains/lotwisted_actions.csv 30
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb02 output/pb02_lotwisted_out_10 domains/lotwisted_actions.csv 10

./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb03 output/pb03_lotwisted_out_100 domains/lotwisted_actions.csv 100 True
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb03 output/pb03_lotwisted_out_70 domains/lotwisted_actions.csv 70
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb03 output/pb03_lotwisted_out_50 domains/lotwisted_actions.csv 50
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb03 output/pb03_lotwisted_out_30 domains/lotwisted_actions.csv 30
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb03 output/pb03_lotwisted_out_10 domains/lotwisted_actions.csv 10

./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb04 output/pb04_lotwisted_out_100 domains/lotwisted_actions.csv 100 True
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb04 output/pb04_lotwisted_out_70 domains/lotwisted_actions.csv 70
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb04 output/pb04_lotwisted_out_50 domains/lotwisted_actions.csv 50
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb04 output/pb04_lotwisted_out_30 domains/lotwisted_actions.csv 30
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb04 output/pb04_lotwisted_out_10 domains/lotwisted_actions.csv 10

./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb05 output/pb05_lotwisted_out_100 domains/lotwisted_actions.csv 100 True
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb05 output/pb05_lotwisted_out_70 domains/lotwisted_actions.csv 70
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb05 output/pb05_lotwisted_out_50 domains/lotwisted_actions.csv 50
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb05 output/pb05_lotwisted_out_30 domains/lotwisted_actions.csv 30
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb05 output/pb05_lotwisted_out_10 domains/lotwisted_actions.csv 10

./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb06 output/pb06_lotwisted_out_100 domains/lotwisted_actions.csv 100 True
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb06 output/pb06_lotwisted_out_70 domains/lotwisted_actions.csv 70
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb06 output/pb06_lotwisted_out_50 domains/lotwisted_actions.csv 50
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb06 output/pb06_lotwisted_out_30 domains/lotwisted_actions.csv 30
./generate_domain.py recon samples/lightsout_twisted_4_36_20000_conv/ domains/lotwisted_domain.pddl problems/lotwisted/pb06 output/pb06_lotwisted_out_10 domains/lotwisted_actions.csv 10
