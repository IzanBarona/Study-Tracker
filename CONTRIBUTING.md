# Guía de Contribución

¡Gracias por tu interés en contribuir a Study Tracker! 🎉

## Cómo contribuir

### 1. Fork y Clone
1. Haz fork del repositorio
2. Clona tu fork: `git clone https://github.com/tu-usuario/study-tracker.git`
3. Crea una rama: `git checkout -b feature/mi-nueva-funcionalidad`

### 2. Estándares de Código

#### Estilo
- Sigue PEP 8 para el estilo de código Python
- Usa nombres descriptivos para variables y funciones
- Añade docstrings a todas las clases y funciones
- Mantén las líneas bajo 88 caracteres cuando sea posible

#### Type Hints
- Usa type hints en todas las funciones nuevas
- Ejemplo: `def add_task(self, title: str, priority: str) -> bool:`

#### Comentarios
- Escribe comentarios claros para lógica compleja
- Los comentarios deben explicar el "por qué", no el "qué"

### 3. Testing

Antes de enviar tu PR, asegúrate de:
- Probar manualmente todas las funcionalidades nuevas
- Verificar que no rompiste funcionalidades existentes
- Probar con diferentes escenarios (casos límite)

### 4. Commits

Usa mensajes de commit descriptivos:
```
✅ Buenos ejemplos:
- "Añade función para exportar tareas a CSV"
- "Corrige bug en cálculo de rachas"
- "Mejora rendimiento del sistema de puntos"

❌ Malos ejemplos:
- "fix"
- "cambios"
- "update"
```

### 5. Pull Request

1. Asegúrate de que tu código funciona
2. Actualiza el README si añades funcionalidades
3. Describe claramente qué cambia tu PR
4. Referencia issues relacionados

Plantilla de PR:
```markdown
## Descripción
[Descripción clara de los cambios]

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Mejora de código
- [ ] Documentación

## Testing
[Describe cómo probaste los cambios]

## Screenshots (si aplica)
[Añade capturas de pantalla]
```

## Ideas para contribuir

### Funcionalidades sugeridas
- [ ] Interfaz gráfica con Tkinter
- [ ] Exportar datos a PDF/CSV
- [ ] Notificaciones de escritorio
- [ ] Gráficos de progreso
- [ ] Temas de colores personalizables
- [ ] Integración con calendarios
- [ ] Sistema de etiquetas para tareas
- [ ] Modo Pomodoro integrado
- [ ] Estadísticas avanzadas

### Mejoras de código
- [ ] Añadir tests unitarios
- [ ] Mejorar manejo de errores
- [ ] Optimizar rendimiento
- [ ] Añadir logging
- [ ] Internacionalización (i18n)

### Documentación
- [ ] Tutorial en video
- [ ] Más ejemplos de uso
- [ ] Traducción a otros idiomas
- [ ] FAQ

## Código de Conducta

- Sé respetuoso con otros colaboradores
- Acepta críticas constructivas
- Enfócate en lo mejor para el proyecto
- Mantén un ambiente inclusivo y acogedor

## ¿Preguntas?

Si tienes dudas, abre un issue con la etiqueta "question" o contacta a los maintainers.

## ¡Gracias!

Toda contribución, grande o pequeña, es valiosa y apreciada. 🙌
