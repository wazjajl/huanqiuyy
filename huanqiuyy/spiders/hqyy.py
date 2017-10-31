#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from huanqiuyy.items import HuanqiuyyItem

class HuanqiuyySpider(scrapy.Spider):
    name = 'hqyy'

    def start_requests(self):
	#pages = 8196
        pages = 8196
        for id in range(1, pages + 1):
            page_url = 'http://www.qgyyzs.net/zs_%s.htm' % id
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        for product_url in response.css('div.r_list').xpath('a/@href').extract():
            yield scrapy.Request(url=product_url, callback=self.parse_question)

    def parse_question(self, response):
        cs_product_name = 'div.r_mina h1::text'
        cs_product_tag = 'div.r_mina dd a.linkblue::text'
        re_product_point = '产品卖点： '.decode('utf8') + '((?:.|\n)*?)<br>'
        re_product_category = '[f/]">(.*?)</a>'
        re_investment_area = '招商区域： '.decode('utf8') + '((?:.|\n)*?)<br>'
        re_manufacture_factory = '生产单位： '.decode('utf8') + '((?:.|\n)*?)<br>'
	re_approval_number = '批准文号： '.decode('utf8') + '((?:.|\n)*?)' + '[【'.decode('utf8') + '<]'
        re_product_specifications = '规　　格： '.decode('utf8') + '((?:.|\n)*?)<br>'
        re_product_ingredients = '成　　份： '.decode('utf8') + '((?:.|\n)*?)<br>'
        re_product_usage = '用法用量： '.decode('utf8') + '((?:.|\n)*?)<br>'
        re_product_pack = '包　　装： '.decode('utf8') + '((?:.|\n)*?)<br>'
        re_product_function_01 = '产品用途'.decode('utf8') + '.*?<dd>((?:.|\n)*?)</dd>'
        re_product_function_02 = '产品用途'.decode('utf8') + '.*?<dd>((?:.|\n)*?)</dd>'
	re_contact_name = '联 系 人：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)<br>'
	re_telphone = '电　　话：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)' + '（联系'.decode('utf8')
	re_fax = '传　　真：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)<br>'
	re_mobilephone = '联系手机：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)<br>'
	re_address = '地　　址：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)<br>'
	re_qq = '系 QQ：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)<a'
	re_wechat = '联系微信：'.decode('utf8') + u'\xa0' + '((?:.|\n)*?)<br>'
	re_mail = '公司邮箱：'.decode('utf8') + u'\xa0' + '.*?>((?:.|\n)*?)</a>'
	# 生成ItemLoder实例
        item_list = ItemLoader(item=HuanqiuyyItem(), response=response)
	#(0)html文件名
	item_list.add_value('product_url', response.url)
	#(1)产品名称
        product_name = response.css(cs_product_name).extract()
        if product_name:
            item_list.add_value('product_name', product_name)
        else:
            item_list.add_value('product_name', 'None')
	#(2)产品标签
	product_tag = response.css(cs_product_tag).extract()
	if product_tag:
	    item_list.add_value('product_tag', product_tag)
	else:
	    item_list.add_value('product_tag', 'None')
	#(3)产品卖点
        product_point = response.css('div.r_mina dd')[0].re(re_product_point)
        if product_point == [] or product_point == [u' ']:
            item_list.add_value('product_point', 'None')
        else:
            item_list.add_value('product_point', product_point)
	#(4)产品类型
        product_category = response.css('div.r_mina dd')[0].re(re_product_category)
        if product_category:
            item_list.add_value('product_category', product_category)
        else:
            item_list.add_value('product_category', 'None')
	#(5)招商区域
        investment_area = response.css('div.r_mina dd')[0].re(re_investment_area)
        if investment_area:
            item_list.add_value('investment_area', investment_area)
        else:
            item_list.add_value('investment_area', 'None')
	#(6)生产单位
        manufacture_factory = response.css('div.r_mina dd')[0].re(re_manufacture_factory)
        if manufacture_factory:
            item_list.add_value('manufacture_factory', manufacture_factory)
        else:
            item_list.add_value('manufacture_factory', 'None')
	#(7)批准文号
	approval_number = response.css('div.r_mina dd')[0].re(re_approval_number)
	if approval_number:
	    item_list.add_value('approval_number', approval_number)
        else:
            item_list.add_value('approval_number', 'None')
	#(8)规　　格
        product_specifications = response.css('div.r_mina dd')[0].re(re_product_specifications)
        if product_specifications:
            item_list.add_value('product_specifications', product_specifications)
        else:
            item_list.add_value('product_specifications', 'None')
	#(9)成　　份
        product_ingredients = response.css('div.r_mina dd')[0].re(re_product_ingredients)
        if product_ingredients:
            item_list.add_value('product_ingredients', product_ingredients)
        else:
            item_list.add_value('product_ingredients', 'None')
	#(10)用法用量
        product_usage = response.css('div.r_mina dd')[0].re(re_product_usage)
        if product_usage:
            item_list.add_value('product_usage', product_usage)
        else:
            item_list.add_value('product_usage', 'None')
	#(11)包　　装
        product_pack = response.css('div.r_mina dd')[0].re(re_product_pack)
        if product_pack:
            item_list.add_value('product_pack', product_pack)
        else:
            item_list.add_value('product_pack', 'None')
	#(12)产品用途或者功能主治
        product_function_01 = response.css('div.r_mina dl').re(re_product_function_01)
        product_function_02 = response.css('div.r_mina dl').re(re_product_function_02)
        if product_function_01:
            item_list.add_value('product_function', product_function_01)
        elif product_function_02:
            item_list.add_value('product_function', product_function_02)
        else:
            item_list.add_value('product_function', 'None')
	#(13)联系人
        contact_name = response.css('div.r_mina').re(re_contact_name)
        if contact_name:
            item_list.add_value('contact_name', contact_name)
        else:
            item_list.add_value('contact_name', 'None')
	#(14)电  话	
        telphone = response.css('div.r_mina').re(re_telphone)
        if telphone:
            item_list.add_value('telphone', telphone)
        else:
            item_list.add_value('telphone', 'None')
	#(15)传真		
        fax = response.css('div.r_mina').re(re_fax)
        if fax:
            item_list.add_value('fax', fax)
        else:
            item_list.add_value('fax', 'None')
	#(16)联系手机		
        mobilephone = response.css('div.r_mina').re(re_mobilephone)
        if mobilephone:
            item_list.add_value('mobilephone', mobilephone)
        else:
            item_list.add_value('mobilephone', 'None')
	#(17)地址	
        address = response.css('div.r_mina').re(re_address)
        if address:
            item_list.add_value('address', address)
        else:
            item_list.add_value('address', 'None')
	#(18)联系QQ		
        qq = response.css('div.r_mina').re(re_qq)
        if qq:
            item_list.add_value('qq', qq)
        else:
            item_list.add_value('qq', 'None')
	#(19)联系微信
        wechat = response.css('div.r_mina').re(re_wechat)
        if wechat:
            item_list.add_value('wechat', wechat)
        else:
            item_list.add_value('wechat', 'None')
	#(20)公司邮箱	
        mail = response.css('div.r_mina').re(re_mail)
        if mail:
            item_list.add_value('mail', mail)
        else:
            item_list.add_value('mail', 'None')
        return item_list.load_item()
	#print item_list.load_item()



