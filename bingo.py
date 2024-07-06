
import streamlit as st
import random
import pandas as pd

def generate_bingo_board(words, seed):
    random.seed(seed)
    random.shuffle(words)
    return [words[i * 5:(i + 1) * 5] for i in range(5)]

def check_bingo(checked):
    # Check rows
    for row in range(5):
        if all(checked[row]):
            return "Linha!"
    # Check columns
    for col in range(5):
        if all(checked[row][col] for row in range(5)):
            return "Linha!"
    # Check for Bingo
    if all(all(row) for row in checked):
        return "BINGO!"
    return ""

def main():
    st.title("Bingo da VIII Convenção Nacional")

    words = ["Inerências", "Verdadeiramente liberal", "Burocracia",
             "Comité central", "Transparência", "Eu não sou jurista, mas...",
             "Delegados", "Separação de poderes", "José Cardoso",
             "Babuje", "RGPD", "Subscritores", "Distritais",
             "'Jota' ou 'Juventude' da IL", "Portal do Membro", "Órgão Máximo",
             "O partido é como uma empresa", "O partido é como o estado",
             "Salários", "Partilha de contactos", "Co-criação", "Realmente liberal",
             "Quórum", "Tens de terminar", "Ratificar", "Quotas",
             "Observador", "Alguém no zoom não aparece", "Viva Portugal, Viva a Iniciativa Liberal",
             "Leva a bebida para o púlpito", "Muito bem!", "Pin arco íris",
             "Estou no partido há pouco tempo", "O partido mudou",
             "Apupos", "Eu não ia falar...", "Problemas de som", "Está tudo a pensar no almoço/jantar",
             "Melancia azul", "Liberalómetro", "WOKE", "Estou mesmo a terminar..."]

    seed = st.number_input("Insere o teu número de membro:", min_value=1, max_value=9000, value=1)
    
    board = generate_bingo_board(words, seed)
    
    checked = [[False] * 5 for _ in range(5)]

    # Create the bingo board with checkboxes in a table format
    for i in range(5):
        cols = st.columns(5)
        for j in range(5):
            checked[i][j] = cols[j].checkbox(board[i][j], key=f"{i}-{j}")

    result = check_bingo(checked)
    if result:
        st.success(result)
    
    # Display the board with checkboxes aligned
    board_df = pd.DataFrame(board)
    st.table(board_df)

if __name__ == "__main__":
    main()
