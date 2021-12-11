import pandas as pd
import numpy as np
from collections import Counter
from scipy import stats
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import sys

#for ML
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

def genres(df):
  unique_artists = df["Artist_Name"].unique()

  primary_genres = ["pop","rap","country","latin","dance","r&b","alternative"]

  n_df = pd.DataFrame()
  #artist_overall_genre = []
  for artist in unique_artists:
    sub_df = df[df["Artist_Name"] == artist].copy()
    n_songs = len(sub_df)
    sub_df.reset_index(drop = True,inplace = True)
    genres = sub_df.at[0,"Genres"]

    #processing each genre list to match one of the primary genres
    try:
      genres = genres.split("**")
    except:
      artist_overall_genre.append("manual look up")
      continue

    genres_list = []
    #print(genres)
    #split into primary category
    for i in genres:
      
      if i == "hip hop":
        i = "hip-hop"

      if " " in i:          #if genre has a prefix, perform this operation
        result = i.split(" ")[1]
        genres_list.append(result)
      else:
        genres_list.append(i)

    #take max of genre as artist genre
    max_genre = max(genres_list, key = genres_list.count)
    artist_overall_genre = max_genre
    artist_overall_genre = list((artist_overall_genre,) * n_songs)
    sub_df["n_Genres"] = artist_overall_genre

    n_df = pd.concat([n_df,sub_df],ignore_index=True)


  #work on conditionals:
  n_df.loc[n_df.n_Genres == "hip-hop", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "hip", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "trap", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "rouge", "n_Genres"] = "rap"
  n_df.loc[n_df.Artist_Name == "Chris Brown", "n_Genres"] = "r&b"
  n_df.loc[n_df.Artist_Name == "Nicki Minaj", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "drill", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "americana", "n_Genres"] = "contry"
  n_df.loc[n_df.n_Genres == "k-pop", "n_Genres"] = "pop"
  n_df.loc[n_df.n_Genres == "k-rap", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "coast", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "brostep", "n_Genres"] = "dance"
  n_df.loc[n_df.n_Genres == "house", "n_Genres"] = "dance"
  n_df.loc[n_df.n_Genres == "bachata", "n_Genres"] = "latin"
  n_df.loc[n_df.n_Genres == "carolina", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "room", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "rican", "n_Genres"] = "latin"
  n_df.loc[n_df.n_Genres == "edm", "n_Genres"] = "dance"
  n_df.loc[n_df.n_Genres == "contemporary", "n_Genres"] = "r&b"
  n_df.loc[n_df.n_Genres == "reggaeton", "n_Genres"] = "latin"
  n_df.loc[n_df.n_Genres == "carioca", "n_Genres"] = "latin"
  n_df.loc[n_df.Artist_Name == "Rosalia", "n_Genres"] = "latin"
  n_df.loc[n_df.Artist_Name == "ROSALIA", "n_Genres"] = "latin"
  n_df.loc[n_df.n_Genres == "z", "n_Genres"] = "alternative"
  n_df.loc[n_df.Artist_Name == "Coldplay", "n_Genres"] = "pop"
  n_df.loc[n_df.Artist_Name == "WizKid", "n_Genres"] = "pop"
  n_df.loc[n_df.Artist_Name == "Tom MacDonald", "n_Genres"] = "country"
  n_df.loc[n_df.Artist_Name == "Avicii", "n_Genres"] = "dance"
  n_df.loc[n_df.n_Genres == "media", "n_Genres"] = "pop"
  n_df.loc[n_df.Artist_Name == "Jack Harlow", "n_Genres"] = "rap"
  n_df.loc[n_df.n_Genres == "ccm", "n_Genres"] = "alternative"
  n_df.loc[n_df.n_Genres == "metal", "n_Genres"] = "rock"
  n_df.loc[n_df.n_Genres == "indie", "n_Genres"] = "alternative"
  n_df.loc[n_df.Artist_Name == "Cochise", "n_Genres"] = "rap"
  n_df.loc[n_df.Artist_Name == "Cheat Codes", "n_Genres"] = "dance"
  n_df.loc[n_df.Artist_Name == "SHAED", "n_Genres"] = "dance"
  n_df.loc[n_df.Artist_Name == "Pardison Fontaine", "n_Genres"] = "rap"
  n_df.loc[n_df.Artist_Name == "Big Red Machine", "n_Genres"] = "alternative"
  n_df.loc[n_df.n_Genres == "contry", "n_Genres"] = "country"
  n_df.loc[n_df.n_Genres == "electropop", "n_Genres"] = "dance"
  n_df.loc[n_df.n_Genres == "folk", "n_Genres"] = "alternative"
  n_df.loc[n_df.n_Genres == "rock", "n_Genres"] = "alternative"
  n_df.loc[n_df.n_Genres == "disney", "n_Genres"] = "pop"
  n_df.loc[n_df.n_Genres == "road", "n_Genres"] = "country"
  

  n_df.drop(columns=["Genres"],inplace = True)
  return n_df

