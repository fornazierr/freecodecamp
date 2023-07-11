def add_time(start: str, duration: str, ):
  current_hour = int(start[:start.find(":")])
  current_min = int(start[start.find(":")+1:start.find(" ")])
  current_am_pm = int(start[start.find(" ")+1:])
  saldo_hora = int(duration.split(":")[0])
  saldo_min = int(duration.split(":")[1])
  
  print(start)
  print("Start:",current_hour, current_min, current_am_pm)
  print("Saldo:", saldo_hora, saldo_min)
  
  
  soma_min = int(current_min) + int(saldo_min)
  if soma_min > 60:
    saldo_hora += saldo_hora 
    current_min = soma_min-60
    saldo_min = 0
  else:
    saldo_min = 0
  
  while saldo_hora > 0:
    print("kkkkk")
     
  
  return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa"