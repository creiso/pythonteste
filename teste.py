from PyQt5 import  uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    if formulario.radioButton.isChecked() :
        print("Categoria Outros selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Bebidas selecionada")
    else :
        print("Categoria Alimentos selecionada")

    print("Nome:",linha1)
    print("Codigo:",linha2)
    print("Preço",linha3)
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
