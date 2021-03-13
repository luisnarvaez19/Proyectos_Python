
import pandas as pd


if __name__ == "__main__":

    # Steps

    # Read data from file
    train = pd.read_csv("./data/abstracts.csv")
    print(train.head())
    print(train.columns.tolist())

    #  Create X features (Dataframe)
    feature_cols = ['foodname', 'ab', 'rating1']
    X = train.loc[:, feature_cols]
    print(X.shape)
    print(type(X))

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(font_scale=1.5)
    countplt = sns.countplot(x='foodname', data=X , palette='hls')
    countplt.set_xticklabels(countplt.get_xticklabels(), rotation=90)
    plt.show()

    # Classified data for column foodname
    from sklearn.feature_extraction.text import CountVectorizer

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X[['ab']])
    print(X_train_counts)


    # Separate Train data and set data

    TRAIN_INPUT = list()
    TRAIN_OUTPUT = list()

    for index, row in countplt.iterrows():
        TRAIN_INPUT.append([row['foodname'],row['ab'] ])
        TRAIN_OUTPUT.append(row['rating1'])

    # Train the model (fit)

    from sklearn.linear_model import LinearRegression

    predictor = LinearRegression(n_jobs=-1)
    predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)


    # Test Data (predict)

