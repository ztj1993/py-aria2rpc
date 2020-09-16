# -*- coding: utf-8 -*-
# Intro: Aria2 RPC 调用模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.3
# Date: 2020-09-16

import xmlrpc.client as xmlrpclib

__version__ = '0.0.3'


class Aria2Rpc(object):
    def __init__(self, uri='http://127.0.0.1:6800/rpc', secret=None):
        self.rpc_uri = uri
        self.rpc_secret = secret
        self.server = xmlrpclib.ServerProxy(self.rpc_uri, allow_none=True)
        self.aria2 = self.server.aria2

    def call(self, name, *args):
        """通用调用"""
        if self.rpc_secret is not None:
            args = ('token:{}'.format(self.rpc_secret),) + args
        return getattr(self.aria2, name)(*args)

    def add_uri(self, uris, options=None, position=None):
        """添加下载"""
        uris = [uris] if isinstance(uris, str) else uris
        return self.call('addUri', uris, options, position)

    def add_torrent(self, torrent, uris=None, options=None, position=None):
        """添加种子下载"""
        uris = [uris] if isinstance(uris, str) else uris
        torrent = xmlrpclib.Binary(open(torrent, 'rb').read())
        return self.call('addTorrent', torrent, uris, options, position)

    def add_meta_link(self, meta_link, options=None, position=None):
        """添加源连接下载"""
        meta_link = xmlrpclib.Binary(open(meta_link, 'rb').read())
        return self.call('addMetalink', meta_link, options, position)

    def remove(self, gid):
        """移除下载"""
        return self.call('remove', gid)

    def pause(self, gid):
        """暂停下载"""
        return self.call('pause', gid)

    def un_pause(self, gid):
        """取消暂停"""
        return self.call('unpause', gid)

    def tell_status(self, gid):
        """返回指定的下载信息"""
        return self.call('tellStatus', gid)

    def tell_active(self, keys=None):
        """返回正在下载的列表信息"""
        return self.call('tellActive', keys)

    def tell_waiting(self, offset, num, keys=None):
        """返回等待下载的列表信息"""
        return self.call('tellWaiting', offset, num, keys)

    def tell_stopped(self, offset, num, keys=None):
        """返回停止下载的列表信息"""
        return self.call('tellStopped', offset, num, keys)

    def remove_result(self, gid):
        """移除下载结果"""
        return self.call('removeDownloadResult', gid)

    def purge_result(self, gid):
        """清除下载结果"""
        return self.call('purgeDownloadResult', gid)

    def get_version(self):
        """获取版本"""
        return self.call('getVersion')

    def get_global_option(self):
        """获取全局选项"""
        return self.call('getGlobalOption')
