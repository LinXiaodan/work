#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-7-21
# Author: LXD
# 读取batch_6中的省份名单，与has_report_namelist中对应省份名单对比，得到差值，保存到no_report_namelist文件夹对应省份名的文件中

import os
import time


def readfile(filepath):
    """
    :param filepath: 文件路径
    :return: list(文件内容按行放置在list中)
    """
    new_list = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            new_list.append(line.strip('\n'))
    return new_list


def writefile(filepath, save_list):
    """
    将list中的每一项按照行存到文件中
    :param filepath: 文件路径+文件名
    :param save_list: 要保存的list
    :return: None
    """
    if isinstance(filepath, unicode):
        filepath = filepath.encode('utf8')

    path = os.path.dirname(filepath)
    if not os.path.exists(path):
        os.makedirs(path)

    with open(filepath, 'w+') as output:
        for i in save_list:
            if isinstance(i, unicode):
                output.write(i.encode('utf8'))
            else:
                output.write(i)
            output.write('\n')


def differ_of_province(dirname1, dirname2=None, savedir=None):
    """
    循环：读取dirname1中的文件1，在dirname2中找到相同名字的文件2并读取，将在文件1中出现但是在文件2中没有的名单保存到savedir中相同名字的文件夹中
    :param dirname1: 
    :param dirname2: 
    :param savedir: 
    :return: 
    """
    pathDir = os.listdir(dirname1)
    pathDirhas = os.listdir(dirname2)  # 有年报名单的文件名
    for dir in pathDir:
        if dir in pathDirhas:
            filepath1 = os.path.join(dirname1, dir)
            all_list = readfile(filepath1)

            filepath2 = os.path.join(dirname2, dir)
            has_report_list = readfile(filepath2)
            print '地区：', dir, '， 公司数目：', len(all_list), '， 有年报公司的数目：', len(has_report_list)

            no_report_list = list(set(all_list) - set(has_report_list))
            print len(no_report_list)

            savepath = os.path.join(savedir, dir)
            writefile(savepath, no_report_list)
        else:
            print 'all has no report:', dir

if __name__ == '__main__':
    # a_list = readfile('batch_6/all_namelist/上海')
    # writefile(unicode('test/test/test中', 'utf8'), ['aaa', 'bbb', '中国'])
    differ_of_province('batch_6/all_namelist', 'batch_6/has_report_namelist',
                       'batch_6/test/no_report_namelist_{}'.format(int(time.time()*1000)))