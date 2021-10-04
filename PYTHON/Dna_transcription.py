#Aluno: Messias Henrique da Silva Santos
# Período: 2021.1

def transcricao(fitaDeDNA):
    mRNA = fitaDeDNA.replace("T", "U")
    return mRNA

def main():
    fitaDeDNA = "GTGCCGGCT"
    mRNA = transcricao(fitaDeDNA)
    print(mRNA)

if __name__ == "__main__":
    main()