def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento a partir del monto total y un porcentaje de descuento.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto 10%)
    :return: float - Monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
total_compra_1 = 100  # Ejemplo de compra
monto_descuento_1 = calcular_descuento(total_compra_1)
monto_final_1 = total_compra_1 - monto_descuento_1
print(f"Compra 1: Total = ${total_compra_1}, Descuento = ${monto_descuento_1}, Monto final = ${monto_final_1}")

total_compra_2 = 200  # Ejemplo de otra compra
porcentaje_descuento_2 = 15  # Aplicando un descuento del 15%
monto_descuento_2 = calcular_descuento(total_compra_2, porcentaje_descuento_2)
monto_final_2 = total_compra_2 - monto_descuento_2
print(f"Compra 2: Total = ${total_compra_2}, Descuento = ${monto_descuento_2}, Monto final = ${monto_final_2}")
