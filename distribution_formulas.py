import math

# Multiple result groups, independent results
# probability of a try is constant
def multinomial(lista_probabilidades, intentos):
    cantidad_intentos = sum(intentos)

    fact_mult = 1
    for intento in intentos:
        fact_mult *= math.factorial(intento)

    right = 1
    for x, p in zip(intentos,lista_probabilidades):
        right *= math.pow(p,x)
    prob_result = math.factorial(cantidad_intentos)/fact_mult * right

    print("El resultado de la distribucion multinomial es: {:.4f}".format(prob_result))


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

    print("El resultado de la distribucion hipergeometrica es: {:.4f}".format(prob_result))



# Use when there is more than one try and there is either
# a chance of success or failure
def geometrica(intentos, probability):
    q = 1 - probability

    prob_result = math.pow(q,(intentos-1))*probability

    print("El resultado de la distribucion geometrica es: {:.4f}".format(prob_result))


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

    print("El resultado de la distribucion de Poisson es: {:.4f}".format(prob_result))


##### PARA USO DE MULTINOMIAL #####
lista_probabilidades = [0.13,0.13,0.14,0.16,0.20,0.24]
lista_intentos = [2,2,2,2,2,2]

multinomial(lista_probabilidades, lista_intentos)

##### PARA USO DE HIPERGEOMETRICA #####
lista_N_y_X = [(5,3),(5,0)]
hipergeometrica(lista_N_y_X)

##### PARA USO DE GEOMETRICA #####
probabilidad = 1/6
repeticiones = 3
geometrica(repeticiones,probabilidad)

##### PARA USO DE POISSON #####
media = 4
num_de_veces_evento = 3
consideraciones = 'at least'
poisson_helper(media, num_de_veces_evento, consideraciones)


# En los casos donde el número de intentos n sea grande y la probabilidad de éxito p sea pequeña,
#  la distribución de Poisson puede ser utilizada para aproximar la distribución binomial. 
# A mayor n y menor p, mejor será la aproximación. Se recomienda que np < 5 (o nq < 5).
#  Si esta condición se cumple, entonces se puede utilizar la distribución de Poisson con 𝜆=𝑛𝑝 para aproximar la distribución binomial. 