def discretize_fn(feature,col_values):

  if feature in ["danceability","energy","acousticness","valence","instrumentalness"]:    #variables are broken into two variables. less x and more x where x is feature
    n_vars = 1
    #low_feature = [1 if x < 0.5 else 0 for x in col_values]
    high_feature = [1 if x >= 0.5 else 0 for x in col_values]
    feature_set = high_feature

  elif feature == "liveness":
    n_vars = 1
    #low_feature = [1 if x < 0.8 else 0 for x in col_values]
    high_feature = [1 if x >= 0.8 else 0 for x in col_values]
    feature_set = high_feature

  elif feature == "speechiness":
    n_vars = 3
    low_feature = [1 if x < 0.33 else 0 for x in col_values]
    mid_feature = [1 if (x >= 0.33 and x < 0.66) else 0 for x in col_values]
    high_feature = [1 if x >= 0.66 else 0 for x in col_values]
    feature_set = (low_feature,mid_feature,high_feature)

  elif feature == "duration_ms":
    n_vars = 1
    col_values = col_values / 60000       #convert to minutes
    #low_feature = [1 if x < 3.50 else 0 for x in col_values]    #threshold based on mean song length
    high_feature = [1 if x >= 3.50 else 0 for x in col_values]
    feature_set = high_feature

  elif feature == "tempo":
    n_vars = 1
    #low_feature = [1 if x < 120 else 1 for x in col_values] #temp has wide range of classification put categorize moderate speed as threshold
    high_feature = [1 if x >= 120 else 0 for x in col_values]
    feature_set = high_feature

  elif feature == "mode":
    n_vars = 1
    #minor_mode = [1 if x == 0 else 0 for x in col_values]
    major_mode = col_values
    feature_set = major_mode

  elif feature == "n_Genres":
    n_vars = 7
    pop_genre = [1 if x =="pop" else 0 for x in col_vals]
    rap_genre = [1 if x =="rap" else 0 for x in col_vals]
    country_genre = [1 if x =="country" else 0 for x in col_vals]
    latin_genre = [1 if x =="latin" else 0 for x in col_vals]
    dance_genre = [1 if x =="dance" else 0 for x in col_vals]
    rb_genre = [1 if x =="r&b" else 0 for x in col_vals]
    alt_genre = [1 if x =="alternative" else 0 for x in col_vals]

    feature_set = (pop_genre,rap_genre,country_genre,latin_genre,dance_genre,rb_genre,alt_genre)
    
  return feature_set,n_vars

def discretize(n_df):
    #break into boolean variables
    feature_to_discretize = ["danceability","energy","acousticness","valence",
                            "instrumentalness","liveness","speechiness",
                            "duration_ms","tempo","mode","n_Genres"]

    for feature in feature_to_discretize:
        col_vals = n_df[feature].to_numpy()
        res,n_vars = discretize_fn(feature,col_vals)

        if (n_vars == 1) and (feature == "mode"):
            names = ["mode"]#["minor_","major_"]
        elif n_vars == 1:
            names = feature#["low_","high_"]
            
        elif n_vars == 3:
            names = ["low_","mid_","high_"]
        elif n_vars == 7:
            names = ["pop_genre","rap_genre","country_genre","latin_genre","dance_genre","r&b_genre","alt_genre"]
        
        if n_vars == 7:
            #print(res)
            for n in range(n_vars):
                n_df[names[n]] = res[n]

        elif n_vars == 3:
            #print(res)
            for n in range(n_vars):
                n_df[names[n] + feature] = res[n]

        else:
            n_df[names] = res

    n_df.drop(columns=["speechiness","n_Genres"],inplace = True)
    return n_df

#using samantha causal inference approach where we assume
#C is the cause being tested
#e is the effect - high chart position (>= 50)
#x is a variable that could be potential cause
#X is the set of all prima facie cause of e

def calc_causal_significance(e,c,x):
  '''p(e|c^x) - p(e|-c^x)'''

  p_e_cx = prob_cond_ext(e,c,x,1,1,1)  #p(e|c,x) -> num(e,c,x)/num(c,x)
  p_e__cx = prob_cond_ext(e,c,x,1,0,1) #p(e|-c,x) -> num(e,-c,x)/num(-c,x)

  return p_e_cx - p_e__cx

def prob_rv(rv,v1):
  return Counter(rv)[v1]/len(rv)

def prob_cond(rv1,rv2,v1,v2):
  d = {"rv1":rv1,"rv2":rv2}
  table = pd.DataFrame(data = d)

  table = table.loc[(table["rv2"] == v2) & (table["rv1"] == v1)].copy() #step one
  cond_prob = len(table)/len(rv1)

  return cond_prob

