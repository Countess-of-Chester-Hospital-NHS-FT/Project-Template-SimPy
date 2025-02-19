import pandas as pd
import numpy as np
from vidigi.prep import reshape_for_animations, generate_animation_df
from vidigi.animation import generate_animation
from model import g
#from model import Trial #for debugging


def animate(logs):
    STEP_SNAPSHOT_MAX = g.number_of_nelbeds * 1.1 # ensure this exceeds number of beds
    LIMIT_DURATION = g.warm_up_period + 10110
    WRAP_QUEUES_AT = 15
    X_TIME_UNITS = 30

    reshaped_logs = reshape_for_animations(
    event_log=logs[logs['run']==0],
    every_x_time_units=X_TIME_UNITS,
    step_snapshot_max=STEP_SNAPSHOT_MAX,
    limit_duration=LIMIT_DURATION,
    debug_mode=True
    )

    event_position_df = pd.DataFrame([
                    {'event': 'arrival',
                     'x':  -20, 'y': 200,
                     'label': "Arrival" },

                     {'event': 'admission_wait_begins',
                     'x':  205, 'y': 75,
                     'label': "Waiting for Admission"},

                    {'event': 'admission_begins',
                     'x':  505, 'y': 75,
                     'resource':'number_of_nelbeds',
                     'label': "Admitted"},

                    {'event': 'exit',
                     'x':  670, 'y': 70,
                     'label': "Exit"}

                ])
    

    # Add an admission wait for each patient that doesn't have one (so they all go via the waiting area)
    first_step = reshaped_logs.sort_values(["patient", "minute"], ascending=True) \
                    .groupby(["patient"]) \
                    .head(1)

    first_step['minute'] = first_step['minute'] - X_TIME_UNITS
    first_step['event'] = 'admission_wait_begins'
    first_step['event_type'] = "queue"

    reshaped_logs2 = pd.concat([reshaped_logs, first_step], ignore_index=True)

    # Add an arrival step for each patient (so that they arrive through the right 'door')
    first_step = reshaped_logs2.sort_values(["patient", "minute"], ascending=True) \
                    .groupby(["patient"]) \
                    .head(1)

    first_step['minute'] = first_step['minute'] - X_TIME_UNITS
    first_step['event'] = 'arrival'
    reshaped_logs2 = pd.concat([reshaped_logs2, first_step], ignore_index=True)

    # add co-ordinates to the logs
    position_logs = generate_animation_df(full_patient_df=reshaped_logs2,
                                                    event_position_df=event_position_df,
                                                    wrap_queues_at=WRAP_QUEUES_AT,
                                                    step_snapshot_max=STEP_SNAPSHOT_MAX,
                                                    gap_between_entities=10, # need this and resource gap to be consistent
                                                    gap_between_resources=10, # if changing this, also need to specify in generate_animation 
                                                    gap_between_rows=30, # if changing this, also need to specify in generate_animation  
                                                    debug_mode=True
                                                    )

        #changes the exit point for reneged patients (if there are any)
    position_logs['x_final'] = np.where((position_logs['event'] == "exit") & (position_logs['event_type'] == "queue"), 150, position_logs['x_final'])
    position_logs['y_final'] = np.where((position_logs['event'] == "exit") & (position_logs['event_type'] == "queue"), 0, position_logs['y_final'])
    position_logs['y_final'] = np.where((position_logs['event'] == "exit") & (position_logs['event_type'] == "resource_use"), 450, position_logs['y_final'])
    position_logs['x_final'] = np.where((position_logs['event'] == "exit") & (position_logs['event_type'] == "resource_use"), 650, position_logs['x_final'])

    filtered_position_logs = position_logs[(position_logs['minute'] > g.warm_up_period) & (position_logs['minute'] < g.warm_up_period + 10080)] # run for 1 week after warmup
    
    animation = generate_animation(
        full_patient_df_plus_pos=filtered_position_logs.sort_values(['patient', 'minute']),
        event_position_df= event_position_df,
        scenario=g(),
        debug_mode=False,
        setup_mode=False, # turns on and off gridlines
        include_play_button=True,
        icon_and_text_size= 16,
        plotly_height=800,
        frame_duration=600,
        frame_transition_duration=600,
        plotly_width=1500,
        override_x_max=600,
        override_y_max=900,
        time_display_units="dhm",
        start_date="2025-02-06 00:00",
        display_stage_labels=False,
        custom_resource_icon='⚬',
        add_background_image="img/animation_background.png"
    )

    return animation#, filtered_position_logs, position_logs, reshaped_logs2, reshaped_logs # hashed out for debugging

# For debugging
# all_event_logs, patient_df, patient_df_nowarmup, run_summary_df, trial_summary_df = Trial().run_trial()
# animation, filtered_position_logs, position_logs, reshaped_logs2, reshaped_logs = animate(all_event_logs)
# display(filtered_position_logs)
# display(position_logs)
# display(reshaped_logs2)
# display(reshaped_logs)
# display(animation)