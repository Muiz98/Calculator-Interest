import streamlit as st

import pandas as pd

# from sklearn import datasets

# from sklearn.ensemble import RandomForestClassifier

Year_List=[1,2,3,4,5,6,7,8,9,10]


st.write("""

# Interest Calculator Per Year!

""")



st.sidebar.header('User Input Values')



def user_input_features():
    
    Principal = st.sidebar.text_input('Please input Principal Amount',10000)
    
    Int_Rate = st.sidebar.slider('Interest Rate in %', 2.0, 43.0, 8.0)

    No_Of_Years = st.sidebar.selectbox('Select No Of Years',Year_List, 1)
    
    	##st.sidebar.add_rows

    	##st.sidebar.add_rows

   



    data = {'Int_Rate': Int_Rate,	
            'Principal': Principal,	
            'No_Of_Years': No_Of_Years}
    features = pd.DataFrame(data, index=[0])
    return features



df = user_input_features()



st.subheader('Entered for the Rate, Amount and No. of years is')

st.write(df)


# Compound Interest function
def compound_int(Principal, Int_Rate, No_Of_Years):

    comp=1.0
    for i in range(0, int(No_Of_Years)):
        comp=comp*(1+Int_Rate/100)
        #st.write(comp)
    comp=float(Principal)*(comp-1)
    comp_text= str("Compound Interest is " + str("%.3f" % comp) )
    st.write(comp_text)
    data_1 = {'Computed_Compound_Interest': comp_text}

    result = pd.DataFrame(data_1, index=[0])

    return result






st.subheader('The calculated interest is')

#st.write(result)
df_1=compound_int(df.Principal, df.Int_Rate, df.No_Of_Years)


st.subheader('Data frame')

st.write(df_1)
