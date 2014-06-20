import matplotlib.pyplot as plt
from random import uniform

game_length = 1000 #ゲームの長さを指定
program_length = 100 #プログラムをどれだけ回すかを指定


def subplots(): #軸を設定
    fig, ax = plt.subplots()
    ax.set_title('Histgram of belief')
    return (fig, ax)

fig, ax = subplots() 

the_last_belief0 = [] #ゲームを指定回数プレイした後の最後の信念を入れるリストを作成    

for j in  range(program_length): #プログラムを繰り返し回す
    
    current_belief0 = uniform(0,1) #最初の信念の指定(ここでは一様分布)
    current_belief1 = uniform(0,1)

    belief0 = [current_belief0] #信念のリストを作成、最初の信念だけを入れておく
    belief1 = [current_belief1]
   
    for i in range(game_length):
    
        if current_belief0 > 0.5: #プレイヤー0の行動を指定
            player0_play = 1
        else:
            player0_play = 0
        
        if current_belief1 > 0.5: #プレイヤー1の行動を指定
            player1_play = 0
        else:
            player1_play = 1
    
        current_belief0 = (current_belief0) + ((player1_play - current_belief0)/(i + 2)) #プレイヤーの信念の変更
        current_belief1 = (current_belief1) + ((player0_play - current_belief1)/(i + 2)) 
        
    the_last_belief0.append(current_belief0) #最後の信念をリストに加える
    
ax.hist(the_last_belief0) #ヒストグラムを作成
ax.legend()

plt.show()