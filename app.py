import random

omikuzi = ["大吉", "吉", "凶", "中吉"]

index = random.randint(0, 3)
result = omikuzi[index]

print(f"今日の運勢は...{result}")
