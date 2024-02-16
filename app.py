# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TOy5grLDBrBS4-vuwu4tOjXAuQKVmg10
"""

import streamlit as st
import os


# EDA Pkgs
import pandas as pd 
import numpy as np 

# Data Viz Pkgs
import matplotlib
matplotlib.use('Agg')# To Prevent Errors
import matplotlib.pyplot as plt
import seaborn as sns 

# ML Pkgs
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import joblib
import pickle
#import uvicorn
#Ini App
#app=FastAPI()
#Routes
#@app.get('/')
#async def index():
    #return "Hello API"
from fastapi import FastAPI
import uvicorn
import nest_asyncio
#nest_asyncio.apply()
#Ini App
#app=FastAPI()
#Routes
  
#@app.get('/')
#async def index():
    #return "Hello API"

from PIL import Image
#def load_image(url):
    #with urllib.request.urlopen(url) as response:
        #image = np.asarray(bytearray(response.read()), dtype="uint8")
    #image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #image = image[:, :, [2, 1, 0]] # BGR -> RGB
    #return image
#background-image:open("healthcare.jpg")






def main():


    


    """ ML App with Streamlit for IVF Prediction"""
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Healthcare Treatment Prediction")
    image = Image.open('healthcare.jpg')
    st.image(image, caption='AI in healthcare',use_column_width=True)
    #from fastapi import FastAPI
    #import uvicorn
    #import nest_asyncio

    #app=FastAPI()
    #Routes
  
    #@app.get('/')
    #async def index():
        #return "Hello API"
    





    activity=["Descriptive","Predictive"]
    choice=st.sidebar.selectbox("Choose Analytics Type",activity)

    if choice=="Descriptive":
        st.subheader("EDA Aspect")
        # Load Our Dataset
        df = pd.read_csv("ivf.csv")
        ## Handling Missing values
        #dataset['CycleDuration'] = dataset.CycleDuration.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.CycleDuration.isnull(), 'CycleDuration'] = df.CycleDuration.mean()
        df.CycleDuration = df.CycleDuration.astype('int')
    
        #dataset['MenstruationDays'] = dataset.MenstruationDays.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.MenstruationDays.isnull(), 'MenstruationDays'] = df.MenstruationDays.mean()
        df.MenstruationDays = df.MenstruationDays.astype('int')
    
        #dataset['OptimumFollicaleRightOvary'] = dataset.OptimumFollicaleRightOvary.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.OptimumFollicaleRightOvary.isnull(), 'OptimumFollicaleRightOvary'] = df.OptimumFollicaleRightOvary.mean()
        df.OptimumFollicaleRightOvary = df.OptimumFollicaleRightOvary.astype('int')
    
        #dataset['OptimumFollicaleLeftOvary'] = dataset.OptimumFollicaleLeftOvary.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.OptimumFollicaleLeftOvary.isnull(), 'OptimumFollicaleLeftOvary'] = df.OptimumFollicaleLeftOvary.mean()
        df.OptimumFollicaleLeftOvary = df.OptimumFollicaleLeftOvary.astype('int')
    
        #dataset['EndometriumThickness'] = dataset.EndometriumThickness.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.EndometriumThickness.isnull(), 'EndometriumThickness'] = df.EndometriumThickness.mean()
        df.EndometriumThickness = df.EndometriumThickness.astype('int')
    
        #dataset['EmbryoCount'] = dataset.EmbryoCount.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.EmbryoCount.isnull(), 'EmbryoCount'] = df.EmbryoCount.mean()
        df.EmbryoCount = df.EmbryoCount.astype('int')
    
        #dataset['TransferDay'] = dataset.TransferDay.isnull() # adding an extra column indicating whether the value are present or not.
        df.loc[df.TransferDay.isnull(), 'TransferDay'] = df.TransferDay.mean()
        df.TransferDay = df.TransferDay.astype('int')
    
        #dataset=dataset.replace(to_replace=['Positive','Negative','No','Yes','A +ve','B +ve','B -ve','AB +ve','O +ve','O -ve','Not Known','Present','Absent','Regular','Regularly Irregular','Irregularly Irregular','Moderate','Normal','Scanty','Mild','Moderate','Severe','FET','OI','OPU','IUI','IUI (D)','IVF-ICSI','ICSI','TI','Minimal Stimulation','Antagonist','Other','GnRh Long Protocol','Recipient Antagonist','Partner','Donor','Ejaculation','Surgical Extraction','ShortGA','A','B','C','>8','Hatching Blastocyst','Expanded Blast','Expanding Blastocyst','Frozen','Fresh'],value=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48])
       
    
    
        df['EmbryoCount'].fillna(df['EmbryoCount'].mode()[0], inplace=True)
        #dataset['AnesthesiaType '].fillna(dataset['AnesthesiaType '].mode()[0], inplace=True) 
        #dataset['StimulationDrug'].fillna(dataset['StimulationDrug'].mode()[0], inplace=True) 
        #dataset['Indication'].fillna(dataset['Indication'].mode()[0], inplace=True) 
        df['Protocol'].fillna(df['Protocol'].mode()[0], inplace=True)
        #dataset['IntermenstrualBleeding'].fillna(dataset['IntermenstrualBleeding'].mode()[0], inplace=True) 
        df['Dysmennorhea'].fillna(df['Dysmennorhea'].mode()[0], inplace=True) 
        df['Ammenorhea'].fillna(df['Ammenorhea'].mode()[0], inplace=True) 
        df['BloodGroup'].fillna(df['BloodGroup'].mode()[0], inplace=True) 
        #df['Consanguinity'].fillna(df['Consanguinity'].mode()[0], inplace=True) 
        df['ARTType'].fillna(df['ARTType'].mode()[0], inplace=True) 
        df['ARTSubType'].fillna(df['ARTSubType'].mode()[0], inplace=True) 
        df['SourceofSperm'].fillna(df['SourceofSperm'].mode()[0], inplace=True) 
        df['MethodofSemenCollection'].fillna(df['MethodofSemenCollection'].mode()[0], inplace=True)
        df['EmbryoStatus'].fillna(df['EmbryoStatus'].mode()[0], inplace=True) 
        df['Grade'].fillna(df['Grade'].mode()[0], inplace=True)
        #train['EndometriumThickness'].fillna(train['EndometriumThickness'].mode()[0], inplace=True) 
        #df['UseofTenaculum'].fillna(df['UseofTenaculum'].mode()[0], inplace=True) 
        df['CellStage'].fillna(df['CellStage'].mode()[0], inplace=True) 
        #train['TransferDay'].fillna(train['TransferDay'].mode()[0], inplace=True)
        #dataset['UseofStylet'].fillna(dataset['UseofStylet'].mode()[0], inplace=True)


            #dataset['OptimumFollicaleRightOvary'].fillna(dataset['OptimumFollicaleRightOvary'].mode()[0], inplace=True) 
            #dataset['OptimumFollicaleLeftOvary'].fillna(dataset['OptimumFollicaleLeftOvary'].mode()[0], inplace=True) 
            #dataset['EndometriumThickness'].fillna(dataset['EndometriumThickness'].mode()[0], inplace=True) 
            #dataset['EmbryoCount'].fillna(dataset['EmbryoCount'].mode()[0], inplace=True) 
            #dataset['CycleDuration'].fillna(dataset['CycleDuration'].mode()[0], inplace=True)
            #dataset['MenstruationDays'].fillna(dataset['MenstruationDays'].mode()[0], inplace=True)
        df['MenstralRegularity'].fillna(df['MenstralRegularity'].mode()[0], inplace=True)
        df['MenstrualFlow'].fillna(df['MenstrualFlow'].mode()[0], inplace=True)


        #df=df.replace(to_replace=['Positive','Negative','A +ve','B +ve','B -ve','O +ve','O -ve','Present','Absent','Regular',
                                      #'Regularly Irregular','Irregularly Irregular','Moderate','Normal','Scanty','Mild','Moderate','FET','OI','OPU','IUI',
                                      #'IUI (D)','IVF-ICSI','ICSI','TI','Minimal Stimulation','Antagonist','Other','GnRh Long Protocol','Partner',
                                      #'Donor','Ejaculation','Surgical Extraction','A','B','Frozen','Fresh'],value=[1,0,0,1,3,2,4,1,0,1,0,2,1,
                                                                                                                   #0,2,2,1,0,1,2,2,3,4,1,5,0,1,3,2,0,1,0,1,0,1,0,1])
                 
        if st.checkbox("Show DataSet"):
            number = st.number_input("Number of Rows to View")
            st.dataframe(df.head(int(number)))
        if st.button("Columns Names"):
            st.write(df.columns)

        if st.checkbox("Shape of Dataset"):
            st.write(df.shape)
            data_dim = st.radio("Show Dimension by",("Rows","Columns"))
            if data_dim == 'Rows':
                st.text("Number of  Rows")
                st.write(df.shape[0])
            elif data_dim == 'Columns':
                st.text("Number of Columns")
                st.write(df.shape[1])
                
        if st.checkbox("Select Columns To Show"):
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect('Select',all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)
            
        if st.button("Data Types"):
            st.write(df.dtypes)
            
        if st.button("Value Counts"):
            st.text("Value Counts By Target/Class")
            st.write(df.iloc[:,-1].value_counts())

        st.subheader("Data Visualization")
        # Show Correlation Plots
        # Matplotlib Plot
        if st.checkbox("Correlation Plot [Matplotlib]"):
            plt.matshow(df.corr())
            st.pyplot()
        # Seaborn Plot
        if st.checkbox("Correlation Plot with Annotation[Seaborn]"):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()
        # Counts Plots
        if st.checkbox("Plot of Value Counts"):
            st.text("Value Counts By Target/Class")
            all_columns_names = df.columns.tolist()
            primary_col = st.selectbox('Select Primary Column To Group By',all_columns_names)
            selected_column_names = st.multiselect('Select Columns',all_columns_names)
            if st.button("Plot"):
                st.text("Generating Plot for: {} and {}".format(primary_col,selected_column_names))
                if selected_column_names:
                    vc_plot = df.groupby(primary_col)[selected_column_names].count()
                else:
                    vc_plot = df.iloc[:,-1].value_counts()
                st.write(vc_plot.plot(kind='bar'))
                st.pyplot()
        if st.checkbox("Pie Plot"):
            all_columns_names = df.columns.tolist()
            # st.info("Please Choose Target Column")
            # int_column =  st.selectbox('Select Int Columns For Pie Plot',all_columns_names)
            if st.button("Generate Pie Plot"):
                # cust_values = df[int_column].value_counts()
                # st.write(cust_values.plot.pie(autopct="%1.1f%%"))
                st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()
                #Prediction
    if choice=="Predictive":
        st.subheader("Options For Prediction")
        st.subheader("Attributes To Select from")
        def get_value(val,my_dict):
            for key ,value in my_dict.items():
                if val == key:
                    return value
        ARTType = {"FET":0,"OI":1,"OPU":2}
        choice_ARTType = st.radio("ARTType",tuple(ARTType.keys()))
        result_ARTType = get_value(choice_ARTType,ARTType)
        # st.text(result_ARTType)


        ARTSubType = {"FET":0,"ICSI":1,"IUI":2,"IUI (D)":3,"IVF-ICSI":4,"TI":5}
        choice_ARTSubType = st.radio("ARTSubType",tuple(ARTSubType.keys()))
        result_ARTSubType = get_value(choice_ARTSubType,ARTSubType)
        # st.text(result_ARTSubType)

	
        CycleDuration = st.slider("Select CycleDuration",0,35)
        #husband_education = st.number_input("Husband's Education Level(low2High) [1,4]",1,4)
        MenstruationDays = st.number_input("MenstruationDays")


        EndometriumThickness = st.number_input("EndometriumThickness(low2High) [1,20]",1,20)
        #media_exposure = {"Good":0,"Not Good":1}
        #choice_media_exposure = st.radio("Media Exposure",tuple(media_exposure.keys()))
        #result_media_exposure = get_value(choice_media_exposure,media_exposure)

        BloodGroup = {"A +ve":0,"B +ve":1,"O +ve":2,"B -ve":3,"O -ve":4}
        choice_BloodGroup = st.radio("BloodGroup",tuple(BloodGroup.keys()))
        result_BloodGroup = get_value(choice_BloodGroup,BloodGroup)
        # st.text(result_BloodGroup)

        
        Ammenorhea = {"Absent":0,"Present":1}
        choice_Ammenorhea = st.radio("Ammenorhea",tuple(Ammenorhea.keys()))
        result_Ammenorhea = get_value(choice_Ammenorhea,Ammenorhea)
        # st.text(result_Ammenorhea)

        
        MenstralRegularity = {"Regularly Irregular":0,"Regular":1,"Irregularly Irregular":2}
        choice_MenstralRegularity = st.radio("MenstralRegularity",tuple(MenstralRegularity.keys()))
        result_MenstralRegularity = get_value(choice_MenstralRegularity,MenstralRegularity)
        # st.text(result_MenstralRegularity)

        
        MenstrualFlow = {"Normal":0,"Moderate":1,"Scanty":2}
        choice_MenstrualFlow = st.radio("MenstrualFlow",tuple(MenstrualFlow.keys()))
        result_MenstrualFlow = get_value(choice_MenstrualFlow,MenstrualFlow)
        # st.text(result_MenstrualFlow)

        Dysmennorhea = {"Absent":0,"Moderate":1,"Mild":2}
        choice_Dysmennorhea = st.radio("Dysmennorhea",tuple(Dysmennorhea.keys()))
        result_Dysmennorhea = get_value(choice_Dysmennorhea,Dysmennorhea)
        # st.text(result_Dysmennorhea)

        Protocol = {"Minimal Stimulation":0,"Antagonist":1,"GnRh Long Protocol":2,"Other":3}
        choice_Protocol = st.radio("Protocol",tuple(Protocol.keys()))
        result_Protocol = get_value(choice_Protocol,Protocol)
        # st.text(result_Protocol)

        SourceofSperm = {"Partner":0,"Donor":1}
        choice_SourceofSperm = st.radio("SourceofSperm",tuple(SourceofSperm.keys()))
        result_SourceofSperm = get_value(choice_SourceofSperm,SourceofSperm)
        # st.text(result_SourceofSperm)

        MethodofSemenCollection = {"Ejaculation":0,"Surgical Extraction":1}
        choice_MethodofSemenCollection = st.radio("MethodofSemenCollection",tuple(MethodofSemenCollection.keys()))
        result_MethodofSemenCollection = get_value(choice_MethodofSemenCollection,MethodofSemenCollection)
        # st.text(result_MethodofSemenCollection)

        OptimumFollicaleRightOvary = st.slider("Select OptimumFollicaleRightOvary",0,100)
        #husband_education = st.number_input("Husband's Education Level(low2High) [1,4]",1,4)
        #OptimumFollicaleRightOvary = st.number_input("OptimumFollicaleRightOvary")

        OptimumFollicaleLeftOvary = st.slider("Select OptimumFollicaleLeftOvary",0,100)
        #husband_education = st.number_input("Husband's Education Level(low2High) [1,4]",1,4)
        #OptimumFollicaleLeftOvary = st.number_input("OptimumFollicaleLeftOvary")

        
        EmbryoCount = st.number_input("EmbryoCount(low2High) [1,3]",1,3)

        
        TransferDay = st.number_input("TransferDay(low2High) [1,20]",1,20)

        Grade = {"A":0,"B":1}
        choice_Grade = st.radio("Grade",tuple(Grade.keys()))
        result_Grade = get_value(choice_Grade,Grade)
        # st.text(result_Grade)

        #CellStage = st.slider("Select CellStage",0,100)
        #husband_education = st.number_input("Husband's Education Level(low2High) [1,4]",1,4)
        CellStage = st.number_input("CellStage")

        
        EmbryoStatus = {"Frozen":0,"Fresh":1}
        choice_EmbryoStatus = st.radio("EmbryoStatus",tuple(EmbryoStatus.keys()))
        result_EmbryoStatus = get_value(choice_EmbryoStatus,EmbryoStatus)
        # st.text(result_EmbryoStatus)


        # Result and in json format
        results = [result_ARTType,result_ARTSubType,CycleDuration,MenstruationDays,EndometriumThickness,result_BloodGroup,result_Ammenorhea,result_MenstralRegularity
                   ,result_MenstrualFlow,result_Dysmennorhea,result_Protocol,result_SourceofSperm,result_MethodofSemenCollection,OptimumFollicaleRightOvary,OptimumFollicaleLeftOvary,EmbryoCount,
                   TransferDay,result_Grade,CellStage,result_EmbryoStatus]
        displayed_results = [choice_ARTType,choice_ARTSubType,CycleDuration,MenstruationDays,EndometriumThickness,choice_BloodGroup,choice_Ammenorhea,choice_MenstralRegularity
                   ,choice_MenstrualFlow,choice_Dysmennorhea,choice_Protocol,choice_SourceofSperm,choice_MethodofSemenCollection,OptimumFollicaleRightOvary,OptimumFollicaleLeftOvary,EmbryoCount,
                   TransferDay,choice_Grade,CellStage,choice_EmbryoStatus]
        prettified_result = {"result_ARTType":choice_ARTType,
        "result_ARTSubType":choice_ARTSubType,
        "CycleDuration":CycleDuration,
        "MenstruationDays":MenstruationDays,
        "EndometriumThickness":EndometriumThickness,
        "result_BloodGroup":choice_BloodGroup,
        "result_Ammenorhea":choice_Ammenorhea,                     
        "result_MenstralRegularity":choice_MenstralRegularity,
        "result_MenstrualFlow":choice_MenstrualFlow,
        "result_Dysmennorhea":choice_Dysmennorhea,
        "result_Protocol":choice_Protocol,
        "result_SourceofSperm":choice_SourceofSperm,
        "result_MethodofSemenCollection":choice_MethodofSemenCollection,
        "OptimumFollicaleRightOvary":OptimumFollicaleRightOvary,
        "OptimumFollicaleLeftOvary":OptimumFollicaleLeftOvary,
        "EmbryoCount":EmbryoCount,
        "TransferDay":TransferDay,
        "result_Grade":choice_Grade,
        "CellStage":CellStage,
        "result_EmbryoStatus":choice_EmbryoStatus}                     

        sample_data = np.array(results).reshape(1, -1)
        st.info(results)
	
	
        if st.checkbox("Your Inputs Summary"):
            st.json(prettified_result)
            st.text("Vectorized as ::{}".format(results))
        #st.subheader("Prediction")
        if st.checkbox("Make Prediction"):
            all_ml_dict = {'LR':LogisticRegression(),'CART':DecisionTreeClassifier(),'RForest':RandomForestClassifier(),'NB':GaussianNB(),'SVC':LinearSVC()}
	   #'MultNB':MultinomialNB()}
                    # models = []
        # model_choice = st.multiselect('Model Choices',list(all_ml_dict.keys()))
	# for key in all_ml_dict:
	# 	if 'RForest' in key:
	# 		st.write(key)

	# Find the Key From Dictionary
            def get_key(val,my_dict):
                for key ,value in my_dict.items():
                    if val == value:
                        return key
           
            ## Handling Missing values
            df = pd.read_csv("ivf.csv")                 
            #dataset['CycleDuration'] = dataset.CycleDuration.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.CycleDuration.isnull(), 'CycleDuration'] = df.CycleDuration.mean()
            df.CycleDuration = df.CycleDuration.astype('int')
    
            #dataset['MenstruationDays'] = dataset.MenstruationDays.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.MenstruationDays.isnull(), 'MenstruationDays'] = df.MenstruationDays.mean()
            df.MenstruationDays = df.MenstruationDays.astype('int')
    
            #dataset['OptimumFollicaleRightOvary'] = dataset.OptimumFollicaleRightOvary.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.OptimumFollicaleRightOvary.isnull(), 'OptimumFollicaleRightOvary'] = df.OptimumFollicaleRightOvary.mean()
            df.OptimumFollicaleRightOvary = df.OptimumFollicaleRightOvary.astype('int')
    
            #dataset['OptimumFollicaleLeftOvary'] = dataset.OptimumFollicaleLeftOvary.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.OptimumFollicaleLeftOvary.isnull(), 'OptimumFollicaleLeftOvary'] = df.OptimumFollicaleLeftOvary.mean()
            df.OptimumFollicaleLeftOvary = df.OptimumFollicaleLeftOvary.astype('int')
    
            #dataset['EndometriumThickness'] = dataset.EndometriumThickness.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.EndometriumThickness.isnull(), 'EndometriumThickness'] = df.EndometriumThickness.mean()
            df.EndometriumThickness = df.EndometriumThickness.astype('int')
    
            #dataset['EmbryoCount'] = dataset.EmbryoCount.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.EmbryoCount.isnull(), 'EmbryoCount'] = df.EmbryoCount.mean()
            df.EmbryoCount = df.EmbryoCount.astype('int')
    
            #dataset['TransferDay'] = dataset.TransferDay.isnull() # adding an extra column indicating whether the value are present or not.
            df.loc[df.TransferDay.isnull(), 'TransferDay'] = df.TransferDay.mean()
            df.TransferDay = df.TransferDay.astype('int')
    
            #dataset=dataset.replace(to_replace=['Positive','Negative','No','Yes','A +ve','B +ve','B -ve','AB +ve','O +ve','O -ve','Not Known','Present','Absent','Regular','Regularly Irregular','Irregularly Irregular','Moderate','Normal','Scanty','Mild','Moderate','Severe','FET','OI','OPU','IUI','IUI (D)','IVF-ICSI','ICSI','TI','Minimal Stimulation','Antagonist','Other','GnRh Long Protocol','Recipient Antagonist','Partner','Donor','Ejaculation','Surgical Extraction','ShortGA','A','B','C','>8','Hatching Blastocyst','Expanded Blast','Expanding Blastocyst','Frozen','Fresh'],value=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48])
       
    
    
            df['EmbryoCount'].fillna(df['EmbryoCount'].mode()[0], inplace=True)
            #dataset['AnesthesiaType '].fillna(dataset['AnesthesiaType '].mode()[0], inplace=True) 
            #dataset['StimulationDrug'].fillna(dataset['StimulationDrug'].mode()[0], inplace=True) 
            #dataset['Indication'].fillna(dataset['Indication'].mode()[0], inplace=True) 
            df['Protocol'].fillna(df['Protocol'].mode()[0], inplace=True)
            #dataset['IntermenstrualBleeding'].fillna(dataset['IntermenstrualBleeding'].mode()[0], inplace=True) 
            df['Dysmennorhea'].fillna(df['Dysmennorhea'].mode()[0], inplace=True) 
            df['Ammenorhea'].fillna(df['Ammenorhea'].mode()[0], inplace=True) 
            df['BloodGroup'].fillna(df['BloodGroup'].mode()[0], inplace=True) 
            #df['Consanguinity'].fillna(df['Consanguinity'].mode()[0], inplace=True) 
            df['ARTType'].fillna(df['ARTType'].mode()[0], inplace=True) 
            df['ARTSubType'].fillna(df['ARTSubType'].mode()[0], inplace=True) 
            df['SourceofSperm'].fillna(df['SourceofSperm'].mode()[0], inplace=True) 
            df['MethodofSemenCollection'].fillna(df['MethodofSemenCollection'].mode()[0], inplace=True)
            df['EmbryoStatus'].fillna(df['EmbryoStatus'].mode()[0], inplace=True) 
            df['Grade'].fillna(df['Grade'].mode()[0], inplace=True)
            #train['EndometriumThickness'].fillna(train['EndometriumThickness'].mode()[0], inplace=True) 
            #df['UseofTenaculum'].fillna(df['UseofTenaculum'].mode()[0], inplace=True) 
            df['CellStage'].fillna(df['CellStage'].mode()[0], inplace=True) 
            #train['TransferDay'].fillna(train['TransferDay'].mode()[0], inplace=True)
            #dataset['UseofStylet'].fillna(dataset['UseofStylet'].mode()[0], inplace=True)


            #dataset['OptimumFollicaleRightOvary'].fillna(dataset['OptimumFollicaleRightOvary'].mode()[0], inplace=True) 
            #dataset['OptimumFollicaleLeftOvary'].fillna(dataset['OptimumFollicaleLeftOvary'].mode()[0], inplace=True) 
            #dataset['EndometriumThickness'].fillna(dataset['EndometriumThickness'].mode()[0], inplace=True) 
            #dataset['EmbryoCount'].fillna(dataset['EmbryoCount'].mode()[0], inplace=True) 
            #dataset['CycleDuration'].fillna(dataset['CycleDuration'].mode()[0], inplace=True)
            #dataset['MenstruationDays'].fillna(dataset['MenstruationDays'].mode()[0], inplace=True)
            df['MenstralRegularity'].fillna(df['MenstralRegularity'].mode()[0], inplace=True)
            df['MenstrualFlow'].fillna(df['MenstrualFlow'].mode()[0], inplace=True)


            #df=df.replace(to_replace=['Positive','Negative','A +ve','B +ve','B -ve','O +ve','O -ve','Present','Absent','Regular',
                                      #'Regularly Irregular','Irregularly Irregular','Moderate','Normal','Scanty','Mild','Moderate','FET','OI','OPU','IUI',
                                      #'IUI (D)','IVF-ICSI','ICSI','TI','Minimal Stimulation','Antagonist','Other','Recipient Antagonist','GnRh Long Protocol','Partner',
                                      #'Donor','Ejaculation','Surgical Extraction','A','B','C','Frozen','Fresh'],value=[1,0,0,1,3,2,4,1,0,1,0,2,1,
                                                                                                                   #0,2,2,1,0,1,2,2,3,4,1,5,0,1,3,4,2,0,1,0,1,0,1,2,0,1])
                 



            #Create model files
            #df = pd.read_csv("ivf.csv")
            X=df.drop('ResultType',axis=1)
            Y=df['ResultType'].to_numpy()
            x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.20,random_state=42)
            state = 12  
            test_size = 0.30
            x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,test_size=test_size, random_state=state)
            RForest=RandomForestClassifier()
            RForest.fit(x_train,y_train)
            LR=LogisticRegression()
            LR.fit(x_train,y_train)
            CART=DecisionTreeClassifier()
            CART.fit(x_train,y_train)
            NB=GaussianNB()
            NB.fit(x_train,y_train)
            SVC=LinearSVC()
            SVC.fit(x_train,y_train)
            from sklearn.metrics import confusion_matrix
            
            
            pickle.dump(RForest,open('ivf_rf_model.pkl','wb'))
            pickle.dump(LR,open('ivf_lr_model.pkl','wb'))
            pickle.dump(CART,open('ivf_cart_model.pkl','wb'))
            pickle.dump(NB,open('ivf_nb_model.pkl','wb'))
            pickle.dump(SVC,open('ivf_svc_model.pkl','wb'))

                             
           

             # Load Models
            def load_model_n_predict(model_file):
                loaded_model = pickle.load(open(os.path.join(model_file),"rb"))
                return loaded_model
            model_choice = st.selectbox('Model Choice',list(all_ml_dict.keys()))
            prediction_label = {"Positive": 1,"Negative": 0}
            if st.button("Predict"):
                if model_choice == 'RForest':
                    loaded_model = pickle.load(open("ivf_rf_model.pkl","rb"))
                    prediction = loaded_model.predict(sample_data)
                    score=RForest.score(x_test, y_test)
                    st.text(score)
                    y_pred = RForest.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    st.text(cm)
                # final_result = get_key(prediction,prediction_label)
                # st.info(final_result)
                elif model_choice == 'LR':
                    model_predictor = load_model_n_predict("ivf_lr_model.pkl")
                    prediction = model_predictor.predict(sample_data)
                    score=LR.score(x_test, y_test)
                    st.text(score)
                    y_pred = LR.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    st.text(cm)
                 # st.text(prediction)
                elif model_choice == 'CART':
                    model_predictor = load_model_n_predict("ivf_cart_model.pkl")
                    prediction = model_predictor.predict(sample_data)
                    score=CART.score(x_test, y_test)
                    st.text(score)
                    y_pred = CART.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    st.text(cm)
                # st.text(prediction)
                elif model_choice == 'NB':
                    model_predictor = load_model_n_predict("ivf_nb_model.pkl")
                    prediction = model_predictor.predict(sample_data)
                    score=NB.score(x_test, y_test)
                    st.text(score)
                    y_pred = NB.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    st.text(cm)
                 # st.text(prediction)
                elif model_choice == 'SVC':
                    model_predictor = load_model_n_predict("ivf_svc_model.pkl")
                    prediction = model_predictor.predict(sample_data)
                    score=SVC.score(x_test, y_test)
                    st.text(score)
                    y_pred = SVC.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    st.text(cm)
                    #st.text(prediction) 
                final_result = get_key(prediction,prediction_label)
                st.success(final_result)
    st.sidebar.subheader("About")
    st.sidebar.info("Project")
    st.sidebar.text("IVF")
    if st.sidebar.button("About"):
        st.sidebar.text("Ankita")
        st.sidebar.text("darekarankita0")
if __name__ == '__main__':
    main()
