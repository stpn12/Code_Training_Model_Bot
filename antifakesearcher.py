from catboost import CatBoostClassifier
import semantic

model = CatBoostClassifier()
model.load_model('antifake.model')

def predict(text: str):
    result = model.predict([semantic.lemmatize(text)])
    
    return result

def predict_proba(text: str):
    result = model.predict_proba([semantic.lemmatize(text)])

    return result

def main():
    while True:
        input_text = input('Введите сообщение: ')
        result = predict_proba(input_text)
        print('Вероятность фейка: ', result)

if __name__ == "__main__":
    main()