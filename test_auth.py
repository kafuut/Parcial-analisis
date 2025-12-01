# test_auth.py
import unittest
# Importamos la función que queremos probar desde nuestro módulo
from auth_manager import verificar_permiso

class TestAuthManager(unittest.TestCase):
    
    # Prueba 1: Un administrador debe tener permiso para VER_REPORTES
    def test_admin_puede_ver_reportes(self):
        # Usamos assertEqual para verificar si la función retorna True
        self.assertEqual(verificar_permiso("admin1", "VER_REPORTES"), True)

    # Prueba 2: Un usuario final NO debe tener permiso para ASIGNAR_TICKET
    def test_usuario_final_no_puede_asignar_ticket(self):
        # Usamos assertEqual para verificar si la función retorna False
        self.assertEqual(verificar_permiso("userB", "ASIGNAR_TICKET"), False)
        
    # Prueba 3: Un técnico debe tener permiso para ACTUALIZAR_ESTADO
    def test_tecnico_puede_actualizar_estado(self):
        self.assertEqual(verificar_permiso("tecnicoA", "ACTUALIZAR_ESTADO"), True)
        
    # Prueba 4: Un usuario no existente debe fallar la verificación
    def test_usuario_inexistente_falla(self):
        self.assertEqual(verificar_permiso("nadie", "CREAR_TICKET"), False)

# Esto permite ejecutar las pruebas cuando se llama directamente al archivo
if __name__ == '__main__':
    unittest.main()
