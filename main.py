# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# ----------------------------------------------------------------
#
# Variables for the goals and scorers named using 0 index counting
#
# ----------------------------------------------------------------

scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)

report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"

player = scorer_1

end_of_first_name = player.find(" ")
first_name = player[0:end_of_first_name]
last_name_len = len(player[end_of_first_name + 1:]) # Also counts the tussenvoegsel

name_short = f"{player[0]}. {player[end_of_first_name + 1:]}"

chant = (f"{first_name}! " * len(first_name))[:-1]

good_chant = chant[-1] != " "

