#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@software: spider_gateway
@author: 'guodl'
@contact: guodl@auto-smart.com
@file: mongo_adapter.py
@date:2017/5/26
"""

from pymongo import MongoClient
import logging

class MongoAdapter(object):
    """
    Database operation class
    """
    def __init__(self, database):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db_client = self.client[database]


    def get_table_class(self):
        Table_SQL = eval("self.Base.classes." + self.table_name)

        pass

    def query(self,table,where=None,columns=None):
        results = self.db_client[table].find(where,columns)
        return results

    def query1(self, table, where=None):
        """
        根据查询条件， 从指定的table中查询

        :param table:
        :param where: dict object， key 是field name， value是
        :return: 可迭代的结果集，用于遍历结果集
        """
        #results = self.db_client[table].find()

        group = {
            '$group': {
                '_id': "$media_id",
                "last_crawl_time": {'$max': "$crawl_time"},
                'crawl_count' : {"$sum": 1}
            }
        }

        # sort = {'$sort':{"crawl_time": -1}}
        #pipeline = [group, sort]
        #{'$match': {'is_newscar': 1}},
        pipeline = [group]
        results = self.db_client[table].aggregate(pipeline)
        # 等于select media_id,max(crawl_time) as 'last_crawl_time',count(crawl_count) as 'crawl_count'
        # from toutiaohao where is_newscar =1 group by media_id


        return results

    def insert(self, table, record):
        self.db_client[table].insert(record)
        pass

    def update(self, table, record, pri_key):
        """
        根据where条件更新，
        :param record: 字典类型， 用于更新数据到mysql
        :当主键media_id = 上面查询出来的_id进行更新
        :return:
        """
        # print pri_key  #<class 'bson.int64.Int64'>

        #self.db_client[table].replace_one({pri_key: record[pri_key]}, record, True)

        newdict = {key: record[key] for key in ['last_crawl_time','crawl_count']}
        #print newdict
        # 只更新count 和time
        self.db_client[table].update_many({'media_id': pri_key}, {'$set':newdict})

        pass

if __name__ == '__main__':
    """
    单元测试
    """
    md = MongoAdapter('huaxiang')
    result = md.query('user_base',{'cos_id':1001})
    for document in result:
        print(type(document))
        print(document)
    # result1 = md.db_client['label_create'].find({'label_id':1},
    #                                              {'user_id_set':1,'_id':1})
    # result2 = md.db_client['label_create'].find({'label_id': 2},
    #                                             {'user_id_set': 1, '_id': 1})
    # #results = md.query('label_create',{'label_id':1},{'user_id_set':1})
    # for document in result1:
    #     result1 = set(document['user_id_set'])
    # for document in result2:
    #     result2 = set(document['user_id_set'])
    #
    # # user_id_set = dict(results)['user_id_set']
    # # print(user_id_set)
    # print(result1)
    # print(len(result1))
    # print(result2)
    # print(len(result2))
    # results = result1|result2
    # print(results)
    # print(len(results))
