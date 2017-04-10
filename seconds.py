"""
Programa: Conversor de Segundos em Dias, Horas, Minutos e Segundos
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 08 de fevereiro de 2017
"""

# Entra com o valor em segundos
ValorSegundos = int(input("Por favor, entre com o número de segundos que "
                          "deseja converter: "))

# Converte os segundos em horas
TotalHoras = ValorSegundos // 3600
TotalDias = TotalHoras // 24
TotalHorasFinal = TotalHoras % 24
SegundosRestantes = ValorSegundos % 3600
TotalMinutos = SegundosRestantes // 60
SegundosFinais = SegundosRestantes % 60

# Caso o Total de horas for menor que 24, menos de um dia
if TotalHoras < 24:
    print(TotalHoras, "horas,", TotalMinutos, "minutos e", SegundosFinais,
          "segundos.")

# Caso o Total de horas for igual a 24
elif TotalHoras == 24 or TotalHoras < 48:
    print(TotalDias, "dia,", TotalHorasFinal, "horas,", TotalMinutos,
          "minutos e", SegundosFinais, "segundos.")

# Caso o total de horas for maior que 24, mais de um dia
else:
    print(TotalDias, "dias,", TotalHorasFinal, "horas,", TotalMinutos,
          "minutos e", SegundosFinais, "segundos.")
