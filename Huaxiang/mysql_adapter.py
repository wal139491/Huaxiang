#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey


class MySQLAdapter(object):
    """
    Database operation class
    """
    def __init__(self, config):
        engine = create_engine(config['conn_string'])
        self.Session = sessionmaker(bind=engine)
        self.table_name = config['table']

        # produce our own MetaData object
        metadata = MetaData()

        # we can reflect it ourselves from a database, using options
        # such as 'only' to limit what tables we look at...
        metadata.reflect(engine, only=[self.table_name])

        # we can then produce a set of mappings from this MetaData.
        self.Base = automap_base(metadata=metadata)
        # calling prepare() just sets up mapped classes and relationships.
        self.Base.prepare()


    def insert(self, table, record):
        Table_SQL = eval("self.Base.classes." + table)
        pass

    def update(self, table, record, where):
        """
        根据where条件更新，
        :param record: 字典类型， 用于更新数据到mysql
        :param where: 字符串类型， 更新条件
        :return:
        """
        Table_SQL = eval("self.Base.classes." + table)
        filed_dyn = eval("self.Base.classes." + table + "." + where)

        session = self.Session()

        result = session.query(Table_SQL).filter(filed_dyn == record[where])
        if record['biz']:
            result.update({Table_SQL.biz : record['biz'], Table_SQL.last_time:record['last_time']})
        session.commit()

        pass

if __name__ == '__main__':
    """
    单元测试
    """
    pass