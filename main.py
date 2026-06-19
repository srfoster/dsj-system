
# TODO: Pull in all functions and wrap in a REPL

import anna as anna
import ashlan as ashlan
import charlie as charlie
import cody as cody
import david as david
import frankie as frankie
import ian as ian
import isaac as isaac
import jyden as jyden
import randy as randy
import raphael as raphael
import seth as seth
import tj as tj
import ulysses as ulysses
import cody_raphael_tj as cody_raphael_tj
import cody_raphael_tj_two as cody_raphael_tj_two
import randy_anna_ulysses_jyden_part_1
import randy_anna_ulysses_jyden_part_2


names = [
    anna,
    ashlan,
    charlie,
    cody,
    david,
    frankie,
    ian,
    isaac,
    jyden,
    randy,
    raphael,
    seth,
    tj,
    ulysses,
    cody_raphael_tj,
    cody_raphael_tj_two,
    randy_anna_ulysses_jyden_part_1,
    randy_anna_ulysses_jyden_part_2,
]

while True:
  for i in range(len(names)):
    print(str(i + 1) + ". " + str(names[i]))

  pick = int(input("Pick one:")) - 1

  names[pick].dsj_topic()


'''
anna.dsj_topic()
ashlan.dsj_topic()
charlie.dsj_topic()
cody.dsj_topic()
david.dsj_topic()
#frankie.dsj_topic()
ian.dsj_topic()
isaac.dsj_topic()
jyden.dsj_topic()
randy.dsj_topic()
raphael.dsj_topic()
seth.dsj_topic()
tj.dsj_topic()
ulysses.dsj_topic()
'''
