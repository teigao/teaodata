#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Welcome to use teaodata. To get the document related to this package, 
please go to https://github.com/teigao/teaodata
-- multiple_process: process large dataset with multiple processes.
"""

__author__ = 'Teige Gao'

import multiprocessing as mp


# divide large dataset into smaller tasks for multiple processing
def _task_seg(task_workload, dataset):
    _workload = dataset.shape[0]
    _task_amount = _workload // task_workload + 1
    _task_list = (dataset.iloc[task_workload*i:task_workload*(i+1)]
                  for i in range(_task_amount))
    print("The task list has been generated, there are " +
          str(_task_amount) + " tasks")
    return _task_list, _task_amount


def multiple_process(dataset, task_workload, cpu_pool_size, function_name):
    """
    This function will start multiple processes to handle large dataset. 
    -- task_workload: parameter represents the size of each task. 
    -- cpu_pool_size: parameter represents the size of processes started at the same time.
    """
    _task_list, _task_amount = _task_seg(task_workload, dataset)
    _result_queue = []
    _worker_pool = mp.Pool(cpu_pool_size)
    _task_number = 0
    for task in _task_list:
        _task_number = _task_number + 1
        _process = str(_task_number) + "/" + str(_task_amount)
        _result_queue.append(_worker_pool.apply_async(function_name, args=(
            task, _process)))  # this function will add all tasks into task pool
    _worker_pool.close()
    _worker_pool.join()
    return _result_queue


if __name__ == '__main__':
    print('Welcome to use "teaodata" library, please use it with the import command!')
