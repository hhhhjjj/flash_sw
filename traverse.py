    def traverse_app(self, path):
        file_list = os.walk(path)
        # 开始遍历文件夹
        for dir_path, dir_name, file_name in file_list:
            # 显示文件夹内的所有文件名
            for file_name_in in file_name:
                if file_name_in == self.judge_name:
                    app = parse_app(os.path.join(dir_path, self.judge_name))
                    self.correspondence[app] = dir_path
        self.rename_app()
        now_name = sys._getframe().f_code.co_name
        write(now_name)
