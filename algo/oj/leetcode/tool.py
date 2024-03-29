#!/usr/bin/env python3

import sys
import logging
import shutil
import subprocess

from pathlib import Path


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


BASE_DIR = Path.cwd()
TEMPLATES = Path.cwd().joinpath("templates")


def create_algo_tmpl(title):
    pass


def create_ci_algo_tmpl(num):
    pnum = f"{num:04d}"

    dirc = BASE_DIR / "coding-interviews" / pnum
    readme_f = BASE_DIR / "coding-interviews" / pnum / "README.md"
    sl_f = BASE_DIR / "coding-interviews" / pnum / "sl.py"
    tmpl_f = TEMPLATES / "tmpl.py"

    try:
        logger.info(f"创建文件夹: {dirc.as_posix()}")
        dirc.mkdir()
        logger.info(f"创建文件: {readme_f.as_posix()}")
        readme_f.touch()
        logger.info(f"创建文件: {sl_f.as_posix()}")
        sl_f.touch()
        shutil.copyfile(tmpl_f, sl_f)

        # Download problem detail
        # https://github.com/clearloop/leetcode-cli
        # p = subprocess.Popen(f"leetcode pick {num}", stdout=subprocess.PIPE, shell=True)
        # desc = p.communicate()[0].decode()
        # desc = desc.strip().replace(" is on the run...", "")
        # print(desc)

        with sl_f.open("r+") as f:
            content = f.read()
            f.seek(0)
            f.write(
                f"""\"""


\"""
\n"""
                + content
            )
    except Exception as e:
        logger.error(f"创建失败: {e}")
    else:
        logger.info("================ Done ================")


def create_lc_algo_tmpl(num):
    pnum = f"{num:05d}"

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
        shutil.copyfile(tmpl_f, sl_f)

        # Download problem detail
        # https://github.com/clearloop/leetcode-cli
        p = subprocess.Popen(f"leetcode pick {num}", stdout=subprocess.PIPE, shell=True)
        desc = p.communicate()[0].decode()
        desc = desc.strip().replace(" is on the run...", "")
        # print(desc)
        with sl_f.open("r+") as f:
            content = f.read()
            f.seek(0)
            f.write(
                f"""\"""

{desc}

\"""
\n"""
                + content
            )
    except Exception as e:
        logger.error(f"创建失败: {e}")
    else:
        logger.info("================ Done ================")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Leetcode 助手")
    parser.add_argument("-p", "--p", type=int, help="创建 leetcode 题号")
    parser.add_argument("-c", "--c", type=int, help="创建 coding interviews 题号")

    parser.add_argument("-a", "--a", type=int, help="创建解题模版")
    args = parser.parse_args()
    if args.p:
        create_lc_algo_tmpl(args.p)

    if args.c:
        create_ci_algo_tmpl(args.c)

    if args.a:
        create_algo_tmpl(args.a)


if __name__ == "__main__":
    main()
