count = 0
value = 50

with open("answer.txt", "r", encoding="utf-8") as file:

    for raw_line in file:

        line = raw_line.strip()

        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == "R":

            count += (value + distance) // 100
            value = (value + distance) % 100

        elif direction == "L":

            if value == 0:
                count += distance // 100
            else:
                count += (distance + (100 - value)) // 100

            value = (value - distance) % 100

print(f"Final value: {value}")
print(f"Zero wrap count: {count}")