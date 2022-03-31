def count_substring(string, sub_string):
 t=len(string)
 req=len(sub_string)
 count=0
 for i in range(t-req +1):
   if(string[i:i+req]== sub_string):
      count += 1
 return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)