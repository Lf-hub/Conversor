print ("Bem vindo ao nosso controle de acesso e IMC.")
nome = str(input("Por favor digite seu nome? "))
peso = float(input("Quanto você esta pesando em quilos? "))
alt = float(input("Qual a sua altura em metro? "))
imc = peso / (alt ** 2)
print (nome,",seu IMC é de: {:.1f}".format(imc))
if imc < 18.5:
    print ("Você está abaixo do peso")
elif 18.6 <= imc < 24.6:
    print ("Você está no peso ideal.PARABÉNS!!")
elif 25 <= imc <29.9:
    print ("Você está levemente acima do peso.")
elif 30.0 <= imc <34.9:
    print ("Você está com obesidade grau I.")
elif 35.0 <= imc <39.9:
    print ("Você esta com obesidade grau II (severa). ")
else:
    imc > 40
    print ("Você está com obesidade grau III, (Mórbida)")



