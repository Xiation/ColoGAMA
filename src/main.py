from PySide2 import QtWidgets

from Ui.ui_mainWindow import Ui_MainWindow

from src.camera import run_camera

from PySide2.QtCore import QThread, Signal, Slot

# from ..Ui.ui_mainWindow import Ui_MainWindow
'''
The .. in the import statement above means "one level up" from the current package (src). 
Thus, ..ui refers to the ui package in the parent directory of src.
'''

# Since ui and src are both at the top level under ColoGama, we can use an absolute import.

'''
class CameraThread(QThread):
    finished = Signal()

    def run(self):
        run_camera()
        self.finished.emit()
'''
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # load the UI design
        self.ui = Ui_MainWindow()
        # load function to give access to main window and widget
        self.ui.setupUi(self)

        self.ui.exitBtn.clicked.connect(self.exit_app)
        self.ui.runCamera.clicked.connect(self.start_camera)
    
    def start_camera(self):
        run_camera()

    def exit_app(self):
        exit()   
'''
    def start_camera(self):
        self.thread = CameraThread()
        self.thread.finished.connect(self.on_camera_finished)
        self.thread.start()
'''
'''
    def on_camera_finished(self):
        print('camera thread finished')
'''

    

if __name__== '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()