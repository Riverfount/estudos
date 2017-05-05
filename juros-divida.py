#!/usr/bin/python
# -*- coding: UTF-8 -*-

valor_emprestado = float(input("Entre com o valor total da dívida: "))
juros = float(input("Entre com o juros mensal da dívida: "))
parcela = float(input("Entre com o valor da parcela: "))

acumulador = valor_emprestado
meses = 0
contador = True

while contador:                                              # Há um erro na lógica, o acumulador não vai zerar!
    acumulador += (valor_emprestado * (juros/100)) - parcela # É necessário corrigir isso!
    meses += 1
    if acumulador <= 0:
        break
print("A dívida será paga em %d meses, o total pago será de R$ %5.2f e o total de juros pagos será de R$ %5.2f"
      % (meses, (meses * parcela), ((meses * parcela) - valor_emprestado)))
