from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# -*- coding: utf-8 -*-

class CarCoolGUI(App):
    def build(self):
        # Tela principal
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Bem-vindo ao CarCool!'))
        layout.add_widget(Button(text='Cadastrar Veículo', on_press=self.abrir_tela_cadastro))
        layout.add_widget(Button(text='Visualizar Veículos', on_press=self.abrir_tela_visualizacao))
        return layout

    def abrir_tela_cadastro(self, instance):
        # Lógica para abrir a tela de cadastro de veículo
        self.root.clear_widgets()  # Limpa a tela principal
        layout_cadastro = BoxLayout(orientation='vertical')
        layout_cadastro.add_widget(Label(text='Tela de Cadastro de Veículo'))
        layout_cadastro.add_widget(Button(text='Voltar', on_press=self.voltar_tela_principal))
        self.root.add_widget(layout_cadastro)

    def abrir_tela_visualizacao(self, instance):
        # Lógica para abrir a tela de visualização de veículos
        self.root.clear_widgets()  # Limpa a tela principal
        layout_visualizacao = BoxLayout(orientation='vertical')
        layout_visualizacao.add_widget(Label(text='Tela de Visualização de Veículos'))
        layout_visualizacao.add_widget(Button(text='Voltar', on_press=self.voltar_tela_principal))
        self.root.add_widget(layout_visualizacao)

    def voltar_tela_principal(self, instance):
        # Lógica para voltar à tela principal
        self.root.clear_widgets()  # Limpa a tela atual
        self.root.add_widget(self.build())  # Recria a tela principal

if __name__ == '__main__':
    CarCoolGUI().run()