# -*- coding: utf-8 -*-
'''
This script is to simulate Pokemon breeding with Destiny Knot.
With Destiny Knot, 5 IVs from the parents will be passed down,
and the rest will be random.
'''
import random
import time

# warper  class for Pokemon
class Pokemon:
    # HP, Atk, Def, Sp. Atk, Sp. Def, Spd
    iv=[0,0,0,0,0,0]
    def __init__(self, iv):
        self.iv = iv

random.seed()

# init parents IVs
father=Pokemon([31,31,2,31,31,31])
mother=Pokemon([22,31,31,31,31,31])

# the desired IVs spread for the child
prefer_mask=[1,1,1,0,1,1]

hit_count=0
num_repeat=500
mode=1
# run the simulation and write the result in file
with open("breeding-"+time.strftime("%Y-%m-%d-%H-%M-%S")+".txt","w+") as f:
    for n in range(0,num_repeat):
        new_ivs=[-1 for i in range(0,6)]
        # pick 5 random index of parents IVs with replacement
        # e.g. the same stats from one parent can overwrite the one
        # picked from the other parent earlier
        if mode==0:
            picks=random.sample(list(range(0,12)),5)
            # gather parents IVs
            ivs=father.iv
            ivs.extend(mother.iv)
            # elements in picks are the indexes of elements to pick from ivs
            for i in range(0,len(picks)):
                new_ivs[picks[i]%6]=ivs[picks[i]]

        # without replacement
        elif mode==1:
            picks=random.sample(list(range(0,6)),5)

            # for the selected stas, get the iv from one of the parents
            for i in range(0,len(picks)):
                p_mask=random.randint(0,1)
                if p_mask==1:
                    new_ivs[picks[i]]=father.iv[picks[i]]
                elif p_mask==0:
                    new_ivs[picks[i]]=mother.iv[picks[i]]

        # get random ivs for stats that are not passed down from parent
        for j in range(0,len(new_ivs)):
            if new_ivs[j]==-1:
                new_ivs[j]=random.randint(0,31)

        # write the ivs to file
        f.write("#"+str(n)+": "+str(new_ivs))

        # check if the child IVs spread is the desired IVs spread
        hit=0
        for k in range(0,len(new_ivs)):
            if prefer_mask[k]==1 and new_ivs[k]==31:
                hit+=1
        if hit==5:
            hit_count+=1
            f.write(" **********")
        f.write("\n")
    f.write("*****Hit Count: "+str(hit_count)+"*****")
print("*****Hits: "+str(hit_count))
