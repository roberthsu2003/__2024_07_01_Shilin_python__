import tools

while True:
    tools.play_game()  
    play = input("是否繼續(y/n)")
    if play == "n":
        break       
print("應用程式結束")