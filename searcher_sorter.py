# --BINARY SEARCH
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2 #finds the middle element
        if sorted_list[mid] == target: #if the middle element ends up being the target...we good
            return mid
        elif sorted_list[mid] < target: #if the middle element is less than the target, we get rid of the left half
            left = mid + 1
        else: # if it was greater then get rid of the right side
            right = mid - 1
    return None # if the target isnt in the list

# --BUBBLE SORT
def sort_videos(video_titles):
    length = len(video_titles)
    for i in range(length):
        for j in range(0, length - i - 1):
            if video_titles[j] > video_titles[j + 1]: # compares the values and swaps them
                video_titles[j], video_titles[j + 1] = video_titles[j + 1], video_titles[j] 
        
    return video_titles

