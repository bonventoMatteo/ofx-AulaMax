from ofxparse import OfxParser

ARQUIVO = "extrato.ofx"


def ler_transacoes(caminho):
    with open(caminho, "rb") as arquivo:
        ofx = OfxParser.parse(arquivo)
    return ofx.account.statement.transactions


def descricao(t):
    # Alguns bancos preenchem apenas "payee" ou deixam o memo vazio
    return (t.memo or t.payee or "SEM DESCRIÇÃO").strip()


def main():
    transacoes = ler_transacoes(ARQUIVO)

    print("EXTRATO BANCÁRIO")
    print("=" * 40)

    entradas = 0
    saidas = 0

    for t in transacoes:
        print(f"Data      : {t.date.strftime('%d/%m/%Y')}")
        print(f"Valor     : R$ {t.amount:.2f}")
        print(f"Descrição : {descricao(t)}")
        print("-" * 40)

        if t.amount > 0:
            entradas += t.amount
        else:
            saidas += t.amount

    saldo = entradas + saidas

    print(f"Total de movimentações: {len(transacoes)}")
    print(f"Entradas: R$ {entradas:.2f}")
    print(f"Saídas  : R$ {saidas:.2f}")
    print(f"Saldo   : R$ {saldo:.2f}")


if __name__ == "__main__":
    main()
