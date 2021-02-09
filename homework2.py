buildCount = 3
ninjaCount = 25
tunelCount = 2
banditCount = 40

print("calculating ....")
ninjaTotal = ninjaCount * buildCount
print(f"Total ninjas: {ninjaTotal}")

banditTotal = banditCount * tunelCount
print(f"Total bandits: {banditTotal}")

total = ninjaTotal + banditTotal
print(f"total: {total}")
