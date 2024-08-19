# CALCULADORA DE NOTAS EN Python!
#   1. Calcula tu promedio.
#   2. Conoce qué notas deberías sacarte para alcanzar tu meta.
#   3. Conoce qué tanto podría variar tu promedio según tu desempeño en el futuro.
# NOTA: se considera el promedio sin aplazos.

MIN_GRADE = 4.00    # Mínima nota para aprobar una materia
MAX_GRADE = 10.0    # Máxima nota posible


def getAverage(grades,offset=0):
    total = len(grades) + offset
    return round((sum(grades)/total),3)

def getMinTryAverage(grades, tries, goal):
    n = len(grades)
    k = tries
    gA = goal
    A = getAverage(grades,k)
    result = ((n+k)*(gA - A)) / k
    if result>0 and result<=10:
        return result
    return None

def getPotencialVariability(grades, tries):
    A = getAverage(grades)
    min = getAverage(grades + [4.00] * tries)
    max = getAverage(grades + [10.0] * tries)
    return [min,A,max] 


def main():

    # Carga tus notas en una lista:
    grades =  [ 8.00, 9.00, 10.0, 10.0, 10.0,
                8.50, 8.50, 8.00, 8.20, 9.00,
                9.88, 8.00, 9.00, 10.0, 8.50,
                8.80, 9.00, 9.00, 9.00, 8.50,
                9.00, 9.20, 10.0, 7.00, 8.50,
                9.00, 8.25, 8.50, 8.50, 10.0 ]
    # 18/08/24 - orden del analítico

    # Cálculo del promedio hasta ahora:
    print("\nAverage:         ",getAverage(grades))

    # Recalcula el promedio en base a notas que aún no hayan sido cargadas
    updated_grades = grades + [8,10,10,10,10]
    print("Updated average: ",getAverage(updated_grades))

    # Ingresa cuál es tu promedio deseado y cuántas materias te quedan por rendir
    goal_avg = 9.00
    tries = 6
    print("\nYou wish to attain a goal of",goal_avg,"in",tries,"tries." if tries>1 else "try.")
    # Cálculo del promedio que deberías sacarte en los intentos para alcanzar tu meta:
    x = getMinTryAverage(updated_grades,tries,goal_avg)
    if x:
        print("You need an average of",round(x,3),"to achieve such goal.")
    else:
        print("Sorry, it appears that your goal is not possible.")

    # Conoce qué tanto podría variar tu promedio según la cantidad de materias que te queden:
    print("\nDo you want to know how much your average could change? Let's find out.")
    y = getPotencialVariability(updated_grades,tries)
    print("In the worst case you would get: ",y[0])     # Worst case: all 4's
    print("In the best case you would get:  ",y[2])     # Best case: all 10's
    print()

main()