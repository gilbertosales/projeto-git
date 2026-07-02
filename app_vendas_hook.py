import pandas as pd
import streamlit as st

st.set_page_config(page_title="Análise de Vendas", layout="wide")


@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados/vendas.csv", encoding="latin-1")
    df["dtc_venda"] = pd.to_datetime(df["dtc_venda"], dayfirst=True, errors="coerce")
    return df


df = carregar_dados()

if "ano_sel" not in st.session_state:
    st.session_state.ano_sel = sorted(df["Ano_venda"].dropna().unique())
if "depto_sel" not in st.session_state:
    st.session_state.depto_sel = sorted(df["nom_departamento"].dropna().unique())


def on_ano_change():
    st.session_state.ano_sel = st.session_state.ano_widget


def on_depto_change():
    st.session_state.depto_sel = st.session_state.depto_widget


st.title("Análise de Vendas")

# Filtros com hook ativo (on_change dispara imediatamente ao alterar o widget)
with st.sidebar:
    st.header("Filtros")
    anos = sorted(df["Ano_venda"].dropna().unique())
    st.multiselect(
        "Ano",
        anos,
        default=st.session_state.ano_sel,
        key="ano_widget",
        on_change=on_ano_change,
    )
    departamentos = sorted(df["nom_departamento"].dropna().unique())
    st.multiselect(
        "Departamento",
        departamentos,
        default=st.session_state.depto_sel,
        key="depto_widget",
        on_change=on_depto_change,
    )

df_filtrado = df[
    df["Ano_venda"].isin(st.session_state.ano_sel)
    & df["nom_departamento"].isin(st.session_state.depto_sel)
]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Faturamento Total", f"R$ {df_filtrado['val_venda'].sum():,.2f}")
col2.metric("Qtd. Vendida", f"{df_filtrado['qtd_venda'].sum():,.0f}")
col3.metric("Nº de Pedidos", f"{df_filtrado['num_nota'].nunique():,}")
col4.metric("Ticket Médio", f"R$ {df_filtrado['val_venda'].mean():,.2f}")

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Vendas por Departamento")
    vendas_depto = (
        df_filtrado.groupby("nom_departamento")["val_venda"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(vendas_depto)

with col_b:
    st.subheader("Vendas por Marca")
    vendas_marca = (
        df_filtrado.groupby("Nom_marca")["val_venda"].sum().sort_values(ascending=False)
    )
    st.bar_chart(vendas_marca)

st.subheader("Evolução de Vendas por Ano/Mês")
col_mes = "M\xeas_venda"
vendas_tempo = (
    df_filtrado.groupby(["Ano_venda", col_mes])["val_venda"]
    .sum()
    .reset_index()
    .sort_values(["Ano_venda", col_mes])
)
vendas_tempo["periodo"] = (
    vendas_tempo["Ano_venda"].astype(str)
    + "-"
    + vendas_tempo[col_mes].astype(str).str.zfill(2)
)
st.line_chart(vendas_tempo.set_index("periodo")["val_venda"])

col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Top 10 Produtos")
    top_produtos = (
        df_filtrado.groupby("Nom_produto")["val_venda"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_produtos)

with col_d:
    st.subheader("Top 10 Vendedores")
    top_vendedores = (
        df_filtrado.groupby("nom_vendedor")["val_venda"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_vendedores)

st.subheader("Vendas por Cidade")
vendas_cidade = (
    df_filtrado.groupby("nom_cidade")["val_venda"].sum().sort_values(ascending=False)
)
st.bar_chart(vendas_cidade)

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado, use_container_width=True)
