import storage


def Print_global_storage():
    for i, j in storage.Global_storage_get_all().items():
        print(i, "\t=====>\t", j)
