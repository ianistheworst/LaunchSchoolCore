# def room_size(length, width):
#     int_len = float(length)
#     int_wid = int(width)
#     area_metres = (int_len * int_wid)
#     print(f'the area of the room is {area_metres:.2f} square metres')
#     area_feet = ((int_len * 10.7639) * (int_wid * 10.7639))
#     print(f'The area of the room is {area_feet:.2f} square feet')

def room_area(length, width, output):
    leng = float(length)
    wid = float(width)
    if output == 'M':
        print(f'The area is {(leng * wid):.2f} metres')
    if output == 'F':
        l_feet = leng * 10.7639
        w_feet = wid * 10.7639
        print(f'The area is {(l_feet * w_feet):.2f} feet')


length = input('How long?\n')
width = input('How wide?\n')
ft_metre = input('You want metres or feet? (M or F)\n')


# room_size(length, width)
room_area(length, width, ft_metre)