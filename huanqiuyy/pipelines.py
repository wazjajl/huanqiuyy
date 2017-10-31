# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql

class InsertMysqlPipeline(object):
    def __init__(self):
        self.set_utf8_sql = "set character_set_client='utf8';\
                    set character_set_filesystem='utf8';\
                    set character_set_results=utf8;\
                    set character_set_connection=utf8;\
                    set character_set_database=utf8;"
        self.s_connect = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    passwd='',
                    db='hqyy_db',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor,
                    autocommit=False,)

    def process_item(self, item, spider):
        #try:
        with self.s_connect.cursor() as s_cursor:
            s_cursor.execute(self.set_utf8_sql)
    	
            # 循环整个item字典，然后将里面数据按字段存入数据库
	    product_url = item['product_url'][0].encode('utf8')
	    product_name = item['product_name'][0].encode('utf8')
	    product_tag = item['product_tag'][0].encode('utf8')
	    product_point = item['product_point'][0].encode('utf8')
	    product_category = item['product_category'][0].encode('utf8')
	    investment_area = item['investment_area'][0].encode('utf8')
	    manufacture_factory = item['manufacture_factory'][0].encode('utf8')
	    approval_number = item['approval_number'][0].encode('utf8')
	    product_specifications = item['product_specifications'][0].encode('utf8')
	    product_ingredients = item['product_ingredients'][0].encode('utf8')
	    product_usage = item['product_usage'][0].encode('utf8')
	    product_pack = item['product_pack'][0].encode('utf8')
	    product_function = item['product_function'][0].encode('utf8')
	    contact_name = item['contact_name'][0].encode('utf8')
	    telphone = item['telphone'][0].encode('utf8')
	    fax = item['fax'][0].encode('utf8')
	    mobilephone = item['mobilephone'][0].encode('utf8')
	    address = item['address'][0].encode('utf8')
	    qq = item['qq'][0].encode('utf8')
	    wechat = item['wechat'][0].encode('utf8')
	    mail = item['mail'][0].encode('utf8')
            sql = 'insert into hqyy_product values( NULL, \'{}\', \
		\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\', \
		\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'\
                .format(product_url,\
		product_name,\
		product_tag,\
		product_point,\
		product_category,\
		investment_area,\
		manufacture_factory,\
		approval_number,\
		product_specifications,\
		product_ingredients,\
		product_usage,\
		product_pack,\
		product_function,\
		contact_name,\
		telphone,\
		fax,\
		mobilephone,\
		address,\
		qq,\
		wechat,\
		mail)
            s_cursor.execute(sql)
            self.s_connect.commit()
        #finally:
        #    self.s_connect.close()


