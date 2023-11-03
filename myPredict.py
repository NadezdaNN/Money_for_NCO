import pandas as pd
import category_encoders as ce
import pickle

def func_predict(region, opf, okved, addOkved, age):
    data = pd.read_csv('df_for_encoder.csv')
    tmp = data[['regionName', 'opf_name', 'mainOkved_name', 'addOkved_name']]
    tmp.loc[len(data.index)] = [region, opf, okved, addOkved]

    bin_encoder = ce.BinaryEncoder(cols=['regionName', 'opf_name', 'mainOkved_name','addOkved_name']) # указываем столбец для кодирования
    type_bin = bin_encoder.fit_transform(tmp[['regionName', 'opf_name', 'mainOkved_name','addOkved_name']])

    age=pd.DataFrame({'age': [age]})
    tmp = type_bin.head(1)
    tmp_bin = pd.concat([tmp, age], axis=1)
    print('tmp_bin', tmp_bin)
    
    # Производим десериализацию и извлекаем модель из файла формата pkl
    with open('myfile.pkl', 'rb') as pkl_file:
        model = pickle.load(pkl_file)
    #print(model)

    #Делаем предсказание вероятностей:
    #y_new_proba_predict = model.predict(tmp_bin.head(1)) # ???
    #print('Predicted probabilities: {}'.format(np.round(y_new_proba_predict, 2)))

    return str('Здесь должна быть вероятность')