#!/usr/bin/env python
#coding=utf-8
#pip install visdom
# python -m visdom.server 
# python -m debugpy --listen 0.0.0.0:5678 main.py --trainpath=.\data\train\ --testpath=.\data\test\
# python main.py --trainpath=.data/train/ --testpath=./data/userTest
from pkg_resources import require
from parameters import *
from model import *
from train import *
import time
import argparse

if __name__ == '__main__':
    time.sleep(10)
    net = ResNet(ResidualBlock)
    net.loadIfExist()
    '''
    for elem in net.named_parameters():
        print(elem)
    '''
    parser = argparse.ArgumentParser(description='train captcha prediction model with CNN+ResNet')
    parser.add_argument('--trainpath', type=str, required=True, help="train data path")
    parser.add_argument('--testpath', type=str, required=True, help="test data path")
    args = parser.parse_args()
    train(net, args.trainpath, args.testpath)