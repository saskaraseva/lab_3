from user import User
from friends import Friends
import matplotlib.pyplot as plt
import random

Age = []
Val = []
def gen_random(begin, end, num_count):
    for i in range(num_count):
         Age.append(random.randint(begin, end))
         Val.append(random.randint(begin, end))



def draw_graph(ages):
    graph = {}
    for age in ages:
        graph[age] = graph.get(age, 0) + 1

    graph = sorted(graph.items())
    for age, val in graph:
        Age.append(age)
        Val.append(val)
        print(age, '#' * val)





def main():
    username = input()

    try:
        uid = User(username).execute()
    except User.UserNotFound as e:
        e.msg()
        return


    try:
        ages = Friends(uid).execute()
    except Friends.FriendsNotFound as e:
        e.msg()
        return

    draw_graph(ages)
    #gen_random(1, 50, 50)
    #gen_random(1, 60, 70)
    fig, ax = plt.subplots()
    # add a 'best fit' line

    plt.bar(Age, Val, align='center')
    ax.set_xlabel('Age')
    ax.set_ylabel('value')
    ax.set_title('Histogram of ages of friends')
    plt.show()


    return


if __name__ == '__main__':
    main()