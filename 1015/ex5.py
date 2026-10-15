month = int(input("값을 입력하시오(cm): "))

match month:
    case 3|4|5:
        print("봄입니다.")
    case 6|7|8:
        print("여름입니다.")
    case 9|10|11:
        print("가을입니다.")
    case 12|1|2:
        print("겨울입니다.")
    case _:
        print("잘못입력하셨습니다.")