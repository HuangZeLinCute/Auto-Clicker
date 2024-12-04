import pyautogui
import time
import random
import threading
import keyboard
import math
import sys
from PyQt5 import QtWidgets, QtCore

clicking = False
center_point = None
radius = 10
click_count = 0


class AutoClickerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('连点器控制面板')
        self.setGeometry(100, 100, 400, 250)

        layout = QtWidgets.QVBoxLayout()

        self.status_label = QtWidgets.QLabel("当前状态: 未启动", self)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.position_label = QtWidgets.QLabel("当前鼠标位置: (0, 0)", self)
        self.position_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.position_label)

        self.hotkey_label = QtWidgets.QLabel("启动关闭热键：F8", self)
        layout.addWidget(self.hotkey_label)

        self.radius_label = QtWidgets.QLabel("设置点击圆的半径：", self)
        layout.addWidget(self.radius_label)

        self.radius_input = QtWidgets.QLineEdit(self)
        self.radius_input.setPlaceholderText("默认半径: 10")
        layout.addWidget(self.radius_input)

        self.frequency_label = QtWidgets.QLabel("设置点击频率（秒）：", self)
        layout.addWidget(self.frequency_label)

        self.frequency_input = QtWidgets.QLineEdit(self)
        self.frequency_input.setPlaceholderText("默认频率: 0.1")
        layout.addWidget(self.frequency_input)

        self.stay_on_top_button = QtWidgets.QPushButton("设置置顶", self)
        self.stay_on_top_button.clicked.connect(self.set_window_top)
        layout.addWidget(self.stay_on_top_button)

        self.setLayout(layout)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_mouse_position)
        self.timer.start(100)

    def toggle_clicker(self):
        global clicking, center_point, radius

        clicking = not clicking

        if clicking:
            try:
                radius = float(self.radius_input.text()) if self.radius_input.text() else 10
            except ValueError:
                self.show_error_message("请输入有效的数字作为半径！")
                clicking = False
                return

            center_point = pyautogui.position()
            self.status_label.setText(f"当前状态: 连点器启动 (点击中心: {center_point})")
            threading.Thread(target=self.auto_clicker).start()
        else:
            self.status_label.setText("当前状态: 已停止")

    def update_mouse_position(self):
        x, y = pyautogui.position()
        self.position_label.setText(f"当前鼠标位置: ({x}, {y})")

    def auto_clicker(self):
        global click_count, clicking
        click_count = 0
        while clicking:
            angle = random.uniform(0, 2 * math.pi)
            r = random.uniform(0, radius)

            offset_x = r * math.cos(angle)
            offset_y = r * math.sin(angle)
            click_x = center_point[0] + offset_x
            click_y = center_point[1] + offset_y

            pyautogui.click(click_x, click_y)
            frequency = random.uniform(0.05, 0.15)
            time.sleep(frequency)

            click_count += 1

            if click_count % random.randint(10, 30) == 0:
                pause_duration = random.uniform(1, 3)
                time.sleep(pause_duration)

    def show_error_message(self, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("错误")
        error_dialog.exec_()

    def set_window_top(self):
        try:
            if self.windowFlags() & QtCore.Qt.WindowStaysOnTopHint:
                self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
                self.status_label.setText("当前状态: 未置顶")
            else:
                self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
                self.status_label.setText("当前状态: 已置顶")
            self.show()  # 更新显示
        except Exception as e:
            print(f"发生错误: {e}")

    def closeEvent(self, event):
        sys.exit(0)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AutoClickerApp()
    window.show()

    keyboard.add_hotkey('F8', window.toggle_clicker)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
