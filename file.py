    def select_log_dir(self):
        # 打开选择文件夹的弹出窗
        self.select_log_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        self.main_ui.log_path.setText(self.select_log_dir)
