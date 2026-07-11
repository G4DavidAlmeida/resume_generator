#!/usr/bin/env python3
"""
Gerador de Currículo PDF

Converte curriculo.html + global.css em PDF usando WeasyPrint.
Uso: uv run main.py <caminho-da-pasta>

A pasta deve seguir a estrutura:
  curriculos/YYYY-MM-DD/empresa/cargo/
    ├── descrição.md          (contexto da vaga)
    └── curriculo.html        (currículo formatado)

O CSS global fica na raiz do projeto: global.css
O PDF será gerado na mesma pasta com o nome:
  "curriculo - {Empresa}, {Cargo}.pdf"
"""

import argparse
import sys
from pathlib import Path

from weasyprint import HTML, CSS


# Raiz do projeto: mesmo diretório onde este script está
PROJECT_ROOT = Path(__file__).resolve().parent
GLOBAL_CSS = PROJECT_ROOT / "global.css"


def extrair_empresa_cargo(pasta_alvo: Path) -> tuple[str, str]:
    """
    Extrai o nome da empresa e o cargo a partir da estrutura de pastas.

    Exemplo:
      curriculos/2026-07-11/empresa/backend-python/
      → empresa = "empresa", cargo = "backend-python"
    """
    partes = pasta_alvo.resolve().parts

    if "curriculos" in partes:
        idx = partes.index("curriculos")
        if len(partes) > idx + 3:
            empresa = partes[idx + 2]
            cargo = partes[idx + 3]
            return empresa, cargo

    empresa = partes[-2] if len(partes) >= 2 else "empresa"
    cargo = partes[-1] if len(partes) >= 1 else "cargo"
    return empresa, cargo


def gerar_pdf(pasta_alvo: Path) -> Path:
    """
    Gera o PDF a partir do curriculo.html + global.css.
    Retorna o path do PDF gerado.
    """
    html_path = pasta_alvo / "curriculo.html"

    if not html_path.is_file():
        raise FileNotFoundError(
            f"Arquivo 'curriculo.html' não encontrado em: {pasta_alvo}"
        )

    if not GLOBAL_CSS.is_file():
        raise FileNotFoundError(
            f"Arquivo 'global.css' não encontrado na raiz do projeto: {GLOBAL_CSS}"
        )

    print(f"📄 HTML : {html_path}")
    print(f"🎨 CSS  : {GLOBAL_CSS}")

    empresa, cargo = extrair_empresa_cargo(pasta_alvo)

    empresa_formatada = empresa.replace("_", " ").replace("-", " ").title()
    cargo_formatado = cargo.replace("_", " ").replace("-", " ").title()
    nome_pdf = f"curriculo - {empresa_formatada}, {cargo_formatado}.pdf"
    pdf_path = pasta_alvo / nome_pdf

    print(f"📦 PDF  : {pdf_path}")
    print(f"🏢 Empresa: {empresa_formatada}")
    print(f"💼 Cargo  : {cargo_formatado}")

    doc = HTML(filename=str(html_path))
    css = CSS(filename=str(GLOBAL_CSS))

    doc.write_pdf(target=str(pdf_path), stylesheets=[css])

    print(f"✅ PDF gerado com sucesso: {pdf_path}")
    return pdf_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera o currículo PDF a partir de HTML+CSS.",
    )
    parser.add_argument(
        "pasta",
        type=str,
        help="Caminho para a pasta-alvo do currículo "
        "(ex.: curriculos/2026-07-11/empresa/backend-python/). "
        "Deve conter 'curriculo.html'.",
    )
    args = parser.parse_args()

    pasta_alvo = Path(args.pasta).resolve()

    if not pasta_alvo.is_dir():
        print(f"❌ Erro: o caminho informado não é uma pasta válida: {pasta_alvo}",
              file=sys.stderr)
        sys.exit(1)

    try:
        pdf_path = gerar_pdf(pasta_alvo)
        print(f"\n✨ Pronto! Currículo salvo em: {pdf_path}")
    except FileNotFoundError as e:
        print(f"❌ Erro: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado ao gerar o PDF: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
