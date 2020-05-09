from GUI import *

def run():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form(Form)
        sys.exit(app.exec_())
if __name__=='__main__':
    run()