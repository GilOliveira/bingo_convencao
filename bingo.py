
import streamlit as st
import random
import pandas as pd

def generate_bingo_board(words, seed):
    random.seed(seed)
    random.shuffle(words)
    return [words[i * 5:(i + 1) * 5] for i in range(5)]

def check_bingo(checked):
    # Check for Bingo
    if all(all(row) for row in checked):
        return "BINGO!"
    # Check rows
    for row in range(5):
        if all(checked[row]):
            return "Linha!"
    # Check columns
    for col in range(5):
        if all(checked[row][col] for row in range(5)):
            return "Linha!"
    return ""

def main():
    st.image('./bingo_pic.png')

    words = ["Inerências", "Verdadeiramente liberal", "Burocracia", "Isso é socialista!",
             "Comité central", "Transparência", "Eu não sou jurista, mas...",
             "Delegados", "Separação de poderes", "José Cardoso", "Encostem-me à parede!",
             "Malas", "Distritais", "Empoderar o Membro", "Microfone dá feedback",
             "'Jota' da IL", "Portal do Membro", "Órgão Máximo", "Assinaturas", "Freguesias",
             "O partido é como uma empresa", "O partido é como o estado", "Carlos Moedas",
             "Salários", "Nepotismo", "Realmente liberal", "Elon Musk", "Fechem as portas!"
             "Quórum", "Tem de terminar...", "Motoserra", "AFUERA!", "15%", "Unir o partido",
             "Observador", "Alguém no zoom não aparece", "Wokismo", "Aplauso do aviso para almoço/jantar"
             "Leva a bebida para o púlpito", "Pin arco íris", "Introduzir o membro", 
             "Estou no partido há pouco tempo", "O partido mudou!", "Liberal em toda a linha",
             "Apupos", "Eu não ia falar, mas...", "Problemas de som", "Está tudo a pensar no almoço/jantar",
             "Melancia azul", "Liberalómetro", "WOKE", "Estou mesmo a terminar...", "BOM DIA LIBERAIS",
              "3 minutos não chega...", "Camaradas...", "Unidos AO Liberalismo", "Tantas listas!",
              "Não sou candidato/a...", "Javier Milei", "Assino por baixo", "Autonomia dos núcleos"]

    seed = st.number_input("Insere o teu número de membro:", min_value=1, max_value=10000, value=1)
    
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
    

if __name__ == "__main__":
    main()
