with open("login_times.log", "r") as f:
    login_times = f.read() 

char_list = list(login_times)  
print(char_list)
time_list = char_list[-23:-53]
ip_list = char_list[-1:-9]
print(time_list)
print(ip_list)
time_login = ' '.join([str(element) for element in time_list]) 

user_ip = ' '.join([str(element) for element in ip_list]) 

print(time_login)
print(user_ip) 