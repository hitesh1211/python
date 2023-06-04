def zigzag(arr):
    n = len(arr)
    # Flag to indicate whether next element should be greater or lesser
    flag = True
    for i in range(n-1):
        if flag:
            # If flag is True, check if current element is greater than next element
            # If yes, swap them
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            # If flag is False, check if current element is lesser than next element
            # If no, swap them
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        # Toggle the flag for next iteration
        flag = not flag
    # Check if the array is in zig-zag form
    for i in range(n-1):
        if i % 2 == 0:
            if arr[i] >= arr[i+1]:
                return 0
        else:
            if arr[i] <= arr[i+1]:
                return 0
    return 1
