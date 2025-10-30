from sys import argv as sysargv, exit as sysexit
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication
from core.Win import MainWin


if __name__ == '__main__':

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 高分屏ui显示问题
    app = QApplication(sysargv)
    myshow = MainWin()
    myshow.show()
    sysexit(app.exec_())


"""
Required Third-Party Libraries:

pyqt5
pyqtgraph
numpy
openpyxl
nuitka


Update Log:
V1.0 – 2023.09.07
Development environment: Python 3.11.2 + PyQt5 5.15.9
V2.0 – 2023.09.12

Added reversal of displacement sequence; manual point selection and deletion when identifying reverse points
Added calculation of skeleton curve, stiffness degradation, and strength degradation curves
Added export of results to “Data Summary.xlsx”

V3.0 – 2024.05.15

Optimized UI logic
New feature: Divide hysteresis loops by reverse points on the hysteresis curve
Fixed bug: Strength degradation curve had identical x and y axes in output
Added type annotations and documentation comments to parts of the code

V3.1 – 2024.05.20

Fixed bug in curve monotonization under certain conditions
Resolved missing software icon issue

V3.2 – 2024.05.21

Fixed missing software icon issue

V4.0 – 2024.07.03

Support for adding auxiliary data; auxiliary data undergoes corresponding operations with the hysteresis curve (cutting, deletion, interpolation, etc.)
Introduced a new skeleton point determination method: "Maximum Displacement & Maximum Force"

V4.1 – 2024.07.03

Fixed bug in density augmentation of auxiliary data

V4.2 – 2024.07.11

Added export of curve plots and auxiliary data

V4.3 – 2024.07.15

Optimized processing speed and fixed several bugs

V4.4 – 2024.08.06

Fixed bug in residual deformation calculation
Each hysteresis loop now displays residual deformation points and skeleton points
Added export of maximum bearing capacity for each loop

V4.5 – 2025.01.08

"About" page now shows the last update time
Smoothed curves on the display page changed from load-time history to hysteresis curve

V4.7 – 2025.10.26

Export auxiliary data for each loop


FIXME:
Detect abnormal displacement values
"""
