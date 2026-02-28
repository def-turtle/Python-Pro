with open("login_times.log", "r") as f:
    login_times = f.read() 

char_list = list(login_times) 

time_list = char_list[0:10]
ip_list = char_list[42:51]
time_login = ' '.join([str(element) for element in time_list]) 

user_ip = ' '.join([str(element) for element in ip_list]) 

print(time_login)
print(user_ip)