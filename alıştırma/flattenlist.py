def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(my_list))
