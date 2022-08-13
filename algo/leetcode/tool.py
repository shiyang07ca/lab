#!/usr/bin/env python

import sys
import logging
import shutil
from pathlib import Path


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


BASE_DIR = Path.cwd()
TEMPLATES = Path.cwd().joinpath("templates")


def create_algo(pnum):
    pnum = f"{pnum:05d}"

    dirc = BASE_DIR / "algo" / pnum
    readme_f = BASE_DIR / "algo" / pnum / "README.md"
    sl_f = BASE_DIR / "algo" / pnum / "sl.py"
    tmpl_f = TEMPLATES / "tmpl.py"

    try:
        logger.info(f"创建文件夹: {dirc.as_posix()}")
        dirc.mkdir()
        logger.info(f"创建文件: {readme_f.as_posix()}")
        readme_f.touch()
        logger.info(f"创建文件: {sl_f.as_posix()}")
        sl_f.touch()
        shutil.copyfile(tmpl_f, BASE_DIR / "algo" / pnum / "sl.py")
    except Exception as e:
        logger.error(f"创建失败: {e}")
    else:
        logger.info("================ Done ================")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Leetcode 助手")
    parser.add_argument("-p", "--p", type=int, help="创建题号")

    args = parser.parse_args()
    if args.p:
        create_algo(args.p)


if __name__ == "__main__":
    main()
