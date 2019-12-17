from teaodata import sample_dataset
import teaodata


def work_task(dataset, process):
    print("task " + process + " is finished!")
    return dataset


if __name__ == '__main__':
    result_queue = teaodata.multiple_process(
        sample_dataset.chipotle(), 100, 3, work_task)
    for result in result_queue:
        print(result.get())
