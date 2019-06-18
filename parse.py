def parse_app(file_name):
    with open(file_name, "rb") as f:  # 注意这里要是rb，不然gbk读不出来
        for line in f:
            # 各个层进行循环遍历
            if re.search(b'1', line.strip()):
                return"1"
    now_name = sys._getframe().f_code.co_name
    write(now_name)
