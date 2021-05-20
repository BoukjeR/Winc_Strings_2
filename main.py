# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

first_goal_scorer = 'Ruud Gullit'
second_goal_scorer = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = first_goal_scorer + ' ' + str(goal_0) + ', ' + second_goal_scorer + ' ' + str(goal_1)

print(scorers)


report = f'{first_goal_scorer} scored in the {goal_0}nd minute\n{second_goal_scorer} scored in the {goal_1}th minute'

print(report)

player = 'Ronald Koeman'

first_name = player[:player.find(" ")]

last_name_len = len(player[player.find(" ")+1:])

name_short = player[0] + '. ' + player[player.find(" ")+1:]

chant = ((first_name + '! ') * len(first_name))[0:-1]

print(chant)

good_chant = chant[-1] != '!'

print(good_chant)