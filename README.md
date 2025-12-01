# Sistema de gestion de servicios (CAT)
En este repositorio se encuentra toda la informacion que se va a estar trabajando durante el desarrollo del proyecto

## Requerimientos del Sistema de gestion de servicios

---

### Requerimientos Funcionales (RF)

| ID | Descripción del Requerimiento |
| :--- | :--- |
| **RF1** | El sistema debe permitir registrar solicitudes de soporte técnico con **descripción**, **categoría** y **prioridad**. |
| **RF2** | El sistema debe permitir **asignar solicitudes a técnicos específicos**. |
| **RF3** | El sistema debe permitir **actualizar el estado de una solicitud** (pendiente, en proceso, resuelto, cerrado). |
| **RF4** | El sistema debe **enviar notificaciones** al usuario cada vez que el estado cambie. |
| **RF5** | El sistema debe **generar reportes** de tiempos de atención y carga de trabajo por técnico. |

---

### Requerimientos No Funcionales (RNF)

| ID | Categoría | Descripción del Requerimiento |
| :--- | :--- | :--- |
| **RNF1** | **Rendimiento** | El sistema debe procesar cualquier acción del usuario en **menos de 3 segundos**. |
| **RNF2** | **Disponibilidad** | El sistema debe estar **disponible el 99% del tiempo** (excepto mantenimiento programado). |
| **RNF3** | **Seguridad** | El sistema debe **autenticar usuarios mediante credenciales institucionales**. |
| **RNF4** | **Usabilidad** | La interfaz debe ser **intuitiva** y **accesible desde dispositivos móviles**. |
| **RNF5** | **Escalabilidad** | El sistema debe **soportar al menos 500 usuarios concurrentes** sin degradación del rendimiento. |

## Planificación (Poker Planning)

**Escala utilizada:** Fibonacci (1, 2, 3, 5, 8, 13)

| Historia | Estimación | Justificación |
| :--- | :--- | :--- |
| **HU1** (Registro de solicitudes) | 5 | Requiere formulario + BD + validaciones |
| **HU2** (Adjuntar archivos) | 3 | Manejo de archivos simple |
| **HU3** (Prioridad solicitud) | 2 | Solo añadir campo y lógica |
| **HU4** (Ver solicitudes asignadas) | 5 | Filtrado + interfaz |
| **HU5** (Actualizar estado) | 3 | Cambios menores sobre HU4 |
| **HU6** (Asignación de técnicos) | 5 | Roles + visibilidad especial |
| **HU7** (Reportes) | 8 | Consultas complejas y gráficos |
| **HU8** (Notificaciones) | 8 | Triggers o colas de notificación |
| **HU9** (Histórico de solicitudes) | 3 | Filtro + consulta |
| **HU10** (Métricas avanzadas) | 8 | Recolección + visualización analítica |