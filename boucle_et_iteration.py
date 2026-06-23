#j'initialise les variable a None
largest = None
smallest = None
#boucle indéfini pour que l'utilisateur puisse mettre autant de nombre qu'il veut
while True:
    num = input('Write integer number: ')
    if num == 'done':
        #break pour mettre fin a la boucle
        break
    try:
        nombre = int(num)
    except ValueError:
        print('Invalid input')
        #continue pour que l'erreur soit ignoré et la boucle remonte pour continuer
        continue
    #structure conditionnel pour comparer les valeurs
    if smallest is None:
        smallest = nombre
    elif nombre < smallest:
        smallest = nombre
    if largest is None:
        largest = nombre
    elif nombre > largest:
        largest = nombre
#resultat
print('Maximum is', largest)
print('Minimum is', smallest)