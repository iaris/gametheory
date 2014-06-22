import matplotlib.pyplot as plt
from random import uniform

game_length = 50 #ゲームの長さを指定

current_belief0 = uniform(0,1) #最初の信念の指定(ここでは一様分布)
current_belief1 = uniform(0,1)

def subplots(): #軸、目盛りを設定
    fig, ax = plt.subplots()
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_title('Coordination game')
    return (fig, ax)

fig, ax = subplots() 

belief0 = [current_belief0] #信念のリストを作成、最初の信念だけ入れておく
belief1 = [current_belief1]

for i in range(game_length):
    
    if current_belief0 > 0.333333333333333333333333333333333333333333333333: #プレイヤー0の行動を指定
        player0_play = 1
    else:
        player0_play = 0
        
    if current_belief1 > 0.333333333333333333333333333333333333333333333333: #プレイヤー1の行動を指定
        player1_play = 1
    else:
        player1_play = 0
    
    current_belief0 = (current_belief0) + ((player1_play - current_belief0)/(i + 2)) #プレイヤーの信念の変更
    current_belief1 = (current_belief1) + ((player0_play - current_belief1)/(i + 2)) 
    
    belief0.append(current_belief0) #変更された信念をリストに追加
    belief1.append(current_belief1)
   
ax.plot(belief0, label = 'x0(t)') #信念のリストをプロットする
ax.plot(belief1, label = 'x1(t)')
ax.legend()

plt.show()