# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-09-16 11:53:03
#  * @modify date 2022-09-16 11:53:03
#  * @desc [description]
#  */
# ----------------------------------------------------
import pandas as pd
import csv
from time import time

data = pd.read_csv('data/mtsamples.csv')

def get_medical_specalities():
    """Returns the unique set of alphabetically ordered medical specialities from the data/mtsamples file.
    Input file: data/mtsamples.csv
    Output: Return a list of strings containing the unique set of alphabetically ordered medical specialities.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    
    specs = data['medical_specialty'].unique().tolist()
    nspecs = []
    for spec in specs:
        if '/' in spec:
            nspecs += spec.split('/')
        else:
            nspecs.append(spec)
            
    return list(map(lambda x: x.strip(), sorted(set(nspecs))))


def get_medical_specialities_count():
    """Returns the count of medical specialities in the data/mtsamples file.
    Input file: data/mtsamples.csv
    Output: Return a dictionary with key as the medical speciality and value as the count of the speciality. The dictionary should be sorted by the count in descending order.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    specs = get_medical_specalities()
    all_specs = data['medical_specialty'].tolist()
    
    spec_count = {}
    for spec in specs:
        for s in all_specs:
            if spec in s:
                if spec in spec_count:
                    spec_count[spec] += 1
                else:
                    spec_count[spec] = 1
    
    return dict(sorted(spec_count.items(), key=lambda item: item[1], reverse=True))

def get_medical_speciality_sample_names():
    """This function returns a dictionary with key as the medical speciality and value as a list of sample names for that speciality.
    Input file: data/mtsamples.csv
    Output: Return a dictionary with key as the medical speciality and value as a list of sample names for that speciality.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    specs = get_medical_specalities()
    spec_sample_names = {spec: [] for spec in specs}
    
    for i in range(len(data)):
        for spec in specs:
            if spec in data['medical_specialty'][i]:
                spec_sample_names[spec].append(data['sample_name'][i])
                
    return spec_sample_names



if __name__ == "__main__":
    start = time()
    # print(get_medical_specalities())
    # print('-'*100)
    # print(get_medical_specialities_count())
    print('-'*100)
    print(get_medical_speciality_sample_names())
    
    print(f"Time taken: {time() - start :.2f} seconds")