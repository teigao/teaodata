#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import os
import jieba.analyse as ja

# 切分出邮编(5位或者6位)，并返回剩余字符串，返回值：(剩余部分，邮编，不符合标识) 元组


def get_single_zip_code(analysis_string):
    zip_code_list = re.findall(r"[0-9]{5,6}", analysis_string)
    if len(zip_code_list) > 1:  # 出现五位数部队名称 sample: 湖北省广水市95816部队 湖北广水 432700
        return "", "", 1
    elif len(zip_code_list) == 1:  # 带有邮编的
        zip_code = zip_code_list[0]
        other_part = analysis_string.replace(zip_code, "")
        return other_part, zip_code, 0
    else:  # 无邮编的
        return analysis_string, None, 0