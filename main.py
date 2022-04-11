from src.editor.editor import Editor

from PyQt5.QtWidgets import QApplication

import sys

APP = QApplication([])
editor = Editor()

APP.setStyle("Fusion")
sys.exit(APP.exec_())