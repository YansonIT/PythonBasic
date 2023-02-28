height = int(input("Введіть висоту фігури :"))


def triangle_empty(height: int):
    for i in range(height-1):
        outer_symbol = " " * (height - i - 1)
        if i == 0:
            border_symbol = "*"
        else: border_symbol = "*" + " " * (2 * i - 1) + "*"
        print(outer_symbol + border_symbol)
    print("*" * (int(height) * 2-1))
    print("\n")




def triangle_simple (height: int):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    print("\n")




def triangle_multi_func (height: int, fill_symbol: ".", outer_symbol: ".", border_symbol: "*") -> None:
    for i in range(height -1):
         print(
            outer_symbol * (height - i -1),
            border_symbol,
            fill_symbol * ((i - 1) if i > 0 else 0),
            border_symbol if i > 0 else " ",
            fill_symbol * ((i - 1) if i > 0 else 0),
            border_symbol if i > 0 else " ",
            outer_symbol * (height - i - 1),
            sep=""
         )
    print(border_symbol * ((height * 2) -1))
    print("\n")




def rhombus_1 (height: int, fill_symbol: ".", outer_symbol: ".", border_symbol: "*") -> None:
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    # print(border_symbol * ((height * 2) - 1))
    for i in range(height -1):
         print(
            outer_symbol * (i + 1),                   #dots befor
            border_symbol,                                    #   '*'  left border
            fill_symbol * (height - i-3),          #  "0" in left part
            border_symbol if i < height - 2 else " ",                  #  '*' in midle
            fill_symbol * (height - i-3),          #  '0' in rigt part
            border_symbol if i < height-2 else " ",                  # right border
            outer_symbol * (i + 1),                  # '.'  after triangle
            sep=""
         )

    print("\n")




def rhombus_2 (height: int, fill_symbol: ".", outer_symbol: ".", border_symbol: "*", middle: " "):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    for i in range(height -1):
         print(
            outer_symbol * (i + 1),
            border_symbol,
            fill_symbol * (height - i-3),
            middle if i < height - 2 else " ",
            fill_symbol * (height - i-3),
            border_symbol if i < height-2 else " ",
            outer_symbol * (i + 1),
            sep=""
         )

    print("\n")



triangle_empty(height=height)
triangle_simple(height=height)
triangle_multi_func(height=height, fill_symbol=" ", outer_symbol=" ", border_symbol="*")
rhombus_2(height=height, fill_symbol=" ", outer_symbol=" ", border_symbol="*", middle=" ")
rhombus_1(height=height, fill_symbol=" ", outer_symbol=" ", border_symbol="*")
