peso = float((input('Escribe tu peso en KG')))
estatura =float(input('Escribe tu estatura en metros'))
imc = peso / estatura ** 2
imcround = round(imc,2)
print('Tu indice de masa corporal es')
print(imcround)