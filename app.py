import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
from dash.dependencies import Input, Output
import plotly.offline as py
from plotly.graph_objs import *
import plotly.graph_objs as go 
import psycopg2 as psy
import os
import glob
import pandas as pd
import numpy as np
from datetime import datetime
now = datetime.now()


external_stylesheets = ['https://codepen.io/g4b1b13l/pen/VwwrYdL.css'] # Esse eh um site externo meu com um monte classe do css pronta,
																		# Copiei quase tudo do original que é um de chris num sei q la
																		#Criei um no meu nome so caso ele decida excluir ou algo do tipo eu n perder 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
        meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
server = app.server

app.title = 'Controle_Alcool'

usinas = ['GIASA', 'JAPUNGU', 'MIRIRI', 'M_ALEGRE', 'TABU', 'D_PADUA']



mydb=psy.connect (
host='ec2-54-235-100-99.compute-1.amazonaws.com',
user = 'mhxcrjdnckxtbr',
password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
database='d9k1k422mp16r5')

mycursor=mydb.cursor()
#dict_usinas = {#
#	'GIASA' :  mycursor.execute('''select * from public."GIASA" '''),
#	'JAPUNGU' :  mycursor.execute('''select * from public."JAPUNGU" '''),
#	'MIRIRI' : mycursor.execute('''select * from public."MIRIRI" '''),
#	'M_ALEGRE' : mycursor.execute('''select * from public."M_ALEGRE" '''),
#	'TABU' : mycursor.execute('''select * from public."TABU" '''),
#	'D_PADUA' : mycursor.execute('''select * from public."D_PADUA" '''),
#}

def usinas_2(usina):
    if usina == 'GIASA':
        return mycursor.execute('''select * from public."GIASA" ''')
    if usina == 'JAPUNGU':
        return mycursor.execute('''select * from public."JAPUNGU" ''')
    if usina == 'MIRIRI':
        return mycursor.execute('''select * from public."MIRIRI" ''')
    if usina == 'M_ALEGRE':
        return mycursor.execute('''select * from public."M_ALEGRE" ''')
    if usina == 'TABU':
        return mycursor.execute('''select * from public."TABU" ''')
    if usina == 'D_PADUA':
        return mycursor.execute('''select * from public."D_PADUA" ''')

app.layout = html.Div([  #Aqui a gente vai upar nosso layout 
						# Podemos criar quantas Div forem necessárias para nosso projeto
						#nesse caso vou criar apenas uma dropdown para teste e um grafico para mostrar

	dcc.Checklist(
    id='check',
    options=[   
    {'label': '', 'value': 'ativado'},


    ],
    value=['d'],
    labelStyle={'display': 'none','margin-top': '30px'}
    ),


	html.Div(

        [html.H1(children= 'Controle Álcool em gel'),

       
        ]
              , 

         style={
        'font-size': '5pt',
        #'height': '75px',
        'margin': '-10px -10px -10px',
        'background-color': '#ADD8E6',
        'text-align': 'center',
        #'border-radius': '2px',
        #'display': 'flex',
        #'margin-left': '0',

        } 

        ),  

	html.Div(

        [html.H3(children= 'Gráfico quantidade líquida'),

       
        ]
              , 

         style={
        'font-size': '5pt',
        #'height': '75px',
        'margin': '-10px -10px -10px',
        #'background-color': '#00BB2D',
        'text-align': 'center',
        #'border-radius': '2px',
        #'display': 'flex',
        #'margin-left': '0',
        'padding-top' : '60px'
        } 

        ), 
	#html.H1('Gráfico quantidade liquida'), #Aqui vai ficar o nome em cima da dropdown que eu quero
	dcc.Graph(id = 'quantidade_liquida'),  # Do mesmo jeito que criamos a dropdown, criamos um grafico
    
	html.Div(

        [html.H3(children= 'Gráfico evasão álcool em gel'),

       
        ]
              , 

         style={
        'font-size': '5pt',
        #'height': '75px',
        'margin': '-10px -10px -10px',
        #'background-color': '#00BB2D',
        'text-align': 'center',
        #'border-radius': '2px',
        #'display': 'flex',
        #'margin-left': '0',
        'padding-top' : '60px'
        } 

        ),  									# Aqui identamos como feature-graphic, futuramente utilizaremos
    #html.H1('Gráfico quantidade liquida'),
    dcc.Graph(id = 'quantidade_saida') 

],  style={'width': '100%',
            'display': 'inline-block'})

