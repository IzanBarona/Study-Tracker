
# 📚 Study Tracker

Un gestor de tareas y hábitos gamificado para estudiantes adolescentes que quieren organizarse mejor y desarrollar buenos hábitos de estudio.

## 🎯 ¿Qué problema resuelve?

Muchos adolescentes tienen dificultades para:
- Organizar sus tareas escolares y deberes
- Recordar fechas de exámenes y entregas
- Mantener hábitos de estudio consistentes
- Sentirse motivados con sus estudios

**Study Tracker** combina gestión de tareas con gamificación para hacer el estudio más organizado y divertido.

## ✨ Características

### 📝 Gestión de Tareas
- Crear tareas con prioridades (Alta, Media, Baja)
- Fechas límite con alertas de vencimiento
- Categorización por materias
- Seguimiento de tareas completadas vs pendientes

### 🎯 Sistema de Hábitos
- Crear hábitos personalizados
- Seguimiento de rachas diarias
- Visualización de tu mejor racha histórica
- Recordatorios de hábitos pendientes

### 🏆 Gamificación
- **Sistema de puntos**: Gana puntos por completar tareas y hábitos
- **Niveles**: Sube de nivel cada 100 puntos
- **Bonificaciones**:
  - Completar tareas antes de tiempo: +10 puntos extra
  - Mantener rachas de hábitos: +5 puntos por día de racha
  - Tareas de alta prioridad: +30 puntos
  - Tareas de media prioridad: +20 puntos
  - Tareas de baja prioridad: +10 puntos

### 💾 Persistencia de Datos
- Todos los datos se guardan automáticamente en `study_data.json`
- No pierdes tu progreso al cerrar la aplicación

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior

### Pasos

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/study-tracker.git
cd study-tracker
```

2. Ejecuta el programa:
```bash
python study_tracker.py
```

¡No necesitas instalar dependencias adicionales! El proyecto usa solo la biblioteca estándar de Python.

## 📖 Cómo usar

### Menú Principal
Al ejecutar el programa verás 8 opciones:

```
1. 📝 Ver tareas pendientes
2. ➕ Añadir nueva tarea
3. ✅ Completar tarea
4. 🔄 Ver hábitos
5. 🆕 Añadir nuevo hábito
6. ✓ Completar hábito de hoy
7. 📊 Ver estadísticas
8. 🚪 Salir
```

### Ejemplo de uso: Crear una tarea

```
👉 Elige una opción: 2

➕ NUEVA TAREA
Título: Estudiar para examen de Matemáticas
Descripción: Repasar capítulos 4-6 de álgebra
Prioridad: 1=Alta, 2=Media, 3=Baja
Prioridad: 1
Fecha límite (YYYY-MM-DD): 2026-02-05
Categoría (ej: Matemáticas, Historia): Matemáticas

✅ Tarea 'Estudiar para examen de Matemáticas' añadida con éxito!
```

### Ejemplo de uso: Crear un hábito

```
👉 Elige una opción: 5

🆕 NUEVO HÁBITO
Nombre del hábito: Leer 30 minutos
Descripción: Leer cualquier libro por 30 minutos
Meta de días seguidos (default 7): 21

✅ Hábito 'Leer 30 minutos' creado con éxito!
```

## 🎮 Sistema de Puntos y Niveles

| Acción | Puntos |
|--------|--------|
| Completar tarea de prioridad baja | 10 pts |
| Completar tarea de prioridad media | 20 pts |
| Completar tarea de prioridad alta | 30 pts |
| Bonus por completar antes de tiempo | +10 pts |
| Completar hábito | 15 pts |
| Bonus por racha de hábito | +5 pts × días de racha |

**Niveles**: Cada 100 puntos subes un nivel. ¡El cielo es el límite!

## 📊 Ejemplo de Estadísticas

```
📊 ESTADÍSTICAS
--------------------------------------------------
📝 Tareas totales: 15
✅ Completadas: 10
⏳ Pendientes: 5
⚠️  Vencidas: 1
🎯 Hábitos: 3
⭐ Nivel: 3
🏆 Puntos: 285

💪 15 puntos para el nivel 4
```

## 🛠️ Estructura del Código

El proyecto está organizado en clases para facilitar su extensión:

- **`Task`**: Representa una tarea individual con todos sus atributos
- **`Habit`**: Maneja hábitos con sistema de rachas
- **`StudyTracker`**: Sistema principal que coordina tareas, hábitos y puntos

### Características técnicas
- Programación orientada a objetos
- Type hints para mejor legibilidad
- Serialización JSON para persistencia
- Manejo de fechas con datetime
- Sistema de cálculo de rachas automático

## 🎨 Personalización

Puedes modificar fácilmente:
- Los puntos otorgados por cada acción (líneas 204-218)
- Puntos necesarios para subir de nivel (línea 221)
- Categorías predeterminadas
- Formato de visualización

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Algunas ideas para mejorar:

- [ ] Interfaz gráfica (GUI) con Tkinter o PyQt
- [ ] Notificaciones de escritorio para recordatorios
- [ ] Exportar estadísticas a PDF o CSV
- [ ] Gráficos de progreso con matplotlib
- [ ] Sistema de recompensas desbloqueables
- [ ] Integración con calendarios (Google Calendar, Outlook)
- [ ] Modo multijugador/competitivo con amigos
- [ ] Aplicación móvil

## 📝 Licencia

MIT License - Libre para usar, modificar y distribuir.

## 👥 Autor

Creado para ayudar a estudiantes a organizarse mejor y desarrollar buenos hábitos de estudio.

## 🐛 Reportar bugs

Si encuentras algún error, por favor abre un issue en GitHub con:
- Descripción del problema
- Pasos para reproducirlo
- Comportamiento esperado vs actual

---

**¡Buena suerte con tus estudios! 📚💪**
