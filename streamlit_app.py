import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


g = 9.81 # gravidade [m/s^2]


st.title("UFRGS Portas Abertas")
st.title("A Matemática e o Lançamento de Foguetes")



st.header("Lançamento vertical") 

st.write("Entre os 3 tempos abaixo (segundos)")

TempoVertical_1 = st.number_input("1o lançamento",
                                  min_value=0.,
                                  step = 0.01,
                                  format = "%.2f",
                                  label_visibility="visible"
                                  )
TempoVertical_2 = st.number_input("2o lançamento",
                                  min_value=0.,
                                  step = 0.01,
                                  format = "%.2f",
                                  label_visibility="visible"
                                  )
TempoVertical_3 = st.number_input("3o lançamento",
                                  min_value=0.,
                                  step = 0.01,
                                  format = "%.2f",
                                  label_visibility="visible"
                                  )

TempoMédioVertical = ( TempoVertical_1 + TempoVertical_2 + TempoVertical_3 ) / 3

MaiorTempoVertical = max( TempoVertical_1 , TempoVertical_2 , TempoVertical_3 )

AlturaMaximaVertical = g*MaiorTempoVertical**2/8

Velocidade = g*MaiorTempoVertical/2
Vel_kmh = Velocidade*3.6

if st.button("Calcular"):
    st.write("Maior tempo:            %.2f s"%MaiorTempoVertical)
    st.write("Altura máxima atingida: %.2f m"%AlturaMaximaVertical)
    st.write("Velocidade inicial: %.2f m/s = %.2f km/h"%(Velocidade,Vel_kmh))




# DESENVOLVIDO POR: MARCELO SCHRAMM E CIBELE LADEIA
st.divider()
st.caption("Desenvolvido por Marcelo Schramm e Cibele Aparecida Ladeia")

