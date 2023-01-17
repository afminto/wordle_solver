#import numpy as np
#import matplotlib.pyplot as plt
from math import log

guess_arr_only = []
g = open('wordle-allowed-guesses.txt', 'r')
for w in g:
    guess_arr_only.append(w.replace('\n', ''))
ans_arr = []
h = open('wordle-answers-alphabetical.txt', 'r')
for w in h:
    ans_arr.append(w.replace('\n', ''))
print(guess_arr_only)
print(ans_arr)
guess_arr = guess_arr_only + ans_arr

def guess_fn(word, possibilities, guess):
    green = dict()
    yellow = dict()
    grey = []
    for i in range(5):
        if word[i] == guess[i]:
            green[i] = word[i]
        elif guess[i] in word:
            yellow[guess[i]] = i
        else:
            grey.append(guess[i])
    remaining_poss = []
    for poss in possibilities:
        possible = True
        for grn in green:
            if poss[grn] != green[grn]:
                possible = False
        for yell in yellow:
            if yell not in poss:
                possible = False
            elif poss[yellow[yell]] == yell:
                possible = False
        for gry in grey:
            if gry in poss:
                possible = False
        if possible == True:
            remaining_poss.append(poss)
    return remaining_poss, remaining_poss == [guess]


def entr_fn(possibilities, guess):
    total_entropy = 0
    total_poss = len(possibilities)
    for poss in possibilities:
        remaining, ans = guess_fn(poss, possibilities[:], guess)
        if ans:
            total_entropy -= 1
        else:
            ind_entropy = log(len(remaining))
            total_entropy += ind_entropy
    avg_entropy = total_entropy / total_poss
    return avg_entropy


def simulate(word):
    possibilities = ans_arr[:]
    downs = 0
    while(1):
        #print('WHILE run once')
        #print(possibilities)
        downs += 1
        ideal = log(2315)
        best_guess = ''
        if downs == 1:
            print('salet')
            possibilities, succ = guess_fn(word, possibilities[:], 'salet')
            if succ:
                return downs
        else:
            if possibilities == no_match:
                print('cornu')
                possibilities, succ = guess_fn(word, possibilities[:], 'cornu')
                if succ:
                    return downs
                continue

            for guess in guess_arr:
                entr = entr_fn(possibilities[:], guess)
                if entr < ideal:
                    ideal = entr
                    best_guess = guess
                #print(f'guessed {guess} with entropy {entr}')
            print(best_guess)
        
            possibilities, succ = guess_fn(word, possibilities[:], best_guess)
            if succ:
                return downs
no_match = guess_fn('mummy', ans_arr, 'salet')[0]
#print(simulate('spire'))



total_guesses = 0
total_tested = 0
for word in ans_arr:
    total_tested += 1
    print('\n')
    guesses = simulate(word)
    print(guesses)
    total_guesses += guesses
    print(float(total_guesses) / float(total_tested))

exit(0)

#average_guesses = total_guesses / len(ans_arr)
#print(f'Average number of guesses necessary: {average_guesses}')

#remaining = guess('groan', guess_arr, 'hoard')

scoredle = '''tarot   baron   carol   savor   manor   arrow
razor   maror   mayor   taros   major   labor
vapor   favor   caron   valor   rayon   maron
apron   karoo   karos   saros   cargo   arbor
armor   faros   taroc   tarok   parol   arson
carom   carob   actor   gator   tabor   ratoo
nagor   ratos   sapor   payor   taxor   arroz
acros   racon   acron   razoo   agros   oarer
ramon   aeros   ratio   afros   pargo   sargo
pareo   margo   parmo   argon   carbo   parvo
arcos   garbo   sarvo   arvos   largo   narco
argot   yarto   yarco   argol   organ   groan
ariot   aroma   algor   arose   oater   croak
oaker   rapso   okras   raupo   purao   oiran
proas   orcas   groat   aroba   troat   ocrea
troak   proal   orbat   trona   orval   oscar
amour   ottar   groma   orgia   krona   orixa
rioja'''

scoredle = scoredle.replace('\n', '')
scoredle = scoredle.replace(' ', '')
print(scoredle)

scoredle_lst = []
print(type(len(scoredle)))
for i in range(int(len(scoredle) / 5)):
    scoredle_lst.append(scoredle[5*i:5*i+5])

print(scoredle_lst)
print(len(scoredle_lst))

for sc in scoredle_lst:
    if sc not in remaining:
        print(sc)