total = 0

with open("answer2.txt", encoding="utf-8") as file:

    # Read each line from the file
    for line in file:

        # Skip empty lines
        if not line.strip():
            continue

        # A line can contain multiple ranges separated by commas
        for ranges in line.strip().split(","):

            # Split the range into starting and ending numbers
            start, stop = map(int, ranges.split("-"))

            # Check every possible digit length in this range
            # Example: 824-1475 contains both 3-digit and 4-digit numbers
            for digits in range(len(str(start)), len(str(stop)) + 1):

                # A number can only have two identical halves
                # if it has an even number of digits.
                #
                # Examples:
                # 11      -> 1 | 1
                # 1212    -> 12 | 12
                # 123123  -> 123 | 123
                #
                # 123 cannot work because it has 3 digits.
                if digits % 2 != 0:
                    continue

                # Number of digits in each half
                #
                # 123123 -> half_len = 3
                # 1212   -> half_len = 2
                half_len = digits // 2

                # If the first half is X, the full number is:
                #
                # X X
                #
                # For example:
                # 123123 = 123 * 1000 + 123
                #        = 123 * 1001
                #
                # So multiplier = 10^half_len + 1
                multiplier = 10 ** half_len + 1

                # Smallest possible first half
                #
                # For 6 digits:
                # 100000 -> first half starts at 100
                min_half = 10 ** (half_len - 1)

                # Largest possible first half
                #
                # For 6 digits:
                # 999999 -> first half ends at 999
                max_half = 10 ** half_len - 1

                # Find the first possible repeated number
                # that is inside our requested range.
                #
                # Example:
                # If start = 120000
                # first might become 120
                first = max(
                    min_half,
                    (start + multiplier - 1) // multiplier
                )

                # Find the last possible repeated number
                # that is inside our requested range.
                last = min(
                    max_half,
                    stop // multiplier
                )

                # Make sure there is at least one valid number
                if first <= last:

                    # We need the sum:
                    #
                    # first + (first+1) + ... + last
                    #
                    # Sum of consecutive numbers:
                    #
                    # (first + last) * count / 2
                    count = last - first + 1

                    half_sum = (first + last) * count // 2

                    # Convert the halves back into the
                    # actual repeated numbers.
                    #
                    # Example:
                    # half_sum = 123 + 124 + 125
                    #
                    # multiplier = 1001
                    #
                    # Result:
                    # 123123 + 124124 + 125125
                    total += half_sum * multiplier

print(total)