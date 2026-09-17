"""Gera relatorio/tabelas_geradas.tex a partir de data/processed/.

    python src/tabelas_relatorio.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from scipy.stats import shapiro, skew

sys.path.insert(0, str(Path(__file__).resolve().parent))
from limpeza import CRIMES_DE_RUA

RAIZ = Path(__file__).resolve().parents[1]
PROCESSADO = RAIZ / "data" / "processed"
SAIDA = RAIZ / "relatorio" / "tabelas_geradas.tex"
N_ANOS = 4


def br(valor, casas: int = 0) -> str:
    """Milhar com ponto, decimal com virgula."""
    return f"{valor:,.{casas}f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def tabela_macrocategorias(auditoria: pd.DataFrame) -> str:
    total = auditoria["registros"].sum()
    g = (auditoria.groupby("macro")
         .agg(tipos=("tipo", "size"), registros=("registros", "sum"))
         .sort_values("registros", ascending=False))

    linhas = []
    for macro, r in g.iterrows():
        exemplo = auditoria[auditoria["macro"] == macro].nlargest(1, "registros").iloc[0]["tipo"]
        exemplo = exemplo.capitalize()
        if len(exemplo) > 30:
            exemplo = exemplo[:29] + "."
        marca = r"$\bullet$" if macro in CRIMES_DE_RUA else ""
        pct = r["registros"] / total * 100
        linhas.append(f"\\texttt{{{macro.replace('_', chr(92) + '_')}}} & {marca} & "
                      f"{int(r['tipos'])} & {br(r['registros'])} & {br(pct, 1)} & {exemplo} \\\\")
    return "\n".join(linhas)


def tabela_mesorregioes(mun: pd.DataFrame) -> str:
    reg = (mun.groupby("mesorregiao")
           .agg(n=("municipio", "size"), pop=("populacao", "sum"),
                occ=("n_ocorrencias", "sum"), mediana=("taxa_100k", "median")))
    reg["taxa"] = reg["occ"] / reg["pop"] / N_ANOS * 1e5

    linhas = []
    for nome, r in reg.sort_values("taxa", ascending=False).iterrows():
        taxas = mun.loc[mun["mesorregiao"] == nome, "taxa_100k"].dropna()
        _, p = shapiro(taxas)
        p_fmt = br(p, 3) if p >= 0.001 else r"$<$0,001"
        linhas.append(f"{nome.replace(' Rio-grandense', '')} & {int(r['n'])} & "
                      f"{br(r['pop'])} & {br(r['taxa'])} & {br(r['mediana'])} & "
                      f"{br(skew(taxas), 2)} & {p_fmt} \\\\")
    return "\n".join(linhas)


def main() -> None:
    auditoria = pd.read_csv(PROCESSADO / "auditoria_macrocategorias.csv")
    mun = pd.read_csv(PROCESSADO / "municipios_taxa.csv")

    SAIDA.write_text(
        "% Gerado por src/tabelas_relatorio.py -- NAO EDITAR A MAO.\n"
        "% Regenere com: python src/tabelas_relatorio.py\n\n"
        "\\newcommand{\\linhasmacro}{%\n" + tabela_macrocategorias(auditoria) + "\n}\n\n"
        "\\newcommand{\\linhasmeso}{%\n" + tabela_mesorregioes(mun) + "\n}\n"
    )
    print(f"Salvo: {SAIDA}")


if __name__ == "__main__":
    main()
