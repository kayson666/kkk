#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import pandas as pd
import redis


project_path = '/home/sunzhaoyang/PycharmProjects/kkk-main/kkk/标准化'
# 构建同义词字典
def get_Synonym_map(file_list):
    '''
    :param file_list: 同义词文件列表
    :return: 同义词字典
    '''

    all_synonym_map = {}
    standard_list = []
    for file in file_list:
        synonym_map = {}
        df = pd.read_excel(os.path.join(project_path, file))
        df.fillna('', inplace=True)
        # 取第一列
        name = df.iloc[:, 0]
        standard_list.extend(name)
        # 取同义词列
        synonym = df['同义词']
        # 合并
        df = pd.concat([name, synonym], axis=1)
        items_list = df.to_records()
        for v_iter in items_list:
            v_list = list(v_iter)
            other_names = re.split('[,，、]', v_list[2])
            for name in other_names:
                if not name: continue
                synonym_map[name] = v_list[1]
        all_synonym_map[file[0:2]] = synonym_map

    return all_synonym_map, standard_list

if __name__ == '__main__':
    file_list = [
        '药物标准化术语表.xlsx',
        '症状标准化术语表.xlsx',
        '方剂标准化术语表.xlsx',
        '证型标准化术语表.xlsx',
        '疾病标准化术语表.xlsx',
    ]
    Synonym_map, standard_list = get_Synonym_map(file_list)
    print(Synonym_map, standard_list)
    """
    redis存储
    """
    # 连接redis,选择存储在db2
    r = redis.Redis(host='121.4.242.85', port=6379, password="Cetc28-redis-prod", decode_responses=True, db=2)

    # 清空数据库
    r.flushdb()

    # 存储Synonym_map到Redis哈希表中
    for key, value in Synonym_map.items():
        r.set(key, str(value))

    # 连接到db3
    r3 = redis.Redis(host='121.4.242.85', port=6379, password="Cetc28-redis-prod", decode_responses=True, db=3)
    r3.flushdb()
    r3.set('standard_list', str(standard_list))

