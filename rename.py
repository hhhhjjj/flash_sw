    def rename_app(self):
        # key在前，value在后
        for new_name, dir_name in self.correspondence.items():
            os.renames(dir_name, os.path.join(self.app_path, new_name))
        now_name = sys._getframe().f_code.co_name
        write(now_name)
