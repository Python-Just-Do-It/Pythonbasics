def return_pair(arr, target):
    l = len(arr)
    ans = []
    outer_break = False
    for i in range(l):
        for j in range(i+1, l):
            if arr[i] + arr[j] == target:
                ans.extend([arr[i],arr[j]])
                outer_break = True
                break
            if outer_break :
                break
            return ans
               