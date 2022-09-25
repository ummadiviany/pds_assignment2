# /**                                   |
#  * @author Vinay Ummadi               |
#  * @email ummadi.vinay2000@gmail.com  |
#  * @create date 2022-09-25 16:03:04   |
#  * @modify date 2022-09-25 16:03:04   |
#  * @desc [description]                |
#  */                                   |
# ---------------------------------------



def print_pattern(x : int, n : int) -> int:
    """Print the pattern as shown in task examples

    Args:
        x (int): starting number
        n (int): Number of lines to print

    Returns:
        int: return x**n
    """
    
 
    if x==0:
        return 0
    if n==0 or x==1:
        return 1
    else:
        
        result =x*print_pattern(x,(n-1))
 
        temp=n
        a=[]
        b=[]

        while temp>=0:
            a.append(chr(97+temp))
            a.insert(len(a)//2,chr(122-temp))
            b=a[-2::-1]
            temp-=1
            
        print(f'^{result}*-'.join(a),end=f'^{result+1}*-')
        print(f'^{result}*-'.join(b),end='')
        print(f'^{result}')
        

        return result

if __name__ == "__main__":
    print(print_pattern(3,3))

    

