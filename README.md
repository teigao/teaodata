# TEAODATA Data Tooltip Document
This is a data tooltip designed by Teige Gao. This tool will provides features to process bigdata, ETL. etc

We can download this module from <https://github.com/teigao/teaodata/blob/master/teaodata.7z>, then unzip this file and put the teaodata folder to the Python path. We can refer to the usage_sample.py in the project list to get started.

**This module is developed under Python 3.6.8, before using this module, please put the teaodata folder under %PYTHONPATH%\Lib\site-packages.**
## multiple_process() function

>This function is used for multiple processings, one large dataset will be divided into multiple parts for processing. 

This function requires four parameters: dataset, task_workload, cpu_pool_size, function_name.

- dataset: the dataset requires to be processed, the type of this dataset must be DataFrame.

- task_workload: specify the workload for each task, in the other word, the size of each tasks.

- cpu_pool_size: the CPU cores used at the same time, assume that we have a 4-cores CPU, then it is suggested to set 3 for this parameter.

- function_name: the function to handle the dataset.

**Important: This function must be working under `if __name__ == '__main__':`, and we need to set a process parameter for the working function.**
    
This function will return a queue of result, we will need to use ```get()``` function to get the result. 

The result will be the result returned from the working function. Please refer to the following example:

```python
import teaodata

def work_task(dataset, process): #the working function, process para is required
    """
    do something
    """
    print("task " + process + " is finished!")
    return xx, xxx, xxxx

if __name__ == '__main__': #must work under this
    result_queue = teaodata.multiple_process(
        dataset_need_handle, 100, 3, work_task)
    for result in result_queue:
        xx, xxx, xxxx = result.get()
        print(xx, xxx, xxxx) #need use get() to get the result from queue
```
## sample_dataset module

>This module provides multiple datasets for tesing and learning, the datasets are get from Internet and free to use.

- ```chipotle()``` function

    This function will return a dataset of Chipotle orders. It includes order_id, quantity, item_name, choice_description, item_price columns.

    ```python
    from teaodata import sample_dataset
    dataset = sample_dataset.chipotle()
    print(dataset.head(3))
    ```

    order_id | quantity | item_name | choice_description | item_price
    -|-|-|-|-
    1 | 1 | Chips and Fresh Tomato Salsa | NaN | $2.39
    1 | 1 | Izze | [Clementine] | $3.39
    2 | 2 | Chicken Bowl | [Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]] | $16.98

        
## address_seg module

