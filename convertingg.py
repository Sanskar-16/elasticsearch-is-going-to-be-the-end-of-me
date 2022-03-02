import pandas as pd

df = pd.DataFrame(pd.read_csv("wiki_movie_plots_deduped.csv"))

df.head()

df2 = df[:1000]

df2.to_json("new_generated_file.json",
            orient="records",
            date_format="epoch",
            double_precision=10,
            force_ascii=True,
            date_unit="ms",
            default_handler=None)
