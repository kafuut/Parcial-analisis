# Archivo: auth_manager.py

# Definición de Roles y sus Permisos
ROLES_PERMISOS = {
    "Administrador": ["CREAR_USUARIO", "VER_REPORTES", "ASIGNAR_TICKET", "ACTUALIZAR_ESTADO", "VER_INTERNO"],
    "Técnico": ["ASIGNAR_TICKET", "ACTUALIZAR_ESTADO", "VER_INTERNO", "AGREGAR_COMENTARIO"],
    "Usuario Final": ["CREAR_TICKET", "VER_PROPIOS_TICKETS", "AGREGAR_COMENTARIO"]
}

# Simulación de la base de datos de usuarios
USUARIOS_DB = {
    "admin1": {"nombre": "Admin Supremo", "rol": "Administrador"},
    "tecnicoA": {"nombre": "Juan Técnico", "rol": "Técnico"},
    "userB": {"nombre": "Ana Usuario", "rol": "Usuario Final"}
}

def verificar_permiso(usuario_id, permiso_requerido):
    """
    Verifica si un usuario tiene un permiso específico.
    """
    usuario = USUARIOS_DB.get(usuario_id)
    
    if not usuario:
        print(f"Error: Usuario '{usuario_id}' no encontrado.")
        return False
    
    rol = usuario["rol"]
    permisos_del_rol = ROLES_PERMISOS.get(rol, [])
    
    if permiso_requerido in permisos_del_rol:
        print(f"✅ Permiso '{permiso_requerido}' concedido a '{usuario_id}' ({rol}).")
        return True
    else:
        print(f"❌ Permiso '{permiso_requerido}' DENEGADO a '{usuario_id}' ({rol}).")
        return False

# --- Ejemplo de Uso ---

# Intento de ver reportes (solo Admin puede)
verificar_permiso("admin1", "VER_REPORTES")
verificar_permiso("tecnicoA", "VER_REPORTES")

print("-" * 30)

# Intento de asignar un ticket (Admin y Técnico pueden)
verificar_permiso("admin1", "ASIGNAR_TICKET")
verificar_permiso("userB", "ASIGNAR_TICKET")
