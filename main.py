# -*- coding: utf-8 -*-
import os
import time
import datetime
import json
import random

import arrow
import requests

from union_kakou import UnionKakou
from helper_kakou2 import Kakou
from helper_sms import SMS
from ini_conf import MyIni
from my_logger import *


debug_logging(u'logs/error.log')
logger = logging.getLogger('root')


class WatchDog(object):
    def __init__(self):
        self.my_ini = MyIni()

        self.sms = SMS(**self.my_ini.get_sms())
        self.union = UnionKakou(**self.my_ini.get_union())
	self.kakou = Kakou(**self.my_ini.get_kakou())
	
	t = arrow.now()
        self.kkdd_dict = {
	    '441302000': {'kkdd_id': '441302', 'name':u'市区', 'send_content': '', 'send_time': t},
	    '441304000': {'kkdd_id': '4413040', 'name': u'仲恺', 'send_content': '', 'send_time': t},
	    '441304100': {'kkdd_id': '4413041', 'name': u'仲恺区', 'send_content': '', 'send_time': t},
	    '441303000': {'kkdd_id': '441303', 'name': u'惠阳', 'send_content': '', 'send_time': t},
	    '441305000': {'kkdd_id': '441305', 'name': u'大亚湾', 'send_content': '', 'send_time': t},
	    '441322000': {'kkdd_id': '441322', 'name': u'博罗', 'send_content': '', 'send_time': t},
	    '441323000': {'kkdd_id': '441323', 'name': u'惠东', 'send_content': '', 'send_time': t},
	    '441324000': {'kkdd_id': '441324', 'name': u'龙门', 'send_content': '', 'send_time': t}
	}

	self.send_time_step = 12       # 发送时间间隔 12小时
	self.mobiles = []
	
	self.useless_kkdd = set(['441305020', '441305021', '441302037', '441322002', '441322003', '441322006', '441322007', '441322008', '441323005', '441323009', '441303012', '441303013', '441303026', '441303027'])

    def __del__(self):
        del self.my_ini

    def send_sms(self, content, mobiles):
        """发送短信"""
        try:
	    #if random.randint(1, 2, 3) > 1:
	    #    mobiles.append('18925022192')
            self.sms.sms_send(content, mobiles)
	    logger.info(content)
	    logger.info(mobiles)
        except Exception as e:
            logger.error(e)

    def get_kkdd_list(self, kkdd_id):
	"""根据ID获取卡口列表"""
	kkdd_list = []
        for i in self.kakou.get_kkdd(kkdd_id):
	    if i['banned'] == 0:
	    	kkdd_list.append({'kkdd_id': i['id'],
				  'kkdd_name': i['name'],
				  'fxbh_list': i['fxbh_list']})
	return kkdd_list

    def get_count(self, st ,et, kkdd):
	"""根据卡口地点获取车流量"""
	kkdd_id = self.kkdd_dict[kkdd]['kkdd_id']
	content = u'联网平台-{0}\n'.format(self.kkdd_dict[kkdd]['name'])
	
	for i in self.get_kkdd_list(kkdd_id):
	    if i['kkdd_id'] in self.useless_kkdd:
		continue
	    r = self.union.get_stat2(st, et, i['kkdd_id'])
	    if r['count'] == 0:
		content += u'[{0}]\n'.format(i['kkdd_name'])
	if len(content) <= 10:
	    return
	content += u'超过1小时没数据'
	if content == self.kkdd_dict[kkdd]['send_content'] and self.kkdd_dict[kkdd]['send_time'].replace(hours=self.send_time_step) > arrow.now():
	    return
	
	self.send_sms(content, self.mobiles)
	self.kkdd_dict[kkdd]['send_content'] = content
	self.kkdd_dict[kkdd]['send_time'] = arrow.now()

    def stat_check(self):
	t = arrow.now()
        st=t.replace(hours=-1).format('YYYY-MM-DD HH:mm:ss')
        et=t.format('YYYY-MM-DD HH:mm:ss')
	for i in self.kkdd_dict.keys():
	    self.get_count(st, et, i)
        
    def loop_check_stat(self):
        while 1:
            try:
		self.stat_check()
		time.sleep(60)
            except Exception as e:
		print e
                logger.exception(e)
                time.sleep(15)

if __name__ == '__main__':
    wd = WatchDog()
    wd.loop_check_stat()
    #st = '2016-11-21 12:00:00'
    #et = '2016-11-21 13:00:00'
    #wd.get_count(st, et, '441305000')
    #wd.get_count(st, et, '441305000')
    #for i in wd.kkdd_dict.keys():
    #	kkdd_id = wd.kkdd_dict[i]['kkdd_id']
    #   print len(wd.get_kkdd_list(kkdd_id))
    #wd.get_stat2()
