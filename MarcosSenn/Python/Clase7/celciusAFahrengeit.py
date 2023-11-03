def celciusAFahrenheit(grados,pasarA):
    if pasarA == "F":
        resultado = (grados * 1.8) + 32
        print(resultado)
    elif pasarA == "C":
        resultado = (grados - 32) / 1.8
        print(resultado)



celciusAFahrenheit(50,"C")
celciusAFahrenheit(10,"F")
