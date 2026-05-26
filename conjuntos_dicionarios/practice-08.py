
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

team_tasks = equipe_a.union(equipe_b)

print('Tarefas das equipes:', team_tasks)
task_to_remove = input("Informe a tarefa que deseja remover\t->")

if task_to_remove in team_tasks:
    team_tasks.discard(task_to_remove)
else:
    print("Tarefa não encontrada no conjunto de tarefas da equipe.")

print("Tarefas finais:", team_tasks)
