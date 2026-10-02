total = 0

with open("answer2.txt", encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            continue

        for ranges in line.strip().split(","):
            start, stop = map(int, ranges.split("-"))

            for digits in range(len(str(start)), len(str(stop)) + 1):

                if digits % 2 != 0:
                    continue

                half_len = digits // 2
                multiplier = 10 ** half_len + 1

                # Smallest and largest possible repeated-half number
                min_half = 10 ** (half_len - 1)
                max_half = 10 ** half_len - 1

                first = max(min_half, (start + multiplier - 1) // multiplier)
                last = min(max_half, stop // multiplier)

                if first <= last:
                    total += multiplier * (first + last) * (last - first + 1) // 2
print(total)