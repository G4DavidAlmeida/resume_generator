# AGENTS.md — Gerador de Currículo

Este projeto utiliza **skills** do VS Code Copilot para automatizar a criação e manutenção de currículos.

## Skills disponíveis

| Skill | Descrição | Como invocar |
|---|---|---|
| `generate-dossiê` | Cria ou atualiza o dossiê profissional | `/generate-dossiê` |
| `generate-resume` | Gera `curriculo.html` para uma vaga específica | `/generate-resume` |

As skills estão em `.agents/skills/`.

## Fluxo típico

1. **Crie/atualize o dossiê** → `/generate-dossiê`
2. **Crie a pasta da vaga** com `descrição.md`
3. **Gere o currículo** → `/generate-resume`
4. **Gere o PDF** → `uv run main.py curriculos/YYYY-MM-DD/empresa/cargo/`
