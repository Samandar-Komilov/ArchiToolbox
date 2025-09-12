# Hashtable techniques training

### 1. Frequency Counting / Uniqueness

This is the most fundamental use of a hashtable: to count the occurrences of items in a collection or to check for uniqueness.

  * **Problem 1: Count Occurrences**

      * **Goal:** Given an array of integers, return a hashmap where keys are the numbers and values are their frequencies.
      * **Template:**
        ```
        freq_map = {}
        for item in array:
            freq_map[item] = freq_map.get(item, 0) + 1
        return freq_map
        ```
      * **Example Problems:**
          * [387] First Unique Character in a String (find the first character with a count of 1)
          * [1207] Unique Number of Occurrences (count frequencies, then check if the frequency counts are unique)

  * **Problem 2: Find Duplicates**

      * **Goal:** Given an array, return `true` if there are any duplicate elements, `false` otherwise.
      * **Template:**
        ```
        seen = set()  // A set is a specialized hash table for unique items
        for item in array:
            if item in seen:
                return True
            seen.add(item)
        return False
        ```
      * **Example Problems:**
          * [217] Contains Duplicate
          * [219] Contains Duplicate II (add a condition on the index)

### 2. Mapping Relationships / Two-Sum Pattern

This pattern uses a hash table to store information about previously seen elements, allowing you to find a pair of elements that satisfy a condition in a single pass.

  * **Problem 3: Basic Two Sum**

      * **Goal:** Given an array and a target, find two numbers that add up to the target.
      * **Template:**
        ```
        seen = {}  // Map: number -> index
        for i, num in enumerate(array):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
        ```
      * **Example Problems:**
          * [1] Two Sum
          * [167] Two Sum II - Input array is sorted (can be solved with two-pointers, but a good hashmap practice)

  * **Problem 4: Word Pattern**

      * **Goal:** Given a pattern string and a sentence string, determine if the sentence follows the same pattern.
      * **Template:**
        ```
        words = sentence.split(' ')
        if len(pattern) != len(words):
            return False

        char_map = {}
        word_map = {}
        for char, word in zip(pattern, words):
            if char in char_map and char_map[char] != word:
                return False
            if word in word_map and word_map[word] != char:
                return False
            if char not in char_map and word not in word_map:
                char_map[char] = word
                word_map[word] = char
        return True
        ```
      * **Example Problems:**
          * [290] Word Pattern

### 3. Grouping Elements

Hash tables are excellent for grouping items that share a common property.

  * **Problem 5: Group Anagrams**
      * **Goal:** Given an array of strings, group the anagrams together.
      * **Template:**
        ```
        groups = {}
        for word in words:
            # The sorted word is the unique "key" for all its anagrams
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            groups[sorted_word].append(word)

        return list(groups.values())
        ```
      * **Example Problems:**
          * [49] Group Anagrams
          * [451] Sort Characters By Frequency (sort based on character counts, which can be stored in a hashmap)

### 4. State/Position Tracking

Use a hash table to store the state or position of elements to help with subsequent lookups.

  * **Problem 6: Check Subarray Sum**

      * **Goal:** Given an array and a target `k`, return `true` if there's a continuous subarray that sums to `k`.
      * **Core Idea:** Use a prefix sum map.
      * **Template:**
        ```
        prefix_sum_map = {0: -1}
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            if (current_sum - k) in prefix_sum_map:
                # Check if the subarray is at least 2 elements long
                if i - prefix_sum_map[current_sum - k] >= 1:
                    return True
            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i
        return False
        ```
      * **Example Problems:**
          * [560] Subarray Sum Equals K
          * [523] Continuous Subarray Sum

  * **Problem 7: Longest Consecutive Sequence**

      * **Goal:** Find the length of the longest consecutive elements sequence.
      * **Core Idea:** Use a `set` for O(1) lookups. Iterate through the set, and for each number, check if it's the start of a sequence (i.e., `num-1` is not in the set).
      * **Template:**
        ```
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length
        ```
      * **Example Problems:**
          * [128] Longest Consecutive Sequence

### 5. Other Foundational Problems

  * **Problem 8: Isomorphic Strings**

      * **Goal:** Given two strings `s` and `t`, determine if they are isomorphic.
      * **Idea:** Similar to the Word Pattern problem, use two hashmaps to track a one-to-one mapping.

  * **Problem 9: Find All Anagrams in a String**

      * **Goal:** Given two strings `s` and `p`, find all the start indices of `p`'s anagrams in `s`.
      * **Idea:** Use a hashmap to store the frequency count of characters in `p`. Then use a sliding window over `s`, maintaining a second hashmap for the characters within the window.

  * **Problem 10: Longest Substring Without Repeating Characters**

      * **Goal:** Find the length of the longest substring without repeating characters.
      * **Idea:** Use a sliding window and a hashmap to store the last seen index of each character.

### Additional Problems for Practice

To reach a total of 20 problems, here are 10 more to solidify your skills:

11. [205] Isomorphic Strings
12. [242] Valid Anagram
13. [438] Find All Anagrams in a String
14. [299] Bulls and Cows
15. [454] 4Sum II (more complex, but a great use of hashmaps)
16. [692] Top K Frequent Words
17. [599] Minimum Index Sum of Two Lists
18. [884] Uncommon Words from Two Sentences
19. [1160] Find Words That Can Be Formed by Characters
20. [1394] Find Lucky Integer in an Array