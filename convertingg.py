import kaggle
import pandas as pd

kaggle.api.authenticate()

kaggle.api.dataset_download_files('jrobischon/wikipedia-movie-plots', path="downloaded_file", unzip=True)

filename = "downloaded_file/wiki_movie_plots_deduped.csv"

df = pd.DataFrame(pd.read_csv(filename))

df.head()

df2 = df[:1000]

df2.to_json("new_generated_file.json",
            orient="records",
            date_format="epoch",
            double_precision=10,
            force_ascii=True,
            date_unit="ms",
            default_handler=None)
