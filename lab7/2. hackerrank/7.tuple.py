if __name__ == '__main__':
    
   n = int(input())
   integer_list = [int(i) for i in input().split()]
   integer_tuple = tuple(integer_list)
   print(hash(integer_tuple))