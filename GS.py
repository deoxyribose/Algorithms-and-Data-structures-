#!/usr/bin/env python
men = {'Thor': [0,5], 'Loke': [0,5], 'Frej':[0,5],'Odin':[0,5],'Balder':[0,5]}
women = {'Freja':0,'Sif':0,'Idun':0,'Frigg':0,'Gerd':0}
Thor = ['Sif','Freja','Frigg','Gerd','Idun']
Loke = ['Frigg','Sif','Freja','Idun','Gerd']
Frej = ['Sif','Gerd','Idun','Frigg','Freja']
Odin = ['Freja','Frigg','Idun','Sif','Gerd']
Balder = ['Sif','Frigg','Freja','Gerd','Idun']
Freja = ['Balder','Thor','Loke','Odin','Frej']
Sif = ['Frej','Loke','Odin','Thor','Balder']
Idun = ['Loke','Frej','Odin','Balder','Thor']
Frigg = ['Thor','Balder','Odin','Frej','Loke']
Gerd = ['Odin','Loke','Balder','Frej','Thor']
wnames = {'Freja':Freja,'Sif':Sif,'Idun':Idun,'Frigg':Frigg,'Gerd':Gerd}
mnames = {'Thor':Thor,'Loke':Loke,'Frej':Frej,'Odin':Odin,'Balder':Balder}
while 0 in [i[0] for i in men.values() if i[1] > 0]: #As long as there exists a single man who still has someone left to propose to
    for m in men.keys():
        if men[m][1]>0 and men[m][0] == 0: # We choose such a man (who is single, and still has options)
            k = mnames[m][0] # We choose his most prefered woman)
        else:
            continue
        if women[k] == 0: # If the woman is single
            men[m][0] = k # The man chooses the woman
            women[k] = m # The woman chooses the man, and makes him a sandwich
            mnames[m].remove(k) # The man now knows how good her sandwiches are, and crosses her off his list
            men[m][1] = len(mnames[m]) # He writes down how many options he has left
        else: # If the woman isn't single
            if wnames[k].index(m) < wnames[k].index(women[k]): # And if she prefers the man over the poor guy she's with
                men[women[k]][0] = 0 # That poor guy gets dumped
                men[m][0] = k # And the new man chooses the woman
                women[k] = m # And the woman chooses him back, and makes him a sandwich
                mnames[m].remove(k) # And again, the new man knows how good her sandwiches are, and crosses her off his list
                men[m][1] = len(mnames[m]) # Writes down how potential sandwiches are left
            else: # But if she doesn't prefer the new man, he gets rejected
                mnames[m].remove(k) # The man swallows his sadness and says "Whatever, I bet your sandwiches aren't that good anyway...", and crosses her off
                men[m][1] = len(mnames[m]) # And says to himself "Plenty of fish in the sea...", even ifthere are none...
    print zip(men.keys(),[i[0] for i in men.values()])
print '_________________________________________________________________________'       
