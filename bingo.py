
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
             "O partido é como...", "Carlos Moedas", "Salários", "Nepotismo", "Realmente liberal", "Elon Musk", "Fechem as portas!",
             "Quórum", "Tens de terminar...", "Motoserra", "AFUERA!", "15%", "Unir o partido",
             "Observador", "Alguém no zoom não aparece", "Wokismo", "Aplauso do aviso para almoço/jantar",
             "Leva a bebida para o púlpito", "Pin arco íris", "Introduzir o membro", 
             "Estou no partido há pouco tempo", "O partido mudou!", "Liberal em toda a linha",
             "Apupos", "Eu não ia falar, mas...", "Problemas de som", "Está tudo a pensar no almoço/jantar",
             "Melancia azul", "Liberalómetro", "WOKE", "Estou mesmo a terminar... (não termina)", "BOM DIA LIBERAIS",
              "3 minutos não chega...", "Camaradas...", "Unidos AO Liberalismo", "Tantas listas!",
              "Não sou candidato/a...", "Javier Milei", "Assino por baixo", "Autonomia dos núcleos",
             "Menciona o Bingo Liberal", "Oh Rui (qualquer um deles)", "Melância azul/Bloco de direita",
            "Pelo seu mérito", "Membros de base", "Faz um L em vez de um I", "Subsidiariedade",
            "Falta de união", "O partido está estagnado", "Analogia que ninguém percebe", "Tenho pouco tempo",
            "Micro a 1 km da cara", "Agregador", "Eu nem era para a intervir", "Viva a liberdade, carago",
            "Nepotismo", "Asua não ter lido a MEG", "Também não concordo com tudo", "Referência soviética/marxista",
            "País está a ver-nos", "Boca da Natacha Santos", "O ÍLE", "Viva Portugal, Viva a IL",
            "Nós somos diferentes", "Já se faz tarde", "Generaliza o eleitorado", "Diferentes sensibilidades/formas de pensar/alas",
            'Eu não gosto do termo "alas"', "Seguidismo", "Liberais clássicos", "Temos que perceber oq ue é o CN", "Aportar",
            "O Iniciativa Liberal", "Liberais expulsos", "Carla Castro", "GTE", "Tem medo de aparecer no RAP", "Pujante",
            "Feedback do microfone rebenta tímpanos", "Bronca sobre candidatos às presidenciais", "Analogia futebolística",
            "PORTUGAL A CRESCER", "Não te estamos a ouvir", "Cartazes das Europeias", "Não querem debater",
            "Tiques socialistas", "Foge à ordem de trabalhos", "Ímpeto reformista", "Paz e amizade", "DeepSeek/ChatGPT"]

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
