"""
Study Tracker - Gestor de Tareas y Hábitos para Estudiantes
Un sistema de organización y gamificación para ayudar a adolescentes
a gestionar sus estudios y desarrollar buenos hábitos.
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import sys


class Task:
    """Representa una tarea con prioridad, fecha límite y estado."""
    
    def __init__(self, title: str, description: str, priority: str, 
                 due_date: str, category: str = "General"):
        self.id = datetime.now().timestamp()
        self.title = title
        self.description = description
        self.priority = priority  # "Alta", "Media", "Baja"
        self.due_date = due_date
        self.category = category
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convierte la tarea a diccionario para JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "category": self.category,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Crea una tarea desde un diccionario."""
        task = cls(
            data["title"],
            data["description"],
            data["priority"],
            data["due_date"],
            data.get("category", "General")
        )
        task.id = data["id"]
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task
    
    def is_overdue(self) -> bool:
        """Verifica si la tarea está vencida."""
        if self.completed:
            return False
        try:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return due.date() < datetime.now().date()
        except:
            return False
    
    def days_until_due(self) -> int:
        """Calcula días hasta la fecha límite."""
        try:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            delta = due.date() - datetime.now().date()
            return delta.days
        except:
            return 999


class Habit:
    """Representa un hábito a seguir con racha y estadísticas."""
    
    def __init__(self, name: str, description: str, target_days: int = 7):
        self.id = datetime.now().timestamp()
        self.name = name
        self.description = description
        self.target_days = target_days
        self.completed_dates = []
        self.current_streak = 0
        self.best_streak = 0
        self.created_at = datetime.now().strftime("%Y-%m-%d")
    
    def mark_completed(self, date: str = None) -> bool:
        """Marca el hábito como completado para hoy."""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        if date not in self.completed_dates:
            self.completed_dates.append(date)
            self.update_streak()
            return True
        return False
    
    def update_streak(self):
        """Actualiza la racha actual y mejor racha."""
        if not self.completed_dates:
            self.current_streak = 0
            return
        
        sorted_dates = sorted([datetime.strptime(d, "%Y-%m-%d") 
                              for d in self.completed_dates])
        
        streak = 1
        max_streak = 1
        
        for i in range(1, len(sorted_dates)):
            diff = (sorted_dates[i] - sorted_dates[i-1]).days
            if diff == 1:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 1
        
        # Verificar si la racha actual está activa
        last_date = sorted_dates[-1].date()
        today = datetime.now().date()
        if (today - last_date).days <= 1:
            self.current_streak = streak
        else:
            self.current_streak = 0
        
        self.best_streak = max(max_streak, self.best_streak)
    
    def to_dict(self) -> Dict:
        """Convierte el hábito a diccionario para JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "target_days": self.target_days,
            "completed_dates": self.completed_dates,
            "current_streak": self.current_streak,
            "best_streak": self.best_streak,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Habit':
        """Crea un hábito desde un diccionario."""
        habit = cls(
            data["name"],
            data["description"],
            data.get("target_days", 7)
        )
        habit.id = data["id"]
        habit.completed_dates = data["completed_dates"]
        habit.current_streak = data["current_streak"]
        habit.best_streak = data["best_streak"]
        habit.created_at = data["created_at"]
        return habit


class StudyTracker:
    """Sistema principal de gestión de tareas y hábitos."""
    
    def __init__(self, data_file: str = "study_data.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.habits: List[Habit] = []
        self.points = 0
        self.level = 1
        self.load_data()
    
    def load_data(self):
        """Carga datos desde el archivo JSON."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
                    self.habits = [Habit.from_dict(h) for h in data.get("habits", [])]
                    self.points = data.get("points", 0)
                    self.level = data.get("level", 1)
            except Exception as e:
                print(f"Error al cargar datos: {e}")
    
    def save_data(self):
        """Guarda datos en el archivo JSON."""
        data = {
            "tasks": [t.to_dict() for t in self.tasks],
            "habits": [h.to_dict() for h in self.habits],
            "points": self.points,
            "level": self.level
        }
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar datos: {e}")
    
    def add_task(self, title: str, description: str, priority: str, 
                 due_date: str, category: str = "General"):
        """Añade una nueva tarea."""
        task = Task(title, description, priority, due_date, category)
        self.tasks.append(task)
        self.save_data()
        print(f"✅ Tarea '{title}' añadida con éxito!")
    
    def complete_task(self, task_id: float) -> bool:
        """Marca una tarea como completada y otorga puntos."""
        for task in self.tasks:
            if task.id == task_id and not task.completed:
                task.completed = True
                
                # Sistema de puntos según prioridad
                points_map = {"Alta": 30, "Media": 20, "Baja": 10}
                earned_points = points_map.get(task.priority, 10)
                
                # Bonus por completar antes de tiempo
                if task.days_until_due() > 0:
                    earned_points += 10
                
                self.add_points(earned_points)
                self.save_data()
                print(f"🎉 ¡Tarea completada! +{earned_points} puntos")
                return True
        return False
    
    def add_habit(self, name: str, description: str, target_days: int = 7):
        """Añade un nuevo hábito."""
        habit = Habit(name, description, target_days)
        self.habits.append(habit)
        self.save_data()
        print(f"✅ Hábito '{name}' creado con éxito!")
    
    def complete_habit(self, habit_id: float) -> bool:
        """Marca un hábito como completado hoy."""
        for habit in self.habits:
            if habit.id == habit_id:
                if habit.mark_completed():
                    points = 15
                    if habit.current_streak > 0:
                        points += habit.current_streak * 5
                    
                    self.add_points(points)
                    self.save_data()
                    print(f"🔥 ¡Hábito completado! Racha: {habit.current_streak} días. +{points} puntos")
                    return True
                else:
                    print("⚠️ Ya completaste este hábito hoy")
                    return False
        return False
    
    def add_points(self, points: int):
        """Añade puntos y verifica subida de nivel."""
        self.points += points
        new_level = (self.points // 100) + 1
        
        if new_level > self.level:
            self.level = new_level
            print(f"🌟 ¡NIVEL {self.level} ALCANZADO! ¡Sigue así!")
    
    def get_pending_tasks(self) -> List[Task]:
        """Obtiene tareas pendientes ordenadas por prioridad y fecha."""
        pending = [t for t in self.tasks if not t.completed]
        priority_order = {"Alta": 0, "Media": 1, "Baja": 2}
        return sorted(pending, 
                     key=lambda t: (priority_order.get(t.priority, 3), 
                                   t.days_until_due()))
    
    def get_stats(self) -> Dict:
        """Obtiene estadísticas generales."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for t in self.tasks if t.completed)
        overdue_tasks = sum(1 for t in self.tasks if t.is_overdue())
        
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": total_tasks - completed_tasks,
            "overdue_tasks": overdue_tasks,
            "total_habits": len(self.habits),
            "points": self.points,
            "level": self.level
        }


def print_menu():
    """Muestra el menú principal."""
    print("\n" + "="*50)
    print("📚 STUDY TRACKER - Tu Asistente de Estudio 📚")
    print("="*50)
    print("1. 📝 Ver tareas pendientes")
    print("2. ➕ Añadir nueva tarea")
    print("3. ✅ Completar tarea")
    print("4. 🔄 Ver hábitos")
    print("5. 🆕 Añadir nuevo hábito")
    print("6. ✓ Completar hábito de hoy")
    print("7. 📊 Ver estadísticas")
    print("8. 🚪 Salir")
    print("="*50)


def display_tasks(tracker: StudyTracker):
    """Muestra las tareas pendientes."""
    tasks = tracker.get_pending_tasks()
    
    if not tasks:
        print("\n🎉 ¡No tienes tareas pendientes! Buen trabajo.")
        return
    
    print("\n📋 TAREAS PENDIENTES:")
    print("-" * 80)
    
    for i, task in enumerate(tasks, 1):
        status = "⚠️ VENCIDA" if task.is_overdue() else f"📅 {task.days_until_due()} días"
        priority_icon = {"Alta": "🔴", "Media": "🟡", "Baja": "🟢"}.get(task.priority, "⚪")
        
        print(f"\n{i}. {priority_icon} [{task.priority}] {task.title}")
        print(f"   📖 {task.description}")
        print(f"   🏷️  Categoría: {task.category}")
        print(f"   {status} | Fecha límite: {task.due_date}")
        print(f"   ID: {task.id}")


def display_habits(tracker: StudyTracker):
    """Muestra los hábitos."""
    if not tracker.habits:
        print("\n💡 No tienes hábitos registrados aún.")
        return
    
    print("\n🎯 TUS HÁBITOS:")
    print("-" * 80)
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    for i, habit in enumerate(tracker.habits, 1):
        completed_today = today in habit.completed_dates
        status = "✅ Completado hoy" if completed_today else "⏳ Pendiente"
        
        print(f"\n{i}. {habit.name}")
        print(f"   📝 {habit.description}")
        print(f"   🔥 Racha actual: {habit.current_streak} días | Mejor racha: {habit.best_streak} días")
        print(f"   {status}")
        print(f"   ID: {habit.id}")


def main():
    """Función principal del programa."""
    tracker = StudyTracker()
    
    while True:
        print_menu()
        
        stats = tracker.get_stats()
        print(f"\n⭐ Nivel {stats['level']} | 🏆 {stats['points']} puntos")
        
        choice = input("\n👉 Elige una opción: ").strip()
        
        if choice == "1":
            display_tasks(tracker)
        
        elif choice == "2":
            print("\n➕ NUEVA TAREA")
            title = input("Título: ").strip()
            description = input("Descripción: ").strip()
            print("Prioridad: 1=Alta, 2=Media, 3=Baja")
            priority_num = input("Prioridad: ").strip()
            priority_map = {"1": "Alta", "2": "Media", "3": "Baja"}
            priority = priority_map.get(priority_num, "Media")
            due_date = input("Fecha límite (YYYY-MM-DD): ").strip()
            category = input("Categoría (ej: Matemáticas, Historia): ").strip() or "General"
            
            tracker.add_task(title, description, priority, due_date, category)
        
        elif choice == "3":
            display_tasks(tracker)
            if tracker.get_pending_tasks():
                try:
                    task_id = float(input("\nID de la tarea a completar: ").strip())
                    if not tracker.complete_task(task_id):
                        print("❌ No se encontró la tarea o ya está completada")
                except ValueError:
                    print("❌ ID inválido")
        
        elif choice == "4":
            display_habits(tracker)
        
        elif choice == "5":
            print("\n🆕 NUEVO HÁBITO")
            name = input("Nombre del hábito: ").strip()
            description = input("Descripción: ").strip()
            target = input("Meta de días seguidos (default 7): ").strip()
            target_days = int(target) if target.isdigit() else 7
            
            tracker.add_habit(name, description, target_days)
        
        elif choice == "6":
            display_habits(tracker)
            if tracker.habits:
                try:
                    habit_id = float(input("\nID del hábito completado hoy: ").strip())
                    if not tracker.complete_habit(habit_id):
                        print("❌ No se encontró el hábito")
                except ValueError:
                    print("❌ ID inválido")
        
        elif choice == "7":
            stats = tracker.get_stats()
            print("\n📊 ESTADÍSTICAS")
            print("-" * 50)
            print(f"📝 Tareas totales: {stats['total_tasks']}")
            print(f"✅ Completadas: {stats['completed_tasks']}")
            print(f"⏳ Pendientes: {stats['pending_tasks']}")
            print(f"⚠️  Vencidas: {stats['overdue_tasks']}")
            print(f"🎯 Hábitos: {stats['total_habits']}")
            print(f"⭐ Nivel: {stats['level']}")
            print(f"🏆 Puntos: {stats['points']}")
            
            # Siguiente nivel
            next_level_points = (stats['level'] * 100)
            remaining = next_level_points - stats['points']
            print(f"\n💪 {remaining} puntos para el nivel {stats['level'] + 1}")
        
        elif choice == "8":
            print("\n👋 ¡Hasta luego! Sigue estudiando fuerte 💪")
            break
        
        else:
            print("\n❌ Opción no válida")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()