"""
Find the Longest Substring Without Repeating Characters
Given a string, find the longest substring without repeating characters.
Input: "abcabcbb" → Output: "abc"
Input: "abcba" → Output: "abc"
Input: "bbbbb" → Output: "b"
Input: "pwwkew" → Output: "wke"
Input: "abcdeabcabcdefgabc" → Output: "abcdefg"
"""

def longest_substring_without_repeating_chars(input_string):
    output_substring = ""
    current_substring = ""
    for char in input_string:
        if char in current_substring:
            if len(current_substring) > len(output_substring):
                output_substring = current_substring
            current_substring = current_substring[current_substring.index(char)+1::] + char
        else:
            current_substring += char
    if len(current_substring) > len(output_substring):
        output_substring = current_substring
    print(output_substring)

longest_substring_without_repeating_chars("abcabcbb")
longest_substring_without_repeating_chars("abcba")
longest_substring_without_repeating_chars("bbbbb")
longest_substring_without_repeating_chars("pwwkew")
longest_substring_without_repeating_chars("abcdeabcabcdefgabc")

