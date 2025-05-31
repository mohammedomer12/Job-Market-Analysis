import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/mohammedomer12/Job-Market-Analysis/main/jobdataset.csv')

# Streamlit app title
st.title('Job Market Analysis Dashboard')

# Preview dataset
st.write('### Data Preview')
st.dataframe(df.head())

# Top 10 Companies Based on Ratings and Reviews
st.write("### Top 10 Companies Based on Ratings and Reviews")

# Data preparation for the pie chart
filter = df.groupby(['company'])['reviews'].min().sort_values(ascending=False).head(10)
filter = filter.reset_index()
filter.columns = ['company', 'filter']

# Normalize the color values to range from 0 to 1
filter['color'] = (filter['filter'] - filter['filter'].min()) / (filter['filter'].max() - filter['filter'].min())

# Create an interactive pie chart with Plotly
fig = px.pie(
    filter,
    values='filter',
    names='company',
    title='Top 10 Companies Based on Ratings and Reviews',
    color='color',
    color_discrete_sequence=px.colors.sequential.Blues_r,
    hover_data=['filter']
)

# Update layout for better appearance
fig.update_layout(
    title_font_family="monospace",
    title_x=0.5,
    margin=dict(t=80, b=20, l=20, r=20),
    showlegend=True
)

# Make the chart interactive
fig.update_traces(
    textposition='outside',
    textinfo='percent',
    hoverinfo='label+percent+value',
    pull=[0.05 if i == 0 else 0 for i in range(len(filter))]
)

# **Use Streamlit to Display Plotly Chart**
st.plotly_chart(fig)


st.write("### Skills needed for almost all the jobs")
skills_df_1 = df['resposibilities'].str.lower().str.split(',').explode().value_counts().head(15)
skills_df_1 = skills_df_1.reset_index()
skills_df_1.columns = ['skills', 'count']
fig = px.bar(skills_df_1 , x = 'skills', y = 'count', title = 'Most demanding skills across all the job roles' , color = 'count', labels = {'count': 'count of occurances'}, color_continuous_scale=px.colors.sequential.Blues)
st.plotly_chart(fig)

st.write('### Skills needed to get hired into HDFC bank')
df_hdfc = df[df['company'] == 'Hdfc Bank']
# Process the data
responsibilities_counts = df_hdfc['resposibilities'].str.lower().str.split(',').explode().value_counts().head(10)
skills_df_2 = responsibilities_counts.reset_index()
skills_df_2.columns = ['skills', 'count']
fig = px.bar(skills_df_2,x = 'skills', y= 'count', title = 'skills needed for getting hired in HDFC', labels = {'Count': 'Count of occurences'}, color = 'count', color_continuous_scale = px.colors.sequential.Blues)
st.plotly_chart(fig)
######
st.write('### Skills needed to get hired as a Data analyst')
df_data_analyst = df[df['job_role'] == 'Data Analyst']
data_analyst_skills = df_data_analyst['resposibilities'].str.lower().str.split(',').explode().value_counts().head(10)
values = data_analyst_skills.values
index = data_analyst_skills.index

# Create a DataFrame from your data
skills_df = pd.DataFrame({
    'Skill': index,
    'Count': values
})

# Create an interactive pie chart with Plotly
fig = px.pie(
    skills_df, 
    values='Count', 
    names='Skill',
    color_discrete_sequence=px.colors.sequential.Blues_r,  # Using blues color scheme
    hover_data=['Count']  # Show count on hover
)

# Update layout for better appearance
fig.update_layout(
    title_font_family="monospace",
    title_x=0.5,  # Center the title
    margin=dict(t=80, b=20, l=20, r=20)
)

# Make the chart interactive with labels outside and percentages inside
fig.update_traces(
    textposition='outside',  # Put labels outside
    textinfo='percent',      # Show only percentages inside
    hoverinfo='label+percent+value',
    pull=[0.05 if i == 0 else 0 for i in range(len(index))]  # Pull out the first slice slightly
)

# Add the labels to the legend instead of on the pie
fig.update_layout(showlegend=True)

st.plotly_chart(fig)


st.write('### Years of experience vs Number of Jobs')

experience = []
job_counts = []
for exp in range(0,32):
    experience.append(exp)
    job_counts.append(len(df[(df['max_exp'] >= exp) & (df['min_exp'] <= exp)]))

#create the plot
fig , ax = plt.subplots(figsize=(12,8))
ax.bar(experience, job_counts, color = 'blue')
ax.set_xlabel("years of experience")
ax.set_ylabel('Number of Jobs')

ax.grid(True)

st.pyplot(fig)
##
st.write('### Average Salary by every company')
df['min_salary'] = df['min_salary'].replace('MBA/PGDM', 'Not disclosed')
new_df = df[(df['min_salary'] != 'Not disclosed') & (['max_salary'] != 'Not disclosed')]
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Assuming new_df is already defined and contains the relevant data
# Convert 'min_salary' to integer
new_df['min_salary'] = new_df['min_salary'].astype(int)

# Calculate the average minimum salary by company
top_companies = new_df.groupby('company')['min_salary'].mean().sort_values(ascending=False).reset_index().head(10)
top_companies.columns = ['company', 'salary']

# Plotting the results
fig = px.bar(top_companies, 
             x='company', 
             y='salary',  
             labels={'salary': 'Average Salary'}, 
             color='salary', 
             color_continuous_scale=px.colors.sequential.Blues)  # Use continuous color scale

# Update layout for better appearance
fig.update_layout(
    title_font_family="monospace",
    title_x=0.5,  # Center the title
    margin=dict(t=80, b=20, l=20, r=20)
)

st.plotly_chart(fig)

st.write('Companies Preffered locations')
# Assuming 'df' is your DataFrame and 'clean_location' is a column in it
locations = df['clean_location'].explode().value_counts().head(20).reset_index()
locations.columns = ['location', 'count']

# Process each location
for i in locations.index:
    location = locations.at[i, 'location']
    
    # Convert to lowercase
    location = location.lower()
    
    # Replace specific values
    location = location.replace('bengaluru', 'bangalore')  # Replace 'bengaluru' with 'bangalore'
    location = location.replace('-', ' ')  # Replace hyphens with a space (or remove them)
    
    # Update the DataFrame with the modified location
    locations.at[i, 'location'] = location.strip()  # Strip any leading/trailing whitespace

# Remove rows with blank locations
locations = locations[locations['location'] != '']
locations = locations.groupby('location', as_index=False).sum()
locations = locations.reset_index(drop = True)

locations = locations.reset_index(drop = True)
locations = locations.sort_values(by = 'count', ascending = False)
fig = px.bar(locations , x = 'location' , y = 'count' ,labels = {'count': 'count'}, title = 'Companies preferred location', color = 'count',color_continuous_scale = px.colors.sequential.Blues)
st.plotly_chart(fig)


st.markdown("""
- 📈 **Peak Demand:** Candidates with **4-6 years of experience**, especially **5 years**, are highly sought after.
- 🎯 **Early-Career Professionals:** Jobs requiring **0-3 years** show strong demand, offering great opportunities.
- 🔄 **Mid-Level Positions Dominate:** Demand gradually decreases **after 6 years**, favoring mid-tier roles.
- 🏆 **Senior & Leadership Roles:** Positions for **15+ years of experience** exist but are significantly limited.
""")

st.write("## Conclusion")
st.markdown("""
The job market is centered around **mid-level experience**, with **early-career roles** also in demand. 
Professionals should focus on **skill development within the 4-6 year window** to leverage maximum job opportunities.
""")