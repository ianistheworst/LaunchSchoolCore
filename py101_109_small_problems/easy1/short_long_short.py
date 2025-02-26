def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return (string2 + string1 + string2)
    elif len(string1) < len(string2):
        return (string1 + string2 + string1)
    else:
        return "These strings are equal length"

 # These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

print(short_long_short('ahoy', 'sailors'))
print(short_long_short('ahoy', 'boys'))
print(short_long_short('sailors', 'ahoy'))