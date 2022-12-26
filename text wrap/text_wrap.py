import textwrap

def wrap(string, max_width):
    
    n = len(string)
    i = 0
    string_arr = []
    while i < n:
        
        if i+max_width < n:
            string_arr.append(string[i:i+max_width])   
        else:
            string_arr.append(string[i:n])       
        i += max_width
        
    string_arr = "\n".join(string_arr)
          
    return string_arr

if __name__ == '__main__':