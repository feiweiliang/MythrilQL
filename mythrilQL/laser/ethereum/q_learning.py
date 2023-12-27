import numpy as np
import pandas as pd

ACTIONS = ['true', 'false']  # 两种动作
EPSILON = 0.9  # 90%选择最优的动作，10%选择随机的动作
ALPHA = 0.1  # 学习率
GAMMA = 0.9  # 衰减率


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # Q表的行和列 也就是1行2列
        columns=actions,  # 列名字 也就是true false
        index=[0]
    )
    # print(table)    # 显示表格
    return table


def choose_action(state, q_table):
    # This is how to choose an action
    if state not in q_table.index.tolist():
        df1 = pd.DataFrame([[0,0]],columns=ACTIONS,index=[state])
        q_table = q_table.append(df1)
    state_actions = q_table.loc[state, :]  # 将此时状态的Q表 行值赋给state_actions
    if (np.random.uniform() > EPSILON) or ((state_actions == 0).all()):  # 如果大于0.9这个概率或者全部Q值都为0的时候我们进行随机选择动作
        action_name = np.random.choice(ACTIONS)  # 随机选择动作
    else:  # 如果不是随机选择的话
        action_name = state_actions.idxmax()  # 就选Q值最大的那个动作
    return action_name,q_table


def get_feedback(S, A):
    # 若该状态下探索到敏感指令，R = 敏感指令个数
    # 若该状态下未探索到敏感指令， R = 0
    if A == 'true':
        S_ = 0
    S_, R = 0, 0
    return S_, R  # 返回此时的状态 和 奖励值

def get_max_score_state(candidatel_list):
    max_score = -1
    max_index = -1
    for i in range(len(candidatel_list)):
        if candidatel_list[i].score > max_score:
            max_score = candidatel_list[i].score
            max_index = i
    global_state = candidatel_list.pop(i)
    print('score',global_state.score)
    return  candidatel_list,global_state

if __name__ == "__main__":
    q = build_q_table(1, ['true', 'false'])
    q = q.append(pd.DataFrame([[11,2]],columns=ACTIONS,index=[20]))
    # print(q)
    state_actions = q.loc[20, :].idxmax()
    # print(state_actions)
    t1,t2=choose_action(7, q)
    # print(t2)
