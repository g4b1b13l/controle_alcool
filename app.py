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
import base64
import dash_bootstrap_components as dbc

now = datetime.now()


ufpb_image = base64.b64encode(open('logo_ufpb.jpeg', 'rb').read())
cear_image = base64.b64encode(open('logo_ufpb.jpeg', 'rb').read())

external_stylesheets = ['https://codepen.io/g4b1b13l/pen/VwwrYdL.css'] # Esse eh um site externo meu com um monte classe do css pronta,
																		# Copiei quase tudo do original que é um de chris num sei q la
																		#Criei um no meu nome so caso ele decida excluir ou algo do tipo eu n perder 

app = dash.Dash(__name__, external_stylesheets=[external_stylesheets,'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'],
        meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
server = app.server


app.title = 'Controle_Alcool'

card_content = [
    dbc.CardHeader("SALDO INICIAL EM LITROS"),

    dbc.CardBody(
        [
            html.H3("31460", className="card-title",style={'textAlign':'center'}),

        ]
    ),
]

card_content_2 = [
    dbc.CardHeader("SALDO DISPONÍVEL EM LITROS"),
    
    dbc.CardBody(
        [
            html.H3(children = '', id= 'ultiminha', className="card-title",style={'textAlign':'center'}),

        ]
    ),
]


row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_2, color="success", outline=True)),
    ],
    className="mb-4",
),

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


                html.Img(id='img_logo_ufpb',height='auto'
                        ,src='data:image/png;base64,{}'.format(ufpb_image.decode())
                        ,style={'display': 'block','height':'70px','position':'absolute','left':'50px','top':'10px'
                        }),

		 html.Div(id='div_topo',children=[


		 				html.Div([
                       html.H3('Doação ao Governo do Estado da Paraíba do Volume de 31.460 litros'),
                       html.H3(	'solicitados pela Secretaria do Estado da Paraíba para combate ao Covid-19'),
                       	]),

		 			html.Div([html.Img(id='img_logo_cear'
                        ,src='data:image/png;base64,{}'.format(cear_image.decode())
                        ,style={'display': 'block','height':'70px','position':'absolute','right':'50px','top':'10px'
                      }),],className='one columns'),
            ],
                
            style={'textAlign':'center'
                  ,'border': '2px solid lightgray'
                  ,'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
                  ,'background-color':'#fffffff'}
                 
            



            ),


              		

		#dbc.Checklist(
        #    options=[
        #        {"label": "Distribuído", "value": 1},
        #    ],
        #    value=[],
        #    id="switches-input",
        #    switch=True,
        #),

	html.Div(

        [html.H3(children= 'Saldo disponível por SAFRA'),

       
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

	html.Div(row_1),
	html.Div(

        [html.H3(children= 'Saldo utilizado por SAFRA'),

       
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
    dcc.Graph(id = 'quantidade_saida'),
   html.Div(children=[

                        html.P('AS INFORMAÇÕES ANEXAS SÃO RETIRADAS DOS RECIBOS DO SAPCANA ENVIADOS AO MAPA. P/ EMPRESAS ASSOCIADAS'),
                        html.P('Elaboração: Sindalcool | Posição até 29/02/2020')
                    ],style={'textAlign': 'center'
                             ,'border': '2px solid lightgray'
                             ,'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
                             ,'background-color':'#eefefe'
                             , 'margin-top' : '30px'}),

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



@app.callback(Output('ultiminha', 'children'),
				[dash.dependencies.Input('check', 'value')])



def upando_grafico_1(check):  

	mydb=psy.connect (
		host='ec2-54-235-100-99.compute-1.amazonaws.com',
		user = 'mhxcrjdnckxtbr',
		password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
		database='d9k1k422mp16r5')
	mycursor=mydb.cursor()
	total_disponivel= 0
	mycursor.execute('''select * from public."GIASA" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]
	df = pd.DataFrame(data=myresult, columns=colnames )
	ultimo_registro  = df.tail(1)
	total_liq = ultimo_registro['total_liq'].sum()
	total_disponivel = total_liq
	mycursor.execute('''select * from public."JAPUNGU" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]
	df = pd.DataFrame(data=myresult, columns=colnames )
	ultimo_registro  = df.tail(1)
	total_liq = ultimo_registro['total_liq'].sum()
	total_disponivel = total_liq + total_disponivel
	mycursor.execute('''select * from public."MIRIRI" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]
	df = pd.DataFrame(data=myresult, columns=colnames )
	ultimo_registro  = df.tail(1)
	total_liq = ultimo_registro['total_liq'].sum()
	total_disponivel = total_liq + total_disponivel

	mycursor.execute('''select * from public."M_ALEGRE" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]
	df = pd.DataFrame(data=myresult, columns=colnames )
	ultimo_registro  = df.tail(1)
	total_liq = ultimo_registro['total_liq'].sum()
	total_disponivel = total_liq + total_disponivel
	mycursor.execute('''select * from public."TABU" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]
	df = pd.DataFrame(data=myresult, columns=colnames )
	ultimo_registro  = df.tail(1)
	total_liq = ultimo_registro['total_liq'].sum() 
	total_disponivel = total_liq + total_disponivel
	mycursor.execute('''select * from public."D_PADUA" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]
	df = pd.DataFrame(data=myresult, columns=colnames )
	ultimo_registro  = df.tail(1)
	total_liq = ultimo_registro['total_liq'].sum()
	total_disponivel = total_liq + total_disponivel + 0.01
	total_disponivel = str(total_disponivel)
	return total_disponivel

    #fig = Figure(data=data, layout=layout)



	return go.Figure(fig)

if(__name__ == '__main__'):
    app.run_server(debug=True,port=3012) 
