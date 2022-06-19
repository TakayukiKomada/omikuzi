import random

omikuzi = ["大吉", "吉", "凶", "中吉", "末吉"]

index = random.randint(0, len(omikuzi) - 1)
result = omikuzi[index]

print(f"今日の運勢は...{result}")
