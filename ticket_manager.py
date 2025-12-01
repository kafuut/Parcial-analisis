# Archivo: ticket_manager.py

# Diccionario simple que simula una base de datos de tickets
TICKETS_DB = {
    1024: {
        "id": 1024,
        "problema": "No puedo ingresar al VPN institucional",
        "categoria": "Redes y Conectividad",
        "prioridad": "Alta",
        "estado": "Resuelto",
        "asignado_a": "Juan Pérez",
        "historial": [
            {"usuario": "Sistema", "mensaje": "Ticket creado.", "fecha": "2025-11-15 10:00"},
            {"usuario": "Técnico Juan Pérez", "mensaje": "Se reinició el servicio y se verificó la cuenta.", "fecha": "2025-11-16 14:30"},
            {"usuario": "Usuario Ana Gómez", "mensaje": "Gracias, ya funciona correctamente.", "fecha": "2025-11-16 15:00"}
        ]
    }
}

def obtener_detalle_ticket(ticket_id):
    """
    Función que busca y muestra los detalles de un ticket específico.
    """
    ticket = TICKETS_DB.get(ticket_id)
    
    if not ticket:
        print(f"Error: No se encontró el ticket con ID #{ticket_id}")
        return

    print("=" * 40)
    print(f"** DETALLE DEL TICKET #{ticket['id']} **")
    print("=" * 40)
    print(f"Problema: {ticket['problema']}")
    print(f"Estado: {ticket['estado']}")
    print(f"Asignado a: {ticket['asignado_a']}")
    print("-" * 40)
    
    print(">>> HISTORIAL DE COMENTARIOS <<<")
    for evento in ticket['historial']:
        print(f"[{evento['fecha']}] {evento['usuario']}: {evento['mensaje']}")
    
    print("-" * 40)
    
    # Lógica de acción simple basada en el estado
    if ticket['estado'] in ["Resuelto", "En Proceso"]:
        print("Acción Sugerida: Cerrar Ticket")
    else:
        print("Acción Sugerida: Asignar a Técnico")

# --- Ejemplo de Uso ---
obtener_detalle_ticket(1024)
