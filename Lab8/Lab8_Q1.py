def joint_prob(network, assignment):
    joint_prob = 1
    for var in network:
        this = network[var]
        parents = this["Parents"]   #used to get info from the network
        CPT = this["CPT"]           #used to get info from the network
        parent_assignments = []     #used to get info from the network
        if len(parents) > 0:        #creates an assignment to get the true/false from parents of variable
            for parents in parents:
                parent_assignments.append(assignment[parents])
        if assignment[var]: #if true
            joint_prob *= CPT[tuple(parent_assignments)]
        else:               #if false
            joint_prob *= 1 - CPT[tuple(parent_assignments)]
    return joint_prob

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))

print("=" * 10)

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': False})
print("{:.5f}".format(p))

print("=" * 10)

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
parents = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(parents))

print("=" * 10)

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
p = joint_prob(network, {'A': False, 'B':False})
print("{:.5f}".format(p)) 

print("=" *10)

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

p = joint_prob(network, {'John': True, 'Mary': True,
                         'Alarm': True, 'Burglary': False,
                         'Earthquake': False})
print("{:.8f}".format(p))
