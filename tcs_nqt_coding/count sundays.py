def count_sundays(start_day: str, total_days: int) -> int:
    day_offsets = {
        "mon": 6,
        "tue": 5,
        "wed": 4,
        "thu": 3,
        "fri": 2,
        "sat": 1,
        "sun": 0,
    }

    offset = day_offsets[start_day.lower()]
    sunday_count = 0
    for i in range(1, total_days + 1):
        if (offset + 1) % 7 == 0:
            sunday_count += 1

    return sunday_count

def main():
    start_day = input().strip()
    total_days = int(input().strip())
    print(count_sundays(start_day, total_days))

if __name__ == "__main__" :
    main()