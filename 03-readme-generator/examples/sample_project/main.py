#!/usr/bin/env python3
"""
TaskFlow CLI — manage tasks from the command line.

A lightweight task manager that stores tasks in a local YAML file.
"""

import click
import yaml
from pathlib import Path

TASKS_FILE = Path.home() / '.taskflow' / 'tasks.yaml'


def load_tasks():
    """Load tasks from the local YAML store."""
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE) as f:
        return yaml.safe_load(f) or []


def save_tasks(tasks):
    """Save tasks to the local YAML store."""
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TASKS_FILE, 'w') as f:
        yaml.dump(tasks, f)


@click.group()
def cli():
    """TaskFlow: a lightweight command-line task manager."""
    pass


@cli.command()
@click.argument('title')
@click.option('--priority', '-p', default='medium',
              type=click.Choice(['low', 'medium', 'high']),
              help='Task priority (default: medium)')
def add(title, priority):
    """Add a new task."""
    tasks = load_tasks()
    task = {'id': len(tasks) + 1, 'title': title, 'priority': priority, 'done': False}
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"✓ Added [{priority}]: {title}")


@cli.command(name='list')
@click.option('--all', 'show_all', is_flag=True, help='Show completed tasks too')
def list_tasks(show_all):
    """List all pending tasks."""
    tasks = load_tasks()
    visible = tasks if show_all else [t for t in tasks if not t['done']]
    if not visible:
        click.echo("No tasks found.")
        return
    for task in visible:
        status = '✓' if task['done'] else '○'
        click.echo(f"  {status} [{task['id']}] [{task['priority']}] {task['title']}")


@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    """Mark a task as complete."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            click.echo(f"✓ Completed: {task['title']}")
            return
    click.echo(f"Task {task_id} not found.")


@cli.command()
@click.argument('task_id', type=int)
def remove(task_id):
    """Remove a task."""
    tasks = load_tasks()
    original_count = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    if len(tasks) < original_count:
        save_tasks(tasks)
        click.echo(f"✓ Removed task {task_id}")
    else:
        click.echo(f"Task {task_id} not found.")


if __name__ == '__main__':
    cli()
