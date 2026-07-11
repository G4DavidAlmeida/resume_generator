# Gerador de Currículo

Ferramenta para gerar currículos em PDF a partir de um dossiê profissional, usando HTML + CSS + WeasyPrint. Projetado para criar currículos customizados e direcionados para vagas específicas.

## Pré-requisitos

- **Python 3.14+**
- **[uv](https://docs.astral.sh/uv/)** — gerenciador de pacotes e ambientes Python

```bash
# Instalar dependências
uv sync
```

## Estrutura do projeto

```
.
├── dossiê.md              ← Perfil profissional completo (fonte de verdade)
├── global.css             ← Estilos CSS do currículo (compartilhado)
├── main.py                ← Script que converte HTML → PDF (WeasyPrint)
├── pyproject.toml         ← Configuração do projeto Python
├── AGENTS.md              ← Referência das skills disponíveis
├── .agents/skills/        ← Skills do Copilot
│   ├── generate-dossiê/   ← Cria/atualiza o dossiê profissional
│   └── generate-resume/   ← Gera curriculo.html para uma vaga
└── curriculos/            ← Currículos gerados (não versionado)
    └── YYYY-MM-DD/
        └── empresa/
            └── cargo/
                ├── descrição.md       ← Descrição da vaga
                ├── curriculo.html     ← HTML gerado
                └── *.pdf              ← PDF final
```

## Como usar

### 1. Configurar o dossiê profissional

Use a skill `/generate-dossiê` no Copilot Chat para criar ou atualizar seu perfil profissional completo. O dossiê é a base de todos os currículos gerados.

### 2. Preparar a vaga

Crie a estrutura de pastas para a vaga:

```
curriculos/2026-07-11/nome-da-empresa/nome-do-cargo/
└── descrição.md
```

No `descrição.md`, coloque o contexto da vaga: descrição da empresa, requisitos, tech stack, responsabilidades, diferenciais — qualquer informação relevante para adaptar o currículo.

### 3. Gerar o currículo

Use a skill `/generate-resume` apontando para a pasta da vaga. O agente irá:

1. Ler `dossiê.md` e `descrição.md`
2. Selecionar experiências, skills e formações mais relevantes
3. Gerar `curriculo.html` customizado para a vaga
4. Respeitar o limite de **exatamente 2 páginas A4**

### 4. Gerar o PDF

```bash
uv run main.py curriculos/YYYY-MM-DD/empresa/cargo/
```

O PDF será salvo na mesma pasta como `curriculo - Empresa, Cargo.pdf`.

## Customização

- **Estilos**: edite `global.css` para alterar cores, fontes, layout
- **Skills**: edite os arquivos em `.agents/skills/` para ajustar o comportamento dos agentes

## Licença

MIT
