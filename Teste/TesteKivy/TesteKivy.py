# -*- coding: utf-8 -*-
# import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.clock import Clock


class Veiculo:
    def __init__(self, marca, modelo, ano, placa, valor_compra, media_valores, percentual_desconto):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.final_placa = placa[-1]
        self.valor_compra = valor_compra
        self.media_valores = media_valores
        self.percentual_desconto = percentual_desconto
        self.valor_minimo_venda = media_valores - (media_valores * percentual_desconto / 100)
        self.pecas_compradas = []
        self.pecas_nao_compradas = []

    def to_dict(self):
        return {
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'placa': self.placa,
            'final_placa': self.final_placa,
            'valor_compra': self.valor_compra,
            'media_valores': self.media_valores,
            'percentual_desconto': self.percentual_desconto,
            'valor_minimo_venda': self.valor_minimo_venda,
            'pecas_compradas': self.pecas_compradas,
            'pecas_nao_compradas': self.pecas_nao_compradas
        }

class VeiculoApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.veiculos = []
        self.progress_value = 0
        self.splash_screen = None

    def build(self):
        # Cria a tela de carregamento
        self.splash_screen = BoxLayout(orientation='vertical', spacing=10)
        self.splash_screen.add_widget(Image(source='logo.png'))
        self.splash_screen.add_widget(Label(text='Carregando...', size_hint_y=None, height=30))
        self.splash_screen.add_widget(Image(source='loading_icon.png', size_hint_y=None, height=30))
        return self.splash_screen

    def on_start(self):
        # Simula o carregamento inicial, chamando a função show_main_screen após 2 segundos
        Clock.schedule_once(self.show_main_screen, 2)

    def show_main_screen(self, dt):
        # Alterna para a tela principal após o tempo de simulação da carga inicial
        self.root.clear_widgets()
        self.root = BoxLayout(orientation='vertical', spacing=10)

        # Adiciona a logo
        logo = Image(source='logo.png')
        self.root.add_widget(logo)

        # Adiciona a barra de progresso
        progress_label = Label(text='Carregando...', size_hint_y=None, height=30)
        self.root.add_widget(progress_label)

        progress_bar = Image(source='loading_icon.png', size_hint_y=None, height=30)
        progress_bar.width = self.progress_value * self.root.width
        self.root.add_widget(progress_bar)

        # Adiciona botões após o carregamento completo
        if self.progress_value >= 1:
            cadastrar_button = Button(text='Cadastrar Veículo')
            cadastrar_button.bind(on_press=self.cadastrar_veiculo)
            self.root.add_widget(cadastrar_button)

            visualizar_button = Button(text='Visualizar Veículos')
            visualizar_button.bind(on_press=self.visualizar_veiculos)
            self.root.add_widget(visualizar_button)

            # Adiciona informações do veículo
            veiculo_info = f"Veículo - {self.veiculos[0].marca} {self.veiculos[0].modelo} ({self.veiculos[0].ano})"
            veiculo_label = Label(text=veiculo_info)
            self.root.add_widget(veiculo_label)

        self.splash_screen.clear_widgets()

    def cadastrar_veiculo(self, instance):
        marca_input = TextInput(hint_text='Marca do veículo')
        modelo_input = TextInput(hint_text='Modelo do veículo')
        ano_input = TextInput(hint_text='Ano do veículo')
        placa_input = TextInput(hint_text='Placa do veículo')
        valor_compra_input = TextInput(hint_text='Valor de compra do veículo')
        media_valores_input = TextInput(hint_text='Média de valores do veículo')
        percentual_desconto_input = TextInput(hint_text='Percentual de desconto')

        salvar_button = Button(text='Salvar Veículo')
        salvar_button.bind(
            on_press=lambda x: self.salvar_veiculo(
                marca_input.text, modelo_input.text, ano_input.text, placa_input.text,
                float(valor_compra_input.text), float(media_valores_input.text), float(percentual_desconto_input.text)
            )
        )

        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(marca_input)
        layout.add_widget(modelo_input)
        layout.add_widget(ano_input)
        layout.add_widget(placa_input)
        layout.add_widget(valor_compra_input)
        layout.add_widget(media_valores_input)
        layout.add_widget(percentual_desconto_input)
        layout.add_widget(salvar_button)

        self.root.clear_widgets()
        self.root.add_widget(layout)

    def salvar_veiculo(self, marca, modelo, ano, placa, valor_compra, media_valores, percentual_desconto):
        veiculo = Veiculo(marca, modelo, ano, placa, valor_compra, media_valores, percentual_desconto)
        self.veiculos.append(veiculo)

        # Adicione aqui a lógica para salvar os dados no arquivo se desejar

        self.root.clear_widgets()
        self.build()

    def visualizar_veiculos(self, instance):
        layout = BoxLayout(orientation='vertical', spacing=10)

        for veiculo in self.veiculos:
            label = Label(text=f"Veículo - {veiculo.marca} {veiculo.modelo} ({veiculo.ano})")
            layout.add_widget(label)

        self.root.clear_widgets()
        self.root.add_widget(layout)


if __name__ == '__main__':
    VeiculoApp().run()
