# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
        self.menubar.setObjectName("menubar")
        self.menuSistema = QtWidgets.QMenu(self.menubar)
        self.menuSistema.setObjectName("menuSistema")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuProdutos_Itens = QtWidgets.QMenu(self.menuCadastro)
        self.menuProdutos_Itens.setObjectName("menuProdutos_Itens")
        self.menuAuxiliares = QtWidgets.QMenu(self.menuCadastro)
        self.menuAuxiliares.setObjectName("menuAuxiliares")
        self.menuDespesa = QtWidgets.QMenu(self.menubar)
        self.menuDespesa.setObjectName("menuDespesa")
        self.menuLan_amento = QtWidgets.QMenu(self.menuDespesa)
        self.menuLan_amento.setObjectName("menuLan_amento")
        self.menuConfiguracoes = QtWidgets.QMenu(self.menubar)
        self.menuConfiguracoes.setObjectName("menuConfiguracoes")
        self.menuRelatorios = QtWidgets.QMenu(self.menubar)
        self.menuRelatorios.setObjectName("menuRelatorios")
        self.menuReceitas = QtWidgets.QMenu(self.menubar)
        self.menuReceitas.setObjectName("menuReceitas")
        self.menuLan_amentos = QtWidgets.QMenu(self.menuReceitas)
        self.menuLan_amentos.setObjectName("menuLan_amentos")
        self.menuInvestimento = QtWidgets.QMenu(self.menubar)
        self.menuInvestimento.setObjectName("menuInvestimento")
        self.menuEstoque = QtWidgets.QMenu(self.menubar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuLan_amento_2 = QtWidgets.QMenu(self.menuEstoque)
        self.menuLan_amento_2.setObjectName("menuLan_amento_2")
        self.menuFinanceiro = QtWidgets.QMenu(self.menubar)
        self.menuFinanceiro.setObjectName("menuFinanceiro")
        MainWindow.setMenuBar(self.menubar)
        self.actionReceitas = QtWidgets.QAction(MainWindow)
        self.actionReceitas.setObjectName("actionReceitas")
        self.actionInvestimentos = QtWidgets.QAction(MainWindow)
        self.actionInvestimentos.setObjectName("actionInvestimentos")
        self.actionDespesa_Fixas = QtWidgets.QAction(MainWindow)
        self.actionDespesa_Fixas.setObjectName("actionDespesa_Fixas")
        self.actionDespesa_Correntes = QtWidgets.QAction(MainWindow)
        self.actionDespesa_Correntes.setObjectName("actionDespesa_Correntes")
        self.actionDespesas_Avulsas = QtWidgets.QAction(MainWindow)
        self.actionDespesas_Avulsas.setObjectName("actionDespesas_Avulsas")
        self.actionMovimenta_o = QtWidgets.QAction(MainWindow)
        self.actionMovimenta_o.setObjectName("actionMovimenta_o")
        self.actionRelat_rios = QtWidgets.QAction(MainWindow)
        self.actionRelat_rios.setObjectName("actionRelat_rios")
        self.actionDespesa_Fixas_2 = QtWidgets.QAction(MainWindow)
        self.actionDespesa_Fixas_2.setObjectName("actionDespesa_Fixas_2")
        self.actionDespesa_Corrente = QtWidgets.QAction(MainWindow)
        self.actionDespesa_Corrente.setObjectName("actionDespesa_Corrente")
        self.actionMovimenta_es = QtWidgets.QAction(MainWindow)
        self.actionMovimenta_es.setObjectName("actionMovimenta_es")
        self.actionReceitas_Fixas = QtWidgets.QAction(MainWindow)
        self.actionReceitas_Fixas.setObjectName("actionReceitas_Fixas")
        self.actionReceitas_Correntes = QtWidgets.QAction(MainWindow)
        self.actionReceitas_Correntes.setObjectName("actionReceitas_Correntes")
        self.actionRelat_rios_2 = QtWidgets.QAction(MainWindow)
        self.actionRelat_rios_2.setObjectName("actionRelat_rios_2")
        self.actionLan_amento_2 = QtWidgets.QAction(MainWindow)
        self.actionLan_amento_2.setObjectName("actionLan_amento_2")
        self.actionMovimenta_es_2 = QtWidgets.QAction(MainWindow)
        self.actionMovimenta_es_2.setObjectName("actionMovimenta_es_2")
        self.actionRelat_rios_3 = QtWidgets.QAction(MainWindow)
        self.actionRelat_rios_3.setObjectName("actionRelat_rios_3")
        self.actionMovimenta_es_3 = QtWidgets.QAction(MainWindow)
        self.actionMovimenta_es_3.setObjectName("actionMovimenta_es_3")
        self.actionRelat_rios_4 = QtWidgets.QAction(MainWindow)
        self.actionRelat_rios_4.setObjectName("actionRelat_rios_4")
        self.actionInvent_rio = QtWidgets.QAction(MainWindow)
        self.actionInvent_rio.setObjectName("actionInvent_rio")
        self.actionAdd_item = QtWidgets.QAction(MainWindow)
        self.actionAdd_item.setObjectName("actionAdd_item")
        self.actionBaixa_de_Estoque = QtWidgets.QAction(MainWindow)
        self.actionBaixa_de_Estoque.setObjectName("actionBaixa_de_Estoque")
        self.actionBancos = QtWidgets.QAction(MainWindow)
        self.actionBancos.setObjectName("actionBancos")
        self.actionOrigens = QtWidgets.QAction(MainWindow)
        self.actionOrigens.setObjectName("actionOrigens")
        self.actionProdutos_itens = QtWidgets.QAction(MainWindow)
        self.actionProdutos_itens.setObjectName("actionProdutos_itens")
        self.actionCategoria = QtWidgets.QAction(MainWindow)
        self.actionCategoria.setObjectName("actionCategoria")
        self.actionCategoria_2 = QtWidgets.QAction(MainWindow)
        self.actionCategoria_2.setObjectName("actionCategoria_2")
        self.actionClasse = QtWidgets.QAction(MainWindow)
        self.actionClasse.setObjectName("actionClasse")
        self.actionEmpresa = QtWidgets.QAction(MainWindow)
        self.actionEmpresa.setObjectName("actionEmpresa")
        self.actionUsu_rios = QtWidgets.QAction(MainWindow)
        self.actionUsu_rios.setObjectName("actionUsu_rios")
        self.menuSistema.addAction(self.actionEmpresa)
        self.menuProdutos_Itens.addAction(self.actionProdutos_itens)
        self.menuProdutos_Itens.addAction(self.actionCategoria_2)
        self.menuProdutos_Itens.addAction(self.actionClasse)
        self.menuAuxiliares.addAction(self.actionBancos)
        self.menuAuxiliares.addAction(self.actionOrigens)
        self.menuCadastro.addAction(self.menuProdutos_Itens.menuAction())
        self.menuCadastro.addAction(self.actionUsu_rios)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.menuAuxiliares.menuAction())
        self.menuLan_amento.addAction(self.actionDespesa_Fixas_2)
        self.menuLan_amento.addAction(self.actionDespesa_Corrente)
        self.menuDespesa.addAction(self.menuLan_amento.menuAction())
        self.menuDespesa.addAction(self.actionMovimenta_o)
        self.menuDespesa.addSeparator()
        self.menuDespesa.addAction(self.actionRelat_rios)
        self.menuLan_amentos.addAction(self.actionReceitas_Fixas)
        self.menuLan_amentos.addAction(self.actionReceitas_Correntes)
        self.menuReceitas.addAction(self.menuLan_amentos.menuAction())
        self.menuReceitas.addAction(self.actionMovimenta_es)
        self.menuReceitas.addSeparator()
        self.menuReceitas.addAction(self.actionRelat_rios_2)
        self.menuInvestimento.addAction(self.actionLan_amento_2)
        self.menuInvestimento.addAction(self.actionMovimenta_es_2)
        self.menuInvestimento.addSeparator()
        self.menuInvestimento.addAction(self.actionRelat_rios_3)
        self.menuLan_amento_2.addAction(self.actionAdd_item)
        self.menuLan_amento_2.addAction(self.actionBaixa_de_Estoque)
        self.menuEstoque.addAction(self.menuLan_amento_2.menuAction())
        self.menuEstoque.addAction(self.actionMovimenta_es_3)
        self.menuEstoque.addAction(self.actionInvent_rio)
        self.menuEstoque.addSeparator()
        self.menuEstoque.addAction(self.actionRelat_rios_4)
        self.menubar.addAction(self.menuSistema.menuAction())
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuDespesa.menuAction())
        self.menubar.addAction(self.menuReceitas.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menubar.addAction(self.menuInvestimento.menuAction())
        self.menubar.addAction(self.menuEstoque.menuAction())
        self.menubar.addAction(self.menuRelatorios.menuAction())
        self.menubar.addAction(self.menuConfiguracoes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSistema.setTitle(_translate("MainWindow", "Sistema"))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro"))
        self.menuProdutos_Itens.setTitle(_translate("MainWindow", "Produtos/Itens"))
        self.menuAuxiliares.setTitle(_translate("MainWindow", "Auxiliares"))
        self.menuDespesa.setTitle(_translate("MainWindow", "Despesas"))
        self.menuLan_amento.setTitle(_translate("MainWindow", "Lançamento"))
        self.menuConfiguracoes.setTitle(_translate("MainWindow", "Configurações"))
        self.menuRelatorios.setTitle(_translate("MainWindow", "Relatórios"))
        self.menuReceitas.setTitle(_translate("MainWindow", "Receitas"))
        self.menuLan_amentos.setTitle(_translate("MainWindow", "Lançamentos"))
        self.menuInvestimento.setTitle(_translate("MainWindow", "Investimento"))
        self.menuEstoque.setTitle(_translate("MainWindow", "Estoque"))
        self.menuLan_amento_2.setTitle(_translate("MainWindow", "Lançamento"))
        self.menuFinanceiro.setTitle(_translate("MainWindow", "Financeiro"))
        self.actionReceitas.setText(_translate("MainWindow", "Receitas"))
        self.actionInvestimentos.setText(_translate("MainWindow", "Investimentos"))
        self.actionDespesa_Fixas.setText(_translate("MainWindow", "Despesa Fixas"))
        self.actionDespesa_Correntes.setText(_translate("MainWindow", "Despesa Correntes"))
        self.actionDespesas_Avulsas.setText(_translate("MainWindow", "Despesas Avulsas"))
        self.actionMovimenta_o.setText(_translate("MainWindow", "Movimentação"))
        self.actionRelat_rios.setText(_translate("MainWindow", "Relatórios"))
        self.actionDespesa_Fixas_2.setText(_translate("MainWindow", "Despesa Fixa"))
        self.actionDespesa_Corrente.setText(_translate("MainWindow", "Despesa Corrente"))
        self.actionMovimenta_es.setText(_translate("MainWindow", "Movimentações"))
        self.actionReceitas_Fixas.setText(_translate("MainWindow", "Receitas Fixas"))
        self.actionReceitas_Correntes.setText(_translate("MainWindow", "Receitas Correntes"))
        self.actionRelat_rios_2.setText(_translate("MainWindow", "Relatórios"))
        self.actionLan_amento_2.setText(_translate("MainWindow", "Lançamento"))
        self.actionMovimenta_es_2.setText(_translate("MainWindow", "Movimentações"))
        self.actionRelat_rios_3.setText(_translate("MainWindow", "Relatórios"))
        self.actionMovimenta_es_3.setText(_translate("MainWindow", "Movimentações"))
        self.actionRelat_rios_4.setText(_translate("MainWindow", "Relatórios"))
        self.actionInvent_rio.setText(_translate("MainWindow", "Inventário"))
        self.actionAdd_item.setText(_translate("MainWindow", "Add item "))
        self.actionBaixa_de_Estoque.setText(_translate("MainWindow", "Baixa de Estoque"))
        self.actionBancos.setText(_translate("MainWindow", "Bancos"))
        self.actionOrigens.setText(_translate("MainWindow", "Origens"))
        self.actionProdutos_itens.setText(_translate("MainWindow", "Produtos/itens"))
        self.actionCategoria.setText(_translate("MainWindow", "Categoria"))
        self.actionCategoria_2.setText(_translate("MainWindow", "Categoria"))
        self.actionClasse.setText(_translate("MainWindow", "Classe "))
        self.actionEmpresa.setText(_translate("MainWindow", "Empresa"))
        self.actionUsu_rios.setText(_translate("MainWindow", "Usuários"))