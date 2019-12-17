#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is used for getting sample dataset. 
-- chipotle: This function will return a dataset of Chipotle orders. 
"""

__author__ = 'Teige Gao'

import pandas as pd
import os


_current_path = os.path.dirname(__file__)
_root_folder = _current_path+"\\_sample_datasets\\"


def chipotle():
    """
    This function will return a dataset of Chipotle orders.
    -- It includes order_id, quantity, item_name, choice_description, item_price columns.
    """
    csv_file = pd.read_csv(open(
        _root_folder + "chipotle.tsv", 'r', encoding='UTF-8'), sep='\t', low_memory=False)
    return csv_file


if __name__ == '__main__':
    print('Welcome to use "teaodata" library, please use it with the import command!')
