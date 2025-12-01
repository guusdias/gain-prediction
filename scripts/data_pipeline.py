import pandas as pd
from pathlib import Path
from typing import Tuple


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "adult.csv"


def carregar_dados(caminho: Path | None = None) -> pd.DataFrame:
    """
    Carrega o dataset Adult a partir de um caminho CSV.

    Parameters
    ----------
    caminho : Path | None
        Caminho para o arquivo CSV. Se None, usa o caminho padrão em data/adult.csv.
    """
    csv_path = caminho or DATA_PATH
    df = pd.read_csv(csv_path)
    return df


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpeza básica:
    - remove linhas totalmente duplicadas;
    - trata valores ausentes simples (se houver).
    """
    df = df.drop_duplicates().copy()
    return df


def separar_features_alvo(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Separa o dataframe em X (features) e y (alvo binário).

    A coluna alvo é 'income', que já vem como string ('>50K' ou '<=50K') e será
    convertida para 1 (renda >50K) e 0 (renda <=50K).
    """
    df = df.copy()
    y = (df["income"].str.strip() == ">50K").astype(int)
    X = df.drop(columns=["income"])
    return X, y


def pipeline_basico() -> Tuple[pd.DataFrame, pd.Series]:
    """
    Executa o pipeline básico de dados:
    - carrega o CSV;
    - aplica limpeza simples;
    - separa features e alvo.
    """
    df = carregar_dados()
    df = limpar_dados(df)
    X, y = separar_features_alvo(df)
    return X, y


if __name__ == "__main__":
    X, y = pipeline_basico()
    print("Shape de X:", X.shape)
    print("Shape de y:", y.shape)