"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.
"""

def calculate_median(stream: list) -> int:
    length_of_stream: int = len(stream)
    if length_of_stream % 2 == 1:
        midpoint = length_of_stream // 2
        return stream[midpoint]
    else:
        midpoint = length_of_stream // 2
        lower_bound: int = midpoint - 1
        upper_bound: int = midpoint 
        median: float = (stream[lower_bound] + stream[upper_bound]) / 2
        return median

def running_median(stream: list) -> None:
    tmp: list = []

    for element in stream:
        tmp.append(element)
        sorted(tmp)
        print(calculate_median(tmp))

running_median([2, 1, 5, 7, 2, 0, 5])