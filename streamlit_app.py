import streamlit as st
# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT app_name, percentile_95 FROM hours_played_95_perc ORDER BY percentile_95 DESC LIMIT 10;', ttl="10m")
st.header('These are the games with the highest 95th percentile in terms of hours played by English-speaking reviewers', divider='rainbow')
# Print results.
st.bar_chart(data=df, x="app_name", y="percentile_95")


df = conn.query('SELECT app_name, percentile_95 FROM hours_played_95_perc ORDER BY percentile_95 ASC LIMIT 10;', ttl="10m")
st.header('These are the games with the lowest 95th percentile in terms of hours played by English-speaking reviewers', divider='rainbow')
# Print results.
st.bar_chart(data=df, x="app_name", y="percentile_95")