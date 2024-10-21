import json 



class DisplayAssociateTable():
    def __init__(self):
        pass

    def cadastro_produtos_field():
        dic_associete_produtos = [
            
            {'tipo': 'QLCDNumber', 'nome_widget': 'lcd_id','valor_entrada':'','tabela': 'produtos','campo': 'id','requerido' : False},

            {'tipo': 'QComboBox', 'nome_widget': 'combobox_tipo_prod','valor_entrada':'','tabela': 'produtos','campo': 'tipo_produto','requerido' : False},

            {'tipo': 'QComboBox', 'nome_widget': 'combobox_status_prod','valor_entrada':'','tabela': 'produtos','campo': 'ativo','requerido' : False},
            {'tipo': 'QCheckBox', 'nome_widget': 'checkbox_prod_controlado','valor_entrada':'','tabela': 'produtos','campo': 'controlado','requerido' : False},
            {'tipo': 'QCheckBox', 'nome_widget': 'checkbox_imp_ticket','valor_entrada':'','tabela': 'produtos','campo': 'imp_ticket','requerido' : False},
            {'tipo': 'QCheckBox', 'nome_widget': 'checkbox_prod_risco','valor_entrada':'','tabela': 'produtos','campo': 'risco','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_id_grupo','valor_entrada':'','tabela': 'produtos','campo': 'grupo','requerido':True},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_desc_grupo','valor_entrada':'','tabela': '','campo': '','requerido':True},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_id_subgrupo','valor_entrada':'','tabela': 'produtos','campo': 'sub_grupo','requerido':True},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_desc_subgrupo','valor_entrada':'','tabela': '','campo': '','requerido':True},

            {'tipo': 'QLineEdit', 'nome_widget': 'text_id_categoria','valor_entrada':'','tabela': 'produtos','campo': 'categoria','requerido':False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_desc_categoria','valor_entrada':'','tabela': '','campo': '','requerido':True},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_id_marca','valor_entrada':'','tabela': 'produtos','campo': 'marca','requerido':False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_desc_marca','valor_entrada':'','tabela': '','campo': '','requerido':False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_id_gp_preco','valor_entrada':'','tabela': 'produtos','campo': 'grupo_preco','requerido':False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_desc_gp_preco','valor_entrada':'','tabela': '','campo': '','requerido':False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_unid','valor_entrada':'','tabela': 'produtos','campo': 'unidade','requerido':True},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_cod_fab','valor_entrada':'','tabela': 'produtos','campo': 'codigo_fab','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_qt_unid','valor_entrada':'','tabela': 'produtos','campo': 'qt_unid','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_medida','valor_entrada':'','tabela': 'produtos','campo': 'medida','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_descricao','valor_entrada':'','tabela': 'produtos','campo': 'descricao','requerido':True},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_margem_direta','valor_entrada':'','tabela': 'produto_preco','campo': 'margem_direta','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_markup','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_preco','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_preco_sugerido','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_custo_direto','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_custo_indireto','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_custo_impostos','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_custo_diff','valor_entrada':'','tabela': '','campo': '','requerido' : False},
            {'tipo': 'QLineEdit', 'nome_widget': 'text_nome_red','valor_entrada':'','tabela': 'produtos','campo': 'nome_reduzido','requerido':True},
            
            
        ]
        return dic_associete_produtos

if __name__=='__main__'    :
    e = DisplayAssociateTable.cadastro_produtos_field()
    for i in e: 
        if i.get('tabela','') == '':
            print(i)