# This is so you can run the model independant of the app, which is useful for debugging / creating reports etc

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from app.model import g, Trial

#overwrite g class - so its easy to play around with
g.ed_inter_visit = (1440 / 38) # convert daily arrivals into inter-arrival time
g.number_of_nelbeds = 320
g.mean_time_in_bed = (225 * 60) # convert hrs to minutes
g.sd_time_in_bed = (405 * 60) # convert hrs to minutes
g.sim_duration = (60 * 24 * 60) # convert days into minutes
g.warm_up_period = (60 * 24 * 60)
g.number_of_runs = 10

# Call the run_trial method of our Trial object
all_event_logs, patient_df, patient_df_nowarmup, run_summary_df, trial_summary_df = Trial().run_trial()

display(all_event_logs.head(1000))
display(all_event_logs.tail(1000))
display(patient_df.tail(1000))
display(run_summary_df.head(100))
display(trial_summary_df.head(100))


###################DIAGNOSTIC PLOTS#############################

#####Number of beds occupied

minutes = pd.Series(range(0, g.sim_duration + g.warm_up_period))

run0_df = patient_df[patient_df['run'] == 0]
beds = ((run0_df["admission_begins"].values[:, None] < minutes.values) &
        ((run0_df["admission_complete"].values[:, None] > minutes.values) |
         run0_df["admission_complete"].isna().values[:, None])).sum(axis=0)

beds_df = pd.DataFrame({"minutes": minutes, "beds": beds})

fig = px.line(beds_df, x = "minutes", y = "beds")

fig.add_hline(y=434, line_dash="dash", line_color="lightblue",
              opacity=0.5, 
              annotation_text="max. beds", 
              annotation_position="top left")

fig.update_layout(template="plotly_dark")

fig.show()



