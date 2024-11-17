import random
coin = ''
def rand_coin_tg():
    rand_coin = random.randint(1,2)
    if rand_coin == 1:
        coin = 'Орел'
    elif rand_coin == 2:
        coin = 'Решка'
        return coin


print(rand_coin_tg)
        
 