def prob_cond_ext(rv1,rv2,rv3,v1,v2,v3):
  d = {"rv1":rv1,"rv2":rv2,"rv3":rv3}
  table = pd.DataFrame(data = d)

  denominator = len(table.loc[(table["rv2"] == v2) & (table["rv3"] == v3)])
  numerator = len(table.loc[(table["rv1"] == v1) & (table["rv2"] == v2) & (table["rv3"] == v3)])

  try:
    cond_prob = numerator/denominator
  except:
    cond_prob = 0

  return cond_prob

def causal_inference(pre_2021,pre_outcome_variables):

    X = list(pre_2021.columns) #prima facie causes
    X.remove("instrumentalness")
    X.remove("liveness")
    e = pre_outcome_variables
    e_avg = {}          

    for c in X:
        c_val = pre_2021[c].to_numpy()
        X_c = X.copy()
        X_c.remove(c)

        if "_" in c:
            c_feature = c.split("_")
            if c_feature[1] == "ms":
                pass
            else:
                if c_feature[1] == "speechiness":
                    X_c = [x for x in X_c if not "speechiness" in x]
                
                elif c_feature[1] == "genre":
                    X_c = [x for x in X_c if not "genre" in x]
                
        print("Cause is {}".format(c))
        E_x = []

        for x in X_c:
            #print("X is {}".format(x))
            x_val = pre_2021[x].to_numpy()
            res = calc_causal_significance(e,c_val,x_val)
            E_x.append(res)

        e_avg[c] = E_x

    #calculate average causal significance for each cause
    mean_e_avg = {}
    for key,val in e_avg.items():
        mean_e_avg[key] = np.round(np.sum(val)/len(val),3)

    return mean_e_avg

def plot_e_avg(mean_e_avg):
    fig, ax = plt.subplots(figsize = (7,9),dpi = 120)
    plt.barh(list(mean_e_avg.keys()),list(mean_e_avg.values()))
    #ax.spines["left"].set_position("zero")
    ax.spines["right"].set_position("zero")
    ax.spines["top"].set_visible(False)
    #plt.yticks([])
    plt.xticks(fontsize = 17)
    plt.yticks(fontsize = 15)
    plt.xlabel("Average Causal Significance " r"$\varepsilon_{avg}(c,e)$",fontsize = 17)
    plt.tight_layout()

def evluation(pre_2021,post_2021,pre_outcome_variables,post_outcome_variables):

    y_train = pre_outcome_variables
    y_test = post_outcome_variables
    x_train = pre_2021
    x_test = post_2021

    x_train.drop(columns=["tempo","valence","dance_genre","pop_genre","acousticness","instrumentalness","liveness"], inplace = True)
    x_test.drop(columns=["tempo","valence","dance_genre","pop_genre","acousticness","instrumentalness","liveness"], inplace = True)

    clf = LogisticRegression(random_state=0).fit(x_train, y_train)
    y_predict = clf.predict_proba(x_test)
    print(roc_auc_score(y_test, clf.predict_proba(x_test)[:, 1]))
    

if __name__ == "main":

    data = sys.argv[1]

    df = pd.read_csv(data)      #load data
    df = df.sample(frac=1,random_state=10).reset_index(drop=True)
    outcome_variables = df["Position"].to_numpy()       #get outcomes variables
    debut_dict = Counter(outcome_variables)

    #process genres
    n_df = genres(df)
    n_df = discretize(n_df)
    
    #convert to datetime
    n_df["Date"] = pd.to_datetime(df["Date"])

    pre_2021 = n_df[n_df["Date"].dt.year != 2021].copy()
    post_2021 = n_df[n_df["Date"].dt.year == 2021].copy()

    pre_2021 = pre_2021.sample(random_state=10,frac = 1)
    post_2021 = post_2021.sample(random_state=10,frac = 1)

    post_2021 = post_2021.reset_index(drop = True)
    pre_2021 = pre_2021.reset_index(drop = True)

    pre_outcome_variables = pre_2021["Position"].to_numpy()
    post_outcome_variables = post_2021["Position"].to_numpy()
    pre_2021.drop(columns=["Position","Artist_Name","Date","time_signature","key","loudness"],inplace = True)    #drop outcome column and artist name
    post_2021.drop(columns=["Position","Artist_Name","Date","time_signature","key","loudness"],inplace = True)

    pre_outcome_variables = [0 if x<=50 else 1 for x in pre_outcome_variables] #discretize outcome variable [1,50],[51,100]
    post_outcome_variables = [0 if x<=50 else 1 for x in post_outcome_variables]

    e_avg = causal_inference(pre_2021,pre_outcome_variables)
    print(e_avg)

    #plot of average causal significance for each cause. generate results figure in the paper
    #plot_e_avg(e_avg)
    
    #evaluating caual effects using prediction task
    evluation(pre_2021,post_2021,pre_outcome_variables,post_outcome_variables)