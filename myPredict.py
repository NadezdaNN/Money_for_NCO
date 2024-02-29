import pandas as pd
import category_encoders as ce
import pickle
import numpy as np

def func_predict(region, opf, okved, addOkved, age):
    
    data = pd.read_csv('df_for_encoder.csv')

    tmp = data[['regionName', 'mainOkved_name', 'addOkved_name', 'opf_name']]
    tmp.loc[len(data.index)] = [region, okved, addOkved, opf]
    
    bin_encoder = ce.BinaryEncoder(cols=['regionName', 'mainOkved_name', 'addOkved_name','opf_name']) # указываем столбец для кодирования
    type_bin = bin_encoder.fit_transform(tmp[['regionName', 'mainOkved_name', 'addOkved_name', 'opf_name']])

    age=pd.DataFrame({'age': [age]})
    tmp = type_bin.head(1)
    tmp_bin = pd.concat([age, tmp], axis=1)    
    
    # Производим десериализацию и извлекаем модель из файла формата pkl
    with open('myfile.pkl', 'rb') as pkl_file:
        model = pickle.load(pkl_file)    
    
    #Делаем предсказание вероятностей:
    y_new_proba_predict = model.predict_proba(tmp_bin.iloc[[-1]])
    
    return str(round(y_new_proba_predict[0,1],3)*100)