"""Figuras F9-F11, usadas na apresentacao.

Le so data/processed/, entao nao depende do parquet.

    python src/figuras_extra.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

import viz

RAIZ = Path(__file__).resolve().parents[1]
PROCESSADO = RAIZ / "data" / "processed"
N_ANOS = 4  # recorte 2022-2025

# Mesma lista da Figura 6 do notebook.
LITORAL = {
    "BALNEARIO PINHAL", "IMBE", "ARROIO DO SAL", "TRAMANDAI", "XANGRI LA",
    "CAPAO DA CANOA", "TORRES", "CIDREIRA", "OSORIO", "MOSTARDAS", "TAVARES",
    "PALMARES DO SUL", "DOM PEDRO DE ALCANTARA", "TERRA DE AREIA",
    "TRES CACHOEIRAS", "MAQUINE",
}


def f9_volume_versus_taxa(mun: pd.DataFrame) -> None:
    """Slopegraph: top 10 por volume bruto vs. top 10 por taxa (50 mil+ hab.)."""
    grandes = mun[mun["populacao"] >= 50_000]
    volume = grandes.nlargest(10, "n_ocorrencias")["municipio"].tolist()
    taxa = grandes.nlargest(10, "taxa_100k")["municipio"].tolist()
    nos_dois = set(volume) & set(taxa)

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    for lado, nomes in ((0, volume), (1, taxa)):
        for pos, nome in enumerate(nomes):
            manteve = nome in nos_dois
            cor = viz.TINTA["primaria"] if manteve else viz.DESTAQUE
            ax.text(lado, pos, nome.title(),
                    ha="right" if lado == 0 else "left",
                    va="center", fontsize=9, color=cor,
                    fontweight="normal" if manteve else "bold")

    for nome in nos_dois:
        ax.plot([0.04, 0.96], [volume.index(nome), taxa.index(nome)],
                color=viz.TINTA["eixo"], linewidth=1.2, zorder=0)

    # Como texto, porque rotulo de eixo no topo colide com o subtitulo.
    for lado, rotulo in ((0, "por volume bruto"), (1, "por taxa/100 mil hab.")):
        ax.text(lado, -1.15, rotulo, ha="right" if lado == 0 else "left",
                va="center", fontsize=9.5, fontweight="bold",
                color=viz.TINTA["secundaria"])

    ax.set_xlim(-0.62, 1.62)
    ax.set_ylim(9.7, -1.7)
    ax.set_xticks([])
    ax.set_yticks([])
    viz.limpar_grade(ax)
    for lado in ax.spines.values():
        lado.set_visible(False)
    viz.titular(ax, "O criterio muda a lista",
                "10 maiores municipios de 50 mil+ hab.; em laranja, "
                "quem aparece so de um lado")
    viz.salvar(fig, "f9_volume_vs_taxa")
    plt.close(fig)


def f10_composicao_macro(auditoria: pd.DataFrame) -> None:
    """Participacao de cada macrocategoria, destacando os crimes de rua."""
    from limpeza import CRIMES_DE_RUA

    comp = (auditoria.groupby("macro")["registros"].sum()
            .sort_values(ascending=True) / auditoria["registros"].sum() * 100)

    cores = [viz.SERIES[0] if m in CRIMES_DE_RUA else viz.NEUTRO for m in comp.index]
    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.barh(comp.index, comp.values, color=cores)
    viz.rotular_barras(ax, "{:.1f}%", horizontal=True)
    ax.set_xlim(0, comp.max() * 1.18)
    viz.titular(ax, "O que entra nos crimes de rua",
                "participacao de cada macrocategoria (%); em azul, as 9 "
                "categorias sensiveis a patrulhamento")
    viz.salvar(fig, "f10_composicao_macro")
    plt.close(fig)


def f11_taxa_versus_populacao(mun: pd.DataFrame) -> None:
    """Dispersao taxa x populacao: a variancia explode nos municipios pequenos."""
    grupo = pd.Series("demais", index=mun.index)
    grupo[mun["municipio"].isin(LITORAL)] = "litoral"
    grupo[(mun["populacao"] >= 50_000) & (grupo == "demais")] = "50 mil+ hab."

    estilo = {
        "demais": (viz.NEUTRO, "o", 16, 0.5),
        "50 mil+ hab.": (viz.SERIES[0], "o", 34, 0.9),
        "litoral": (viz.DESTAQUE, "^", 46, 0.95),
    }

    fig, ax = plt.subplots(figsize=(8.5, 5))
    for nome, (cor, marca, tam, alfa) in estilo.items():
        sub = mun[grupo == nome]
        ax.scatter(sub["populacao"], sub["taxa_100k"], s=tam, c=cor,
                   marker=marca, alpha=alfa, linewidths=0, label=nome)

    ax.axvline(50_000, color=viz.TINTA["eixo"], linewidth=1, linestyle=(0, (4, 3)))
    ax.text(52_000, ax.get_ylim()[1] * 0.97, "corte de 50 mil hab.",
            fontsize=8, color=viz.TINTA["suave"], va="top")
    ax.set_xscale("log")
    ax.set_xlabel("populacao (Censo 2022, escala log)")
    ax.set_ylabel("taxa/100 mil hab. por ano")
    ax.legend(loc="lower right")
    viz.titular(ax, "Municipio pequeno, taxa instavel",
                "cada ponto e um dos 497 municipios do RS; a dispersao encolhe "
                "conforme a populacao cresce")
    viz.salvar(fig, "f11_taxa_vs_populacao")
    plt.close(fig)


def main() -> None:
    viz.aplicar_estilo()
    mun = pd.read_csv(PROCESSADO / "municipios_taxa.csv")
    auditoria = pd.read_csv(PROCESSADO / "auditoria_macrocategorias.csv")

    f9_volume_versus_taxa(mun)
    f10_composicao_macro(auditoria)
    f11_taxa_versus_populacao(mun)
    print("Geradas: f9_volume_vs_taxa, f10_composicao_macro, f11_taxa_vs_populacao")
    print(f"  em {viz.FIGURAS}")


if __name__ == "__main__":
    main()
