advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice.find('house'))
print(advice[0:39])
advice_list = advice.split('house')
print(advice_list)
print(advice_list[0])