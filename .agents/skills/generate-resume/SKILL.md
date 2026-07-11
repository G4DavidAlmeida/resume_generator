---
name: generate-resume
description: 'Generate curriculo.html tailored to a specific job opening. Use when the user wants to create a customized CV for a job application based on the professional dossier (dossiê.md) and a job description (descrição.md).'
argument-hint: 'path to job folder (e.g. curriculos/2026-07-11/empresa/cargo/)'
---

# Generate Resume

Gera o arquivo `curriculo.html` para uma vaga específica, utilizando como base o **dossiê profissional** (`dossiê.md`) e o **contexto da vaga** (`descrição.md`).

## Estrutura do projeto

```
.
├── dossiê.md              ← Fonte de verdade com TODO o perfil profissional
├── global.css             ← Estilos globais do currículo (não alterar)
├── main.py                ← Script que converte curriculo.html → PDF
└── curriculos/
    └── YYYY-MM-DD/
        └── empresa/
            └── cargo/
                ├── descrição.md       ← Contexto da vaga (fornecido pelo usuário)
                ├── curriculo.html     ← VOCÊ GERA ESTE ARQUIVO
                └── *.pdf              ← Gerado pelo script main.py
```

## Fluxo de trabalho

1. O usuário aponta para uma pasta de vaga:
   `curriculos/YYYY-MM-DD/empresa/cargo/`

2. Você **lê** dois arquivos:
   - `dossiê.md` (raiz) — perfil profissional completo
   - `descrição.md` (pasta da vaga) — contexto: empresa, vaga, requisitos

3. Você **gera** `curriculo.html` na pasta da vaga com:
   - HTML semântico e limpo
   - Conteúdo extraído e adaptado do dossiê, priorizando o que é relevante para a vaga
   - `<link rel="stylesheet" href="../../../../global.css">` no `<head>` (caminho relativo da pasta da vaga até a raiz)

## Regras de conteúdo

### O que NÃO fazer
- **Não invente** informações que não estejam no dossiê
- **Não altere** `global.css` — o CSS é fixo e compartilhado
- **Não modifique** `dossiê.md`

### O que FAZER
- Selecione as experiências, competências e formações do dossiê que mais se alinham com a vaga descrita em `descrição.md`
- Adapte o resumo profissional para destacar o que interessa à empresa
- Se a vaga for backend, reduza destaque em frontend
- Se a vaga for full stack, mantenha React, Vue, TypeScript e JavaScript com mais visibilidade
- Se a vaga mencionar AI, OCR, automação ou documentos, destaque PED, Textract, Tesseract, OpenCV
- Se a vaga mencionar cloud, destaque AWS S3, AWS Textract e hospedagem
- Se a vaga mencionar testes, destaque pytest, Selenium, Playwright, Cypress
- Se não houver vaga específica (indicação, carta de apresentação), monte um currículo generalista com os pontos fortes do candidato
- Evite exagerar impacto numérico; prefira destacar complexidade técnica e confiabilidade

### Restrição de páginas
- **O PDF final deve ter exatamente 2 páginas.** Ajuste a quantidade de bullets, o nível de detalhe das experiências e o tamanho do resumo para que o conteúdo ocupe 2 páginas A4 no total — nem mais, nem menos.

### Estrutura HTML esperada

Use as classes CSS definidas em `global.css`:

- `resume-header` / `resume-header__name` / `resume-header__contact` — cabeçalho
- `section-title` — títulos de seção
- `summary` — resumo profissional
- `experience-entry` / `experience-entry__header` / `experience-entry__role` / `experience-entry__period` / `experience-entry__company` / `experience-entry__context` / `experience-entry__details` — experiências
- `highlights-grid` — realizações em grid
- `skills-category` / `skills-category__name` / `skills-category__list` — competências
- `edu-entry` / `cert-entry` — formação e certificações
- `availability-tags` / `tag` — tags de disponibilidade
- `resume-footer` — rodapé

## Como gerar o PDF

Depois que `curriculo.html` estiver pronto, o usuário executará:

```bash
uv run main.py curriculos/YYYY-MM-DD/empresa/cargo/
```

O script:
- Lê `curriculo.html` da pasta alvo
- Carrega `global.css` da raiz do projeto
- Gera o PDF com WeasyPrint
- Salva como `curriculo - {Empresa}, {Cargo}.pdf` na mesma pasta
