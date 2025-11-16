import cookiejar

jar = cookiejar.CookieJar(2, 5, 99) # The ints are passed to __init__().
print(jar)
print('CC:', jar.cChip, 'PB:', jar.pbChip, 'BS:', jar.bsChip)
print('Total number of chips:', jar.value())
print('Weight:', jar.weightInGrams(), 'grams')

print()

platter = cookiejar.CookieJar(13, 0, 0) # The ints are passed to __init__().
print(platter)
print('CC:', platter.cChip, 'PB:', platter.pbChip, 'BS:', platter.bsChip)
print('Total number of chips:', platter.value())
print('Weight:', platter.weightInGrams(), 'grams')