import matplotlib.pyplot as plt
from random import uniform

ts_length = 2000 #ゲームの長さを指定

current_belief0 = uniform(0,1) #最初の信念の指定(ここでは一様分布)
current_belief1 = uniform(0,1)

def subplots(): #軸を設定
    fig, ax = plt.subplots()   
    return (fig, ax)

fig, ax = subplots() 

belief0 = [current_belief0] #信念のリスト
belief1 = [current_belief1]

for i in range(ts_length):
    
    if current_belief0 > 0.5: #プレイヤー0の行動を指定
        player0_play = 1
    else:
        player0_play = 0
        
    if current_belief1 > 0.5: #プレイヤー1の行動を指定
        player1_play = 0
    else:
        player1_play = 1
    
    current_belief0 = (current_belief0) + ((player1_play - current_belief0)/(i + 1)) #プレイヤーの信念の変更
    current_belief1 = (current_belief1) + ((player0_play - current_belief1)/(i + 1)) 
    
    belief0.append(current_belief0) #信念のリストに追加
    belief1.append(current_belief1)
   
ax.plot(belief0)
ax.plot(belief1)

plt.show()
