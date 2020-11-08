import math

# Multiple result groups, independent results
# probability of a try is constant
def multinomial(probabilities, results):
    n = sum(results)

    fact_mult = 1
    for result in results:
        fact_mult *= math.factorial(result)

    right = 1
    for x, p in zip(results,probabilities):
        right *= math.pow(p,x)
    prob_result = math.factorial(n)/fact_mult * right

    print(prob_result)


# Use when there are multiple gruops of options
# NO REPLACEMENT strict number of tries
def hipergeometrica(n_x_list):
    N = 0
    n = 0
    for N_k, x in n_x_list:
        N += N_k
        n += x

    numerator = 1

    for N_k, x in n_x_list:
        numerator *= math.comb(N_k,x)

    prob_result = numerator/math.comb(N,n)

    print(prob_result)



# Use when there is more than one try and there is either
# a chance of success or failure
def geometrica(intentos, probability):
    q = 1 - probability

    prob_result = math.pow(q,(intentos-1))*probability

    print(prob_result)


def poisson(mean, repetitions):
    prob_result = math.pow(mean, repetitions) * math.pow(math.e, -mean)/math.factorial(repetitions)

    return prob_result

def poisson_helper(mean, repetitions, amount):
    if(amount == 'exactly'):
        prob_result = math.pow(mean, repetitions) * math.pow(math.e, -mean)/math.factorial(repetitions)
    elif amount == 'at least':
        prob_result = 1
        for i in range(repetitions):
            prob_result -= poisson(mean, i)
    else:
        prob_result = 0
        for i in range(repetitions+1):
            prob_result += poisson(mean, i)

    print(prob_result)


# multinomial([.60,.30,.10], [15,10,5])
# hipergeometrica([(9,4),(7,2),(4,1),(3,1)])
# geometrica(4,1/6)
# poisson_helper(4, 3, 'at least')

# En los casos donde el número de intentos n sea grande y la probabilidad de éxito p sea pequeña,
#  la distribución de Poisson puede ser utilizada para aproximar la distribución binomial. 
# A mayor n y menor p, mejor será la aproximación. Se recomienda que np < 5 (o nq < 5).
#  Si esta condición se cumple, entonces se puede utilizar la distribución de Poisson con 𝜆=𝑛𝑝 para aproximar la distribución binomial. 
