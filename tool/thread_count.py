import argparse

import psutil


def print_threads_count_by_name(process_name):
    # 标记是否找到对应的进程
    found = False

    # 遍历所有进程
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if process.info['cmdline']:
                if process_name in ' '.join(process.info['cmdline']):
                    found = True
                    # 获取线程数
                    thread_count = process.num_threads()
                    print(f"进程名称: {process_name}, 进程ID: {process.info['pid']}, 线程数: {thread_count}, {process.info['cmdline']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        print(f"未找到进程: {process_name}")

# 设置命令行参数解析
parser = argparse.ArgumentParser(description='获取指定进程的线程数和命令行信息')
parser.add_argument('process_name', type=str, help='要查询的进程名称')

# 解析命令行参数
args = parser.parse_args()

# 使用命令行参数调用函数
print_threads_count_by_name(args.process_name)
