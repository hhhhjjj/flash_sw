    def __init__(self):
        super().__init__()
        self.main_ui = MAIN_UI.Ui_MAIN_UI()
        # 按键进行连接,实现界面跳转
        self.main_ui.ABOUT_US.clicked.connect(self.button_connect_about)
    def button_connect_about(self):
        self.about_ui.show()
    
    if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = FLASH()
    main.show()
    sys.exit(app.exec_())
