import random

def play_game():
    min = 1
    max = 100
    target = random.randint(min, max)
    print(target)
    print("===========猜數字遊戲============\n")
    count = 0

    while True:
        
        try:
            keyin = int(input(f"猜數字範圍{min}~{max}:"))
            count += 1
        except:
            print("格式錯誤")     # 輸入錯誤不算次數
            continue

        if keyin < min or keyin > max:
            print("超過範圍")        
            continue

        

        if keyin == target:
            print(f"賓果!猜對了, 答案是:{keyin}")
            print(f"您猜了{count}次")
            break
        elif keyin > target:
            print("再小一點")
            max = keyin - 1
            
        elif keyin < target:
            print("再大一點")
            min = keyin + 1
        print(f"您已經猜了{count}次")

while True:
    play_game()  
    play = input("是否繼續(y/n)")
    if play == "n":
        break       
print("應用程式結束")