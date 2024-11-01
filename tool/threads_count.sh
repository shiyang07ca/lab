
#!/bin/bash

# 检查是否提供了进程名称
if [ -z "$1" ]; then
    echo "用法: $0 <进程名称>"
    exit 1
fi

PROCESS_NAME="$1"

# 查找进程名称对应的进程ID
PIDS=$(ps -ef | grep "$PROCESS_NAME" | grep -v "threads_count.sh" | grep -v "grep" | awk '{print $2}')

# 检查是否找到了进程
if [ -z "$PIDS" ]; then
    echo "未找到进程: $PROCESS_NAME"
    exit 1
fi

# 遍历每个进程ID，计算线程数
for PID in $PIDS; do
    THREAD_COUNT=$(ps -M "$PID" | wc -l)
    echo "进程ID: $PID, 进程命令: $(ps -p $PID -o command=), 线程数: $THREAD_COUNT"
done
