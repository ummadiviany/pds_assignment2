# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-09-16 11:53:03
#  * @modify date 2022-09-16 11:53:03
#  * @desc [description]
#  */
# ----------------------------------------------------
import pandas as pd
from time import time

data = pd.read_csv('data/mtsamples.csv')

def get_medical_specalities():
    """Returns the unique set of alphabetically ordered medical specialities from the data/mtsamples file.
    Input file: data/mtsamples.csv
    Output: Return a list of strings containing the unique set of alphabetically ordered medical specialities.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    
    
            
    return 


def get_medical_specialities_count():
    """Returns the count of medical specialities in the data/mtsamples file.
    Input file: data/mtsamples.csv
    Output: Return a dictionary with key as the medical speciality and value as the count of the speciality. The dictionary should be sorted by the count in descending order.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    
    
    return 

def get_medical_speciality_sample_names():
    """This function returns a dictionary with key as the medical speciality and value as a list of sample names for that speciality.
    Input file: data/mtsamples.csv
    Output: Return a dictionary with key as the medical speciality and value as a list of sample names for that speciality.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    
    
    return


if __name__ == "__main__":
    start = time()
    
        
    
    print(f"Time taken: {time() - start :.2f} seconds")