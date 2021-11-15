
def comprobarLongitud(campo, dato):
    if(campo == 'nombre'):
        if(len(dato) < 5): return False
        else: return True
    if(campo == 'telefono'):
        if(len(dato) < 6): return False
        else: return True
    if(campo == 'cedula'):
        if(len(dato) < 8): return False
        else: return True
    if(campo == 'codigo'):
        if(len(dato) < 5): return False
        else: return True
    if(campo == 'nit'):
        if(len(dato) < 6): return True
        else: return True
    if(campo == 'eps'):
        if(len(dato) < 4): return False
        else: return True
    if(campo == 'afp'):
        if(len(dato) < 4): return False
        else: return True