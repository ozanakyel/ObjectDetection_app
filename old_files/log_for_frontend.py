class Log():
    def __init__(self):
        self.log_array = {'type': [], 'content': [], 'time': []}
    
    def log_for_frontend(self, log_array_type, log_array_content, time):
        if len(self.log_array['type']) == 100:
            self.log_array["type"].pop()
            self.log_array["content"].pop()
            self.log_array["time"].pop()
            self.log_array["type"].append(log_array_type)
            self.log_array["content"].append(log_array_content)
            self.log_array["time"].append(time)
        else:
            self.log_array["type"].append(log_array_type)
            self.log_array["content"].append(log_array_content)
            self.log_array["time"].append(time)
    
    def get_(self):
        return self.log_array
    
# # LOG
# log_for_frontend = Log()
# for item in range(10):
#     log_array = {"type": [],"content": []}
#     log_array["type"].append("error")
#     log_array["content"].append(str(f"Kamera Baglantisi Saglanamadi"))
#     log_for_frontend.log_for_frontend("error", str(f"Kamera Baglantisi Saglanamadi"))
# print(log_for_frontend.log_array)
# ####################