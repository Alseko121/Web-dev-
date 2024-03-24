m_length = 109  
v = int(input())  
t = int(input())  

distance_traveled = v * t 
position_on_MKAD = distance_traveled % m_length  

print(position_on_MKAD)  
