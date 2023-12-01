import streamlit as st
import pandas as pd
import os,sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader


data_loader  = SlackDataLoader



slack_data = data_loader.slack_parser('../data/all-week5/')


data_loader = SlackDataLoader
for week in range(1, 13):
    week_channel_variable_name = f'week{week}_channel'
    week_path = f'../data/all-week{week}/'

    globals()[week_channel_variable_name] = data_loader.slack_parser(week_path)

weeks = [week1_channel, week2_channel, week3_channel, week4_channel, week5_channel, week6_channel, week7_channel, week8_channel, week9_channel, week10_channel, week11_channel, week12_channel]

for i, week in enumerate(weeks, start=1):
    week['channel'] = i

concated_data = pd.concat(weeks, ignore_index=True)


# Top 10 users by replaying
top_10_replaying_users = slack_data.groupby('sender_name')['reply_count'].sum().nlargest(10)

# Convert Series to DataFrame and reset the index
top_10_dataframe = top_10_replaying_users.reset_index(name='reply_count')
# st.text('week7 channel')
st.text('Top 10 users by replaying count')

# Bar chart
st.bar_chart(top_10_dataframe.set_index('sender_name'))


# Bottom 10 users by replaying

bottom_10_replaying_users = slack_data.groupby('sender_name')['reply_count'].sum().nsmallest(10)


bottom_10_dataframe = bottom_10_replaying_users.reset_index(name='reply_count')

st.text('Bottom 10 users by replaying count')

# Bar chart
st.bar_chart(bottom_10_dataframe.set_index('sender_name'))



# Top 10  users by mention
top_10_mention_users = slack_data.groupby('sender_name')['msg_content'].apply(lambda x: x.str.count('@').sum()).nlargest(10)

# Convert Series to DataFrame and reset the index
top_10_mention_dataframe = top_10_mention_users.reset_index(name='msg_content')

st.text('Top 10 users by mention')

# Bar chart
st.bar_chart(top_10_mention_dataframe.set_index('sender_name'))


# Bottom 10  users by mention
bottom_10_mention_users = slack_data.groupby('sender_name')['msg_content'].apply(lambda x: x.str.count('@').sum()).nsmallest(10)

# Convert Series to DataFrame and reset the index
bottom_10_mention_dataframe = bottom_10_mention_users.reset_index(name='msg_content')

st.text('Bottom 10 users by mention')

# Bar chart
st.bar_chart(bottom_10_mention_dataframe.set_index('sender_name'))




# Top 10  users by message count
top_10_message_users = slack_data['sender_name'].value_counts().nlargest(10)


# Convert Series to DataFrame and reset the index
top_10_message_dataframe = top_10_message_users.reset_index(name='msg_content')

st.text('Top 10  users by message count')

# Bar chart
st.bar_chart(top_10_message_dataframe.set_index('sender_name'))



# Bottom 10 users by message count
bottom_10_message_users = slack_data['sender_name'].value_counts().nsmallest(10)


# Convert Series to DataFrame and reset the index
bottom_10_message_count_dataframe = bottom_10_message_users.reset_index(name='msg_content')

st.text('Bottom 10  users by message count')

# Bar chart
st.bar_chart(bottom_10_message_count_dataframe.set_index('sender_name'))


# Top 10  users by reaction count
top_10_reaction_users = slack_data.groupby('sender_name')['reply_users_count'].sum().nlargest(10)


# Convert Series to DataFrame and reset the index
top_10_reaction_users_dataframe = top_10_reaction_users.reset_index(name='reaction_count')

st.text('Top 10 users by reaction count')

# Bar chart
st.bar_chart(top_10_reaction_users_dataframe.set_index('sender_name'))


# Bottom 10  users by reaction count

bottom_10_reaction_users = slack_data.groupby('sender_name')['reply_users_count'].sum().nsmallest(10)



# Convert Series to DataFrame and reset the index
bottom_10_reaction_users_dataframe = bottom_10_reaction_users.reset_index(name='reaction_count')

st.text('Bottom 10  users by reaction count')

# Bar chart
st.bar_chart(bottom_10_reaction_users_dataframe.set_index('sender_name'))


# Which channel has the highest activity?

# from week 1 up to week 12 channel

channel_activity = concated_data.groupby('channel').agg({
    'msg_content': 'count',
    'reply_count': 'sum',
    'reply_users_count': 'sum'
}).reset_index()

channel_activity['replies_and_reactions'] = channel_activity['reply_count'] + channel_activity['reply_users_count']

most_active_channel = channel_activity.loc[channel_activity['replies_and_reactions'].idxmax()]

st.write('Which channel has the highest activity? i use from week 1 up to week 12 channel')
# Create a scatter chart using Streamlit
st.scatter_chart(
    channel_activity,
    x='msg_content',
    y='replies_and_reactions',
    color='msg_content',
    size='replies_and_reactions',
)

# Print the most active channel
st.write(f"The most highest activity is on channel: {most_active_channel['channel']}")


