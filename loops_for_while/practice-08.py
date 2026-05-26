projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for project in projetos:
    text_to_display = "Projeto ausente" if (project is None) else project

    print(text_to_display)

print("\nEnding process...")