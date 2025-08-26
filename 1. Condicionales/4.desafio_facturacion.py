CARGO_FIJO = 7000
COSTO_METRO = 200
IVA = .21

mts_consumidos = int(input('Ingrese cantidad de metros consumidos: '))
tipo_cliente = input('Ingrese tipo de cliente (Residencial, Comercial, Industrial): ')

costo_consumo = mts_consumidos * COSTO_METRO
sub_consumo = CARGO_FIJO + costo_consumo
bonificacion = 0
bonificacion_extra = 0
recargo = 0

match tipo_cliente:
    case 'Residencial':
        if mts_consumidos < 30:
            bonificacion = .1 * costo_consumo
        elif mts_consumidos > 80:
            recargo = .15 * costo_consumo

        if  sub_consumo < 35000:
            bonificacion_extra = .05 * costo_consumo 

    case 'Comercial':
        if mts_consumidos > 300:
            bonificacion = .12 * costo_consumo
        elif mts_consumidos > 150:
            bonificacion = .08 * costo_consumo
        elif mts_consumidos < 50:
            recargo = .05 * costo_consumo

    case 'Industrial':
        if mts_consumidos > 1000:
            bonificacion = .3 * costo_consumo
        elif mts_consumidos > 500:
            bonificacion = .2 * costo_consumo
        elif mts_consumidos < 200:
            recargo = .1 * costo_consumo
    case _:
        print('No es un tipo de cliente valido')

sub_impuestos = sub_consumo - bonificacion - bonificacion_extra + recargo
total = sub_impuestos * (IVA + 1)

print(f"""
        Tipo de cliente: {tipo_cliente}   Consumo en m3: {mts_consumidos}m3

        Cargo Fijo ${CARGO_FIJO}
        Costo de consumo ${costo_consumo}
        Subtotal de consumo: ${sub_consumo}
        Bonificaciones: ${bonificacion + bonificacion_extra}
        Recargos: ${recargo}
        Subtotal con recargos y bonificaciones: ${sub_impuestos}
        IVA (%21): ${IVA * sub_impuestos}
        --------------------------------------------------------------
        TOTAL: ${total}
""")
