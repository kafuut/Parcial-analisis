# Archivo: comments_manager.py
from datetime import datetime

# Simulación de la base de datos de tickets (asumiendo que ya existe)
TICKETS_DB = {
    1025: {
        "id": 1025,
        "problema": "La impresora no funciona",
        "estado": "En Proceso",
        "historial": [
            {"tipo": "publico", "usuario": "Usuario A", "mensaje": "Se creó el ticket.", "fecha": "2025-11-28 09:00"}
        ]
    }
}

def agregar_comentario(ticket_id, usuario, mensaje, tipo="publico"):
    """
    Agrega un comentario al historial del ticket.
    Tipo puede ser 'publico' (visible para todos) o 'interno' (solo para técnicos).
    """
    ticket = TICKETS_DB.get(ticket_id)
    
    if not ticket:
        print(f"Error: No se encontró el ticket ID #{ticket_id}")
        return False

    nuevo_comentario = {
        "tipo": tipo,
        "usuario": usuario,
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    ticket["historial"].append(nuevo_comentario)
    
    print(f"Comentario ({tipo}) agregado al Ticket #{ticket_id} por {usuario}.")
    return True

def mostrar_comentarios(ticket_id, es_tecnico=False):
    """
    Muestra los comentarios. Oculta los comentarios internos si no es técnico.
    """
    ticket = TICKETS_DB.get(ticket_id)
    
    if not ticket:
        print(f"Error: No se encontró el ticket ID #{ticket_id}")
        return

    print(f"\n--- Comentarios para Ticket #{ticket_id} (Rol: {'Técnico' if es_tecnico else 'Usuario'}) ---")
    
    for evento in ticket["historial"]:
        if evento["tipo"] == "publico" or es_tecnico:
            tipo_tag = "[INTERNO] " if evento["tipo"] == "interno" else ""
            print(f"[{evento['fecha']}] {tipo_tag}{evento['usuario']}: {evento['mensaje']}")

# --- Ejemplo de Uso ---
agregar_comentario(1025, "Técnico Laura", "El cartucho de tinta está vacío. Se procederá a cambiarlo.", tipo="interno")
agregar_comentario(1025, "Usuario A", "Espero la confirmación de la reparación.", tipo="publico")

print("\n--- Vista para Técnico ---")
mostrar_comentarios(1025, es_tecnico=True)

print("\n--- Vista para Usuario Final ---")
mostrar_comentarios(1025, es_tecnico=False)
