import matplotlib.pyplot as plt
from random import uniform

game_length = 2000 #�Q�[���̒������w��

current_belief0 = uniform(0,1) #�ŏ��̐M�O�̎w��(�����ł͈�l���z)
current_belief1 = uniform(0,1)

def subplots(): #���A�ڐ����ݒ�
    fig, ax = plt.subplots()
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_title('Fititious play')
    return (fig, ax)

fig, ax = subplots() 

belief0 = [current_belief0] #�M�O�̃��X�g���쐬�A�ŏ��̐M�O��������Ă���
belief1 = [current_belief1]

for i in range(game_length):
    
    if current_belief0 > 0.5: #�v���C���[0�̍s�����w��
        player0_play = 1
    else:
        player0_play = 0
        
    if current_belief1 > 0.5: #�v���C���[1�̍s�����w��
        player1_play = 0
    else:
        player1_play = 1
    
    current_belief0 = (current_belief0) + ((player1_play - current_belief0)/(i + 2)) #�v���C���[�̐M�O�̕ύX
    current_belief1 = (current_belief1) + ((player0_play - current_belief1)/(i + 2)) 
    
    belief0.append(current_belief0) #�ύX���ꂽ�M�O�����X�g�ɒǉ�
    belief1.append(current_belief1)
   
ax.plot(belief0, label = 'x0(t)') #�M�O�̃��X�g���v���b�g����
ax.plot(belief1, label = 'x1(t)')
ax.legend()

plt.show()