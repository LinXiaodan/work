#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project: GaoDe_0001
# Author: LXD

import json


def main():
    filename = 'yz-addresss.json'
    save_filename = 'ZB0012_20170710'
    address = []
    name = []
    max_num = 10
    num = 0
    error_num = 0
    output = open(save_filename.encode('utf8'), 'w+')

    with open(filename) as f:
        lines = f.readlines()
        print len(lines)
        empty_num = 0
        for data in lines:
            doc = json.loads(data.decode('utf-8'))
            try:
                temp = doc['address']
                temp_address = ''
                # 一种address为dict， 一种address就是地址
                if isinstance(temp, dict) or isinstance(temp, list):
                    # 一种地址在value中，一种地址在address的value中
                    if 'value' in temp:
                        if isinstance(temp['value'], dict):
                            temp_address = temp['value']['value']
                        else:
                            temp_address = temp['value']
                    elif 'address' in temp:
                        temp_address = temp['address']['value']
                else:
                    temp_address = temp
                # 删掉地址为空的情况
                if not temp_address == '':
                    address.append(temp_address)
                    name.append(doc.get('name', ''))
                else:
                    print 'address empty', temp
                    empty_num = empty_num + 1
                    continue

            except Exception as e:
                print 'decode error', doc
                error_num = error_num + 1
                continue

            num = num + 1
            if num % max_num == 0 or num == len(lines):
                str1 = '|'.join(address)
                str2 = '|'.join(name)
                str = str1 + '#split#' + str2
                # print str
                if isinstance(str, unicode):
                    output.write(str.encode('utf8'))
                else:
                    output.write(str)
                output.write('\n')
                address = []
                name = []
    output.close()
    print 'error_num:', error_num
    print 'empty_num', empty_num

if __name__ == '__main__':
    main()