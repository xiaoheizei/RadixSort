def radixSort(arr):
    n = len(str(max(arr)))  # 记录最大值的位数
    for k in range(n):#n轮排序
        # 每一轮生成10个列表
        bucket_list=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
        for i in arr:
            # 按第k位放入到桶中
            bucket_list[i//(10**k)%10].append(i)
        # 按当前桶的顺序重排列表
        arr=[j for i in bucket_list for j in i]
    return arr
# example
array = [1, 3, 4, 8, 5]
sort = radixSort(array)
