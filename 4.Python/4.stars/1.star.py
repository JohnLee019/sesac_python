# print('*')
# print('**')
# print('***')
# print('*')
# print('*')

# def draw_ltriangle(lines):
#     for i in range(1, lines +1):
#         print('*' * i)

# draw_ltriangle(5)

# def draw_rtriangle(lines):
#     for i in range(1, lines +1):
#         print(' ' * (lines -i) + '*'* i)
# draw_rtriangle(5)

# def draw_iltriangle(lines):
#     for i in range(lines, 0,-1):
#         print('*' * i)
# draw_iltriangle(5)

def draw_irtriangle(lines):
    for i in range(lines, 0,-1):
        print(' ' * (lines -i) + '*' * i)
draw_irtriangle(5)