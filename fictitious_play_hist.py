import matplotlib.pyplot as plt
from random import uniform

game_length = 1000 #�Q�[���̒������w��
program_length = 100 #�v���O�������ǂꂾ���񂷂����w��


def subplots(): #����ݒ�
    fig, ax = plt.subplots()
    ax.set_title('Histgram of belief')
    return (fig, ax)

fig, ax = subplots() 

the_last_belief0 = [] #�Q�[�����w��񐔃v���C������̍Ō�̐M�O�����郊�X�g���쐬    

for j in  range(program_length): #�v���O�������J��Ԃ���
    
    current_belief0 = uniform(0,1) #�ŏ��̐M�O�̎w��(�����ł͈�l���z)
    current_belief1 = uniform(0,1)

    belief0 = [current_belief0] #�M�O�̃��X�g���쐬�A�ŏ��̐M�O���������Ă���
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
        
    the_last_belief0.append(current_belief0) #�Ō�̐M�O�����X�g�ɉ�����
    
ax.hist(the_last_belief0) #�q�X�g�O�������쐬
ax.legend()

plt.show()