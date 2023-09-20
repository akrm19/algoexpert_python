# given two non-empty arrays, write a function that determines if the second
# array is a subsequence of the first one

def isValidSubsequence(array, sequence):
    cur_array_idx = 0
    cur_seq_idx = 0

    while cur_array_idx < len(array) and cur_seq_idx < len(sequence):
        if array[cur_array_idx] == sequence[cur_seq_idx]:
            cur_seq_idx += 1
        cur_array_idx += 1

    return cur_seq_idx == len(sequence) 
