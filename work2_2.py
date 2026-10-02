total = 0

with open("answer2.txt", encoding="utf-8") as file:

    for line in file:

        if not line.strip():
            continue

        for ranges in line.strip().split(","):

            start, stop = map(int, ranges.split("-"))

            # Keep track of invalid IDs found in this range.
            #
            # A number such as 1111 can be created in more than
            # one way:
            #
            # 1 × 4
            # 11 × 2
            #
            # We only want to add it once.
            invalid_ids = set()

            # We only need to consider numbers with the same
            # number of digits as numbers inside our range.
            for digits in range(len(str(start)), len(str(stop)) + 1):

                # An invalid ID needs at least two repetitions,
                # so the smallest possible pattern is half the
                # total number of digits.
                #
                # Example:
                # 123123 -> pattern length can be 3
                # 121212 -> pattern length can be 2
                for pattern_length in range(1, digits // 2 + 1):

                    # The pattern must divide the total number
                    # of digits exactly.
                    #
                    # Example:
                    #
                    # 123123123 has 9 digits.
                    #
                    # Pattern length 3 works:
                    # 123 | 123 | 123
                    #
                    # Pattern length 4 doesn't:
                    # 1231 | 2312...
                    if digits % pattern_length != 0:
                        continue

                    repetitions = digits // pattern_length

                    # We need at least two copies of the pattern.
                    if repetitions < 2:
                        continue

                    # Example:
                    #
                    # pattern_length = 3
                    # repetitions = 2
                    #
                    # 123123 = 123 × 1001
                    #
                    # For 123123123:
                    #
                    # 123 × 1001001
                    multiplier = sum(
                        10 ** (pattern_length * i)
                        for i in range(repetitions)
                    )

                    # The pattern itself must contain exactly
                    # pattern_length digits.
                    #
                    # Example for a 3-digit pattern:
                    # 100 -> 999
                    min_pattern = 10 ** (pattern_length - 1)
                    max_pattern = 10 ** pattern_length - 1

                    # Find the smallest pattern whose repeated
                    # number is >= start.
                    #
                    # We use ceiling division:
                    #
                    # ceil(start / multiplier)
                    first = max(
                        min_pattern,
                        (start + multiplier - 1) // multiplier
                    )

                    # Find the largest pattern whose repeated
                    # number is <= stop.
                    last = min(
                        max_pattern,
                        stop // multiplier
                    )

                    # No patterns from this combination fall
                    # inside the current range.
                    if first > last:
                        continue

                    # Generate only the invalid IDs that actually
                    # fall inside the range.
                    for pattern in range(first, last + 1):

                        number = pattern * multiplier

                        invalid_ids.add(number)

            # Add each invalid ID only once.
            total += sum(invalid_ids)


print(total)