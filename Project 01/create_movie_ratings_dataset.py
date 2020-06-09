import pandas as pd
import numpy as np
#
# For this assignment, we need a movie data set. In order to mimic real data, we generated our random data set.
# It's a 16 x 7 Pandas data frame with movie ratings, randomly selected from the List numberList.
# Some may be rated as "?" (as it was in the instructions video https://www.youtube.com/playlist?list=PLuKhJYywjDe96T2L0-zXFU5Up2jqXlWI9),
# which means not rated. The data frame contains movies as heading, and users as index.
#
# After creating movie_ratings.csv, it was uploaded to git hub. Subsequent to this, the main program, movie_ratings.py will read it from github.
# So, although execution of this is program is a one time task, inadvertent multiple executions will not mutilate the actual movie_ratings.csv
# that will be used.
#
numberList = ["?", 1, 2, 3, 4, 5]
np.random.seed(123)
movie_ratings_df = pd.DataFrame(np.random.choice(numberList, size = (16, 7)),
                  columns = list(['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07']),
                  index = ['U01', 'U02', 'U03', 'U04', 'U05', 'U06', 'U07', 'U08', 'U09', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16'])
#
print()
print(movie_ratings_df)
movie_ratings_df.to_csv('./movie_ratings.csv')
#
# Build up of movie_test_df, which will contain test data set. In the instructions YouTube video they did not split the given
# movie data set, but arbitrarily selected cells from the given movie data set. We'll also mimic the same procedure. So, we need to
# identify an arbitrary set of cell locations as test data cells. In order to achieve that, I created a data frame movie_test_df,
# having the dimensions of movie_ratings_df, but filled with random True and False values, with a 25% probability of True-cells.
#
# We'll move elements from movie_ratings_df to only True-cells of movie_test_df (including "?"). Rest of the data in movie_ratings_df
# will go to the train data set, called movie_train_df. In the train data set, we'll mark the cells that went to movie_test_df with "-",
# to distinguish from the pre-existing "?". The movie_ratings_df data will be split into movie_train_df and movie_test_df, on a 75/25
# basis.
#
# After creation, movie_test_df.csv was uploaded to git hub. The main program will read it from github.
#
rows, columns = movie_ratings_df.shape
probability = 0.25    # setting probability for selecting Test data set at 25% of train data set.
movie_test_df = pd.DataFrame(np.random.choice(a = [True, False], size = (rows, columns), p = [probability, 1 - probability]),
                             columns = list(movie_ratings_df.columns.values),
                             index = list(movie_ratings_df.index.values))
#
print()
print(movie_test_df)
movie_test_df.to_csv('./movie_test_df.csv')
