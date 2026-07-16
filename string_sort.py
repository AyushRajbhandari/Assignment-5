# Author: Ayush Rajbhandari
# GitHub username: AyushRajbhandari
# Date: 6-13-26
# Description: Defines a string_sort function that uses insertion sort to sort
# #              a list of strings in-place while ignoring case.

def string_sort(string_list):
    """
    Sorts a list of strings in-place using insertion sort.
    The sorting ignores case sensitivity.
    """
    for index in range(1, len(string_list)):
        current_string = string_list[index]
        pos = index - 1

        # Compare the lowercase versions of the strings to ignore case
        while pos >= 0 and string_list[pos].lower() > current_string.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1

        # Insert the current string in its correct sorted position
        string_list[pos + 1] = current_string


