height = 0
growth_per_day = 2
target_height = 10
days = 0
#Loop to track plant growth
while height < target_height:
    height += growth_per_day
    days += 1
#Output to tell us days it took
print("The plant took:",days)