@app.callback(Output('quantidade_liquida', 'figure'),
				[dash.dependencies.Input('check', 'value')])



def upando_grafico_1(check):  
	def usinas_2(usina):
	    if usina == 'GIASA':
	        return mycursor.execute('''select * from public."GIASA" ''')
	    if usina == 'JAPUNGU':
	        return mycursor.execute('''select * from public."JAPUNGU" ''')
	    if usina == 'MIRIRI':
	        return mycursor.execute('''select * from public."MIRIRI" ''')
	    if usina == 'M_ALEGRE':
	        return mycursor.execute('''select * from public."M_ALEGRE" ''')
	    if usina == 'TABU':
	        return mycursor.execute('''select * from public."TABU" ''')
	    if usina == 'D_PADUA':
	        return mycursor.execute('''select * from public."D_PADUA" ''')
	fig=go.Figure()
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()

	usinas = ['GIASA', 'JAPUNGU', 'MIRIRI', 'M_ALEGRE', 'TABU', 'D_PADUA']

	for usina in usinas:

		usinas_2(usina)

		myresult= mycursor.fetchall()
		colnames = [desc[0] for desc in mycursor.description]
		df = pd.DataFrame(data=myresult, columns=colnames )
		ultimo_registro  = df.tail(1)
		total_liq = ultimo_registro['total_liq']
		fig.add_trace((go.Bar(
		       hoverinfo='y',
		            y=[x for x in total_liq],
		            name = usina,
		            visible=True,

		        opacity = 0.8)))


	fig.update_layout(bargap=0.2, 
            bargroupgap=0.1 
            ) 
	fig.update_layout(
 
        yaxis={'title': 'Quantidade em litros'},)






    #fig = Figure(data=data, layout=layout)



	return go.Figure(fig)



@app.callback(Output('quantidade_saida', 'figure'),
				[dash.dependencies.Input('check', 'value')])



def upando_grafico_1(check):  
	def usinas_2(usina):
	    if usina == 'GIASA':
	        return mycursor.execute('''select * from public."GIASA" ''')
	    if usina == 'JAPUNGU':
	        return mycursor.execute('''select * from public."JAPUNGU" ''')
	    if usina == 'MIRIRI':
	        return mycursor.execute('''select * from public."MIRIRI" ''')
	    if usina == 'M_ALEGRE':
	        return mycursor.execute('''select * from public."M_ALEGRE" ''')
	    if usina == 'TABU':
	        return mycursor.execute('''select * from public."TABU" ''')
	    if usina == 'D_PADUA':
	        return mycursor.execute('''select * from public."D_PADUA" ''')
	fig=go.Figure()
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()

	usinas = ['GIASA', 'JAPUNGU', 'MIRIRI', 'M_ALEGRE', 'TABU', 'D_PADUA']

	for usina in usinas:

		usinas_2(usina)

		myresult= mycursor.fetchall()
		colnames = [desc[0] for desc in mycursor.description]
		df = pd.DataFrame(data=myresult, columns=colnames )
		total_liq = df['quantidade_saida'].sum()

		if total_liq == 0:
			total_liq = None

		fig.add_trace((go.Bar(
		       hoverinfo='y',
		            y=[total_liq],
		            name = usina,
		            visible=True,

		        opacity = 0.8)))


		fig.update_layout(bargap=0.2, 
            bargroupgap=0.1 
            ) 
		fig.update_layout(
 
        yaxis={'title': 'Quantidade em litros'},)





    #fig = Figure(data=data, layout=layout)



	return go.Figure(fig)

if(__name__ == '__main__'):
    app.run_server(debug=True,port=3012) 
