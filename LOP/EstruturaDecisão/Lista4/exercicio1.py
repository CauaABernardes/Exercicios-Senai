aresta_x = float(input("Digite quantos metros tem a aresta 'X': "))
aresta_Y = float(input("Digite quantos metros tem a aresta 'Y': "))
aresta_Z = float(input("Digite quantos metros tem a aresta 'Z': "))

area_xy = (aresta_x * aresta_Y)
area_xz = (aresta_x * aresta_Z)
area_yz = (aresta_Y * aresta_Z)

area_total = ((2 * area_xy) + (2 * area_xz) + (2 * area_yz))

qtd_litros_por_metro = (area_total * 3)

qtd_latas = ((qtd_litros_por_metro // 5) + 1)
valor_lata_tinta = (qtd_latas * 45)

qtd_rolos_tinta = ((area_total // 10) + 1)
valor_rolo = (qtd_rolos_tinta * 5)

mao_de_obra = (20 * area_total)

valor_total = (mao_de_obra + valor_lata_tinta + valor_rolo)

print(f"A quantindade de tinta necessária para a pintura externa é: {qtd_litros_por_metro} litros de tinta, ou {qtd_latas} latas de tinta"
      f"\nCustando R${valor_total}")