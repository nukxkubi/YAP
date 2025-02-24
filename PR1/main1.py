def convert_seconds(x):
    hours = x // 3600
    remaining_seconds_after_hours = x % 3600
    minutes = remaining_seconds_after_hours // 60
    seconds = remaining_seconds_after_hours % 60

    return hours, minutes, seconds

x = int(input("Введите количество секунд: "))
hours, minutes, seconds = convert_seconds(x)
print(f"{x} секунд = {hours} часов, {minutes} минут, {seconds} секунд")