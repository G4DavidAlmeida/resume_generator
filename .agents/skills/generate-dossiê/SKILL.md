---
name: generate-dossiê
description: 'Create or update the professional dossier (dossiê.md). Use when the user wants to build, expand, or refresh their comprehensive career profile including experience, skills, education, certifications, projects, and professional positioning.'
argument-hint: 'describe what to add/update (e.g. new job, skill, certification)'
---

# Generate Dossiê

Cria ou atualiza o **dossiê profissional** (`dossiê.md`) — o documento fonte que alimenta a geração de currículos customizados.

## Objetivo do dossiê

O `dossiê.md` é a **fonte de verdade** com todo o perfil profissional. Ele deve ser completo e detalhado, permitindo que o agente de geração de currículos selecione e adapte as informações mais relevantes para cada vaga específica.

## Estrutura do dossiê

O documento deve seguir esta estrutura de seções:

```
# Dossiê profissional

## 1. Posicionamento profissional
   - Perfil principal (parágrafo descritivo)
   - Cargos-alvo (lista priorizada)
   - Tipo de vaga desejada
   - Nível pretendido

## 2. Resumo profissional (português)
   - Parágrafo conciso com tempo de experiência, stacks, domínios

## 3. Headline / Título profissional
   - Opções de headline para diferentes focos (backend, full stack, etc.)

## 4. Informações de contato
   - Nome, localização, email, LinkedIn, GitHub, telefone

## 5. Experiência profissional
   - Lista reversa cronológica
   - Cada entrada: cargo, empresa, período, contexto, responsabilidades, tecnologias

## 6. Habilidades técnicas
   - Categorizadas: Backend, Frontend, DevOps, Dados, etc.

## 7. Formação acadêmica

## 8. Certificações

## 9. Idiomas

## 10. Projetos pessoais / Portfólio

## 11. Disponibilidade e preferências
   - Remoto/Presencial/Híbrido
   - Fuso horário
   - Setores de interesse
```

## Fluxo de trabalho

### Se o dossiê NÃO existe
1. Entreviste o usuário para coletar todas as informações listadas nas seções acima
2. Faça perguntas uma seção por vez
3. Gere o `dossiê.md` completo com todas as informações coletadas

### Se o dossiê JÁ existe
1. Leia o `dossiê.md` atual
2. Pergunte ao usuário o que ele deseja adicionar, atualizar ou remover
3. Aplique as alterações preservando a estrutura e o formato existentes
4. Não remova informações sem confirmar com o usuário

## Regras

- **Seja minucioso**: quanto mais detalhes no dossiê, melhores os currículos gerados
- **Use a voz do usuário**: escreva em primeira pessoa, como se fosse o profissional
- **Seja específico**: evite generalidades. Prefira tecnologias, métricas e contextos concretos
- **Mantenha a estrutura**: respeite a numeração e hierarquia das seções
- **Não invente**: todas as informações devem ser fornecidas ou confirmadas pelo usuário
- **Formato Markdown**: use títulos `#`, listas `-`, e formatação limpa para facilitar o parse
