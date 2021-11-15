#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import signal
import subprocess
import gevent
import gevent.pool
from gevent import monkey;monkey.patch_all()


def custom_print(content,colour='white'):
    """
    写入日志文件
    :param content: 内容
    :param colour: 颜色
    :return: None
    """
    # 颜色代码
    colour_dict = {
        'red': 31,  # 红色
        'green': 32,  # 绿色
        'yellow': 33,  # 黄色
        'blue': 34,  # 蓝色
        'purple_red': 35,  # 紫红色
        'bluish_blue': 36, # 浅蓝色
        'white': 37,  # 白色
    }
    choice = colour_dict.get(colour)  # 选择颜色

    info = "\033[1;{};1m{}\033[0m".format(choice, content)
    print(info)


def execute_linux2(cmd, timeout=10, skip=False):
    """
    执行linux命令,返回list
    :param cmd: linux命令
    :param timeout: 超时时间,生产环境, 特别卡, 因此要3秒
    :param skip: 是否跳过超时限制
    :return: list
    """
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,shell=True,close_fds=True,preexec_fn=os.setsid)

    t_beginning = time.time()  # 开始时间
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if not skip:
            if seconds_passed > timeout:
                # p.terminate()
                # p.kill()
                # raise TimeoutError(cmd, timeout)
                custom_print('错误, 命令: {},本地执行超时!'.format(cmd),"red")
                # 当shell=True时，只有os.killpg才能kill子进程
                try:
                    # time.sleep(1)
                    os.killpg(p.pid, signal.SIGUSR1)
                except Exception as e:
                    pass
                return False

    result = p.stdout.readlines()  # 结果输出列表
    return result


class NetworkTest(object):
    def __init__(self):
        self.flag_list = []

    def check_ping(self,ip):
        """
        检查ping
        :param ip: ip地址
        :return: none
        """
        cmd = "ping %s -c 2" % ip
        # print(cmd)
        # 本机执行命令
        res = execute_linux2(cmd,2)
        # print(res)
        if not res:
            custom_print("错误, 执行命令: {} 失败".format(cmd), "red")
            self.flag_list.append(False)
            return False

        res.pop()  # 删除最后一个元素
        last_row = res.pop().decode('utf-8').strip()  # 再次获取最后一行结果
        if not last_row:
            custom_print("错误，执行命令: {} 异常","red")
            self.flag_list.append(False)
            return False

        res = last_row.split()  # 切割结果
        # print(res,type(res),len(res))
        if len(res) <10:
            custom_print("错误，切割 ping 结果异常","red")
            self.flag_list.append(False)
            return False

        if res[5] == "0%":  # 判断丢包率
            custom_print("正常, ip: {} ping正常 丢包率0%".format(ip), "green")
        else:
            self.flag_list.append(False)
            custom_print("错误, ip: {} ping异常 丢包率100%".format(ip), "red")

    def main(self):
        """
        主程序
        :return:
        """
        process_list = []
        for num in range(1, 256):
            ip = '192.168.10.{}'.format(num)
            # self.check_ping(ip)
            # 将任务加到列表中
            process_list.append(gevent.spawn(self.check_ping, ip))

        gevent.joinall(process_list)  # 等待所有协程结束


if __name__ == '__main__':
    startime = time.time()  # 开始时间

    NetworkTest().main()

    endtime = time.time()
    take_time = endtime - startime

    if take_time < 1:  # 判断不足1秒时
        take_time = 1  # 设置为1秒
    # 计算花费时间
    m, s = divmod(take_time, 60)
    h, m = divmod(m, 60)

    custom_print("本次花费时间 %02d:%02d:%02d" % (h, m, s), "green")