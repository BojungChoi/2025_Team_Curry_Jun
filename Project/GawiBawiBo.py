import random

def GawiBawiBo():

    while True:
        number = random.randint(0,2)

        if number == 0:
            computer = "가위"
        elif number == 1:
            computer = "바위"
        else:
            computer = "보"

        MyChoice = input("가위, 바위, 보 중에 하나를 골라 적으세요 ==>  ")

        if MyChoice not in ["가위", "바위", "보"]:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue

        if MyChoice == computer:
            game = "무승부"
        elif MyChoice == "가위":
            if computer == "보":
                game = "승리"
            else:
                game = "패배"
        elif MyChoice == "바위":
            if computer == "가위":
                game = "승리"
            else:
                game = "패배"
        elif MyChoice == "보":
            if computer == "바위":
                game = "승리"
            else:
                game = "패배"

        print(f"컴퓨터의 선택은 {computer}, 따라서 당신의 {game}입니다.\n")
        
        if game == "승리":
            print("축하합니다! 승리하셨습니다.\n")
            break

