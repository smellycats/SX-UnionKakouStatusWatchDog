# -*- coding: utf-8 -*-
import json

import requests


class UnionKakou(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        
        self.headers = {'content-type': 'application/json'}
        
        self.status = False

    def get_maxid(self):
        """获取最大ID值"""
        url = u'http://{0}:{1}/alarm_maxid'.format(self.host, self.port)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_vehicle_by_id(self, _id):
        """根据ID范围获取车辆信息"""
        url = u'http://{0}:{1}/alarm/{2}'.format(
            self.host, self.port, _id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_kkdd_by_id(self, kkdd_id):
        """根据车牌号码获取布控信息"""
        url = u'http://{0}:{1}/kkdd/{2}'.format(
            self.host, self.port, kkdd_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_stat(self, st, et, kkdd_id):
        """根据车牌号码获取布控信息"""
        url = u'http://{0}:{1}/stat/{2}/{3}/{4}'.format(
            self.host, self.port, st, et, kkdd_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_stat2(self, st, et, kkdd_id):
        """根据车牌号码获取布控信息"""
        url = u'http://{0}:{1}/stat2/{2}/{3}/{4}'.format(
            self.host, self.port, st, et, kkdd_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_traffic_crossing_info(self, unit_id):
        """获取卡口地点信息"""
        url = u'http://{0}:{1}/traffic_crossing_info/{2}'.format(
            self.host, self.port, unit_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_traffic_direction_info(self, crossing_id):
        """获取卡口方向信息"""
        url = u'http://{0}:{1}/traffic_direction_info/{2}'.format(
            self.host, self.port, crossing_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_traffic_lane_info(self, direction_id):
        """获取车道信息"""
        url = u'http://{0}:{1}/traffic_lane_info/{2}'.format(
            self.host, self.port, direction_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


