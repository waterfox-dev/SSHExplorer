from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ..utils.load_theme import load_theme

import sys

class Editor(QMainWindow) :
    
    def __init__(self, *args, **kwargs) :
        
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle("SSHExplorer")
        self.setStyleSheet(load_theme('editorWhite'))
        self.theme ='white'
        
        self.load_menubar()
        
        self.showMaximized()
        
    def load_menubar(self) :
        
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        
        switchThemeAction = QAction('&Switch Theme', self)
        switchThemeAction.setShortcut('Ctrl+alt+s')
        switchThemeAction.setStatusTip('Switch Color Theme')
        switchThemeAction.triggered.connect(self.changeThemeStyle)
        
        self.statusBar()
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exitAction)
        file_menu.addAction(switchThemeAction)
        
    def changeThemeStyle(self) :
        if self.theme == 'white' :
            self.setStyleSheet(load_theme('editorDark'))
            self.theme = 'dark'
        elif self.theme == 'dark' :
            self.setStyleSheet(load_theme('editorWhite'))
            self.theme = 'white'