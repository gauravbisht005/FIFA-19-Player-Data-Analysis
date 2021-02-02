import pandas as pd
import seaborn as sns
import streamlit as st
import altair as alt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('FIFA 19 Player Data Analysis')

st.markdown("""FIFA19 is the official football game of EA Sports. Queries in the following project are based on the 
Player Dataset of FIFA19. This Dataset is available in Kaggle which is a hub of datasets. This dataset consists of 
details of players and their stats in the year 2019. This can be used to determine success ratio, ratings, top players 
etc.""")

# read DF
uploaded_file = st.file_uploader("Select FIFA19 Dataset")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# DataFrame - map                                                South & West are negative(-ve)
lat_lon_map = [['Argentina', -38.4161, -63.6167], ['Portugal', 39.3339, -8.2245], ['Brazil', -14.2350, -51.9253],
               ['Spain', 40.4637, -3.7492], ['Belgium', 50.5039, 4.4699], ['Croatia', 45.1000, 15.2000], ['Uruguay',
                                                                                                          -32.5228,
                                                                                                          -55.7658],
               ['Slovenia', 46.1512, 14.9955], ['Poland', 51.9194, 19.1451], ['Germany', 51.1657, 10.4515], ['France',
                                                                                                             46.2276,
                                                                                                             2.2137],
               ['England', 52.3555, -1.1743], ['Italy', 41.8719, 12.5674], ['Egypt', 26.8206, 30.8025], ['Colombia',
                                                                                                         4.5709,
                                                                                                         -74.2973],
               ['Denmark', 56.2639, 9.5018], ['Gabon', -0.8037, 11.6094], ['Wales', 52.1307, -3.7837], ['Senegal',
                                                                                                        14.4974,
                                                                                                        -14.4524],
               ['Costa Rica', 9.7489, -83.7534], ['Slovakia', 48.6690, 19.6990], ['Netherlands', 52.1326, 5.2913], [
                   'Bosnia Herzegovina', 43.9159, 17.6791], ['Morocco', 31.7917, -7.0926], ['Serbia', 44.0165, 21.0059],
               ['Algeria', 28.0339, 1.6596], ['Austria', 47.5162, 14.5501], ['Greece', 39.0742, 21.8243], ['Chile',
                                                                                                           -35.6751,
                                                                                                           -71.5430], [
                   'Sweden', 60.1282, 18.6435], ['Korea Republic', 35.9078, 127.7669], ['Finland', 61.9241, 25.7482],
               ['Guinea', 9.9456, -9.6966],
               ['Montenegro', 42.7087, 19.3744], ['Armenia', 40.0691, 45.0382], ['Switzerland', 46.8182, 8.2275],
               ['Norway', 60.4720, 8.4689], ['Czech Republic', 49.8175, 15.4730], ['Scotland', 56.4907, -4.2026],
               ['Ghana', 7.9465, -1.0232], ['Central African Republic', 6.6111, 20.9394],
               ['DR Congo', -4.0383, 21.7587],
               ['Ivory Coast', 7.5400, -5.5471], ['Russia', 61.5240, 105.3188], ['Ukraine', 48.3794, 31.1656],
               ['Iceland', 64.9631, -19.0208], ['Mexico', 23.6345, -102.5528], ['Jamaica', 18.1096, -77.2975],
               ['Albania', 41.1533, 20.1683], ['Venezuela', 6.4238, -66.5897], ['Japan', 36.2048, 138.2529], ['Turkey',
                                                                                                              38.9637,
                                                                                                              35.2433],
               ['Ecuador', -1.8312, -78.1834], ['Paraguay', -23.4425, -58.4438], ['Mali', 17.5707, -3.9962], ['Nigeria',
                                                                                                              9.0820,
                                                                                                              8.6753],
               ['Cameroon', 7.3697, 12.3547], ['Dominican Republic', 18.7357, -70.1627], ['Israel', 31.0461, 34.8516],
               ['Kenya', -0.0236, 37.9062], ['Hungary', 47.1625, 19.5033], ['Republic of Ireland', 53.4129, -8.2439],
               ['Romania', 45.9432, 24.9668], ['United States', 36.1671, -115.0602], ['Cape Verde', 16.5388, -23.0418],
               ['Peru', -9.1900, -75.0152], ['Togo', 8.6195, 0.8248], ['Syria', 34.8021, 38.9968], ['Zimbabwe', -19.0154
                                                                                                    , 29.1549],
               ['Burkina Faso', 12.2383, -1.5616], ['Tunisia', 33.8869, 9.5375], ['FYR Macedonia', 41.6086, 21.7453],
               ['United Arab Emirates', 23.4241, 53.8478], ['China PR', 35.8617, 104.1954], ['Guinea Bissau', 11.8037,
                                                                                             -15.1804], ['Kosovo',
                                                                                                         42.6026,
                                                                                                         20.9030],
               ['South Africa', -30.5595, 22.9375], ['Madagascar', -18.7669, 46.8691], ['Georgia', 32.1656, -82.9001],
               ['Gambia', 13.4432, -15.3101], ['Cuba', 21.5218, -77.7812], ['Iran', 32.4279, 53.6880], ['Belarus',
                                                                                                        53.7098,
                                                                                                        27.9534],
               ['Uzbekistan', 41.3775, 64.5853], ['Mozambique', -18.6657, 35.5296], ['Honduras', 15.2000, -86.2419],
               ['Canada', 56.1304, -106.3468], ['Australia', -25.2744, 133.7751], ['New Zealand', -40.9006, 174.8860],
               ['Bulgaria', 42.7339, 25.4858]]
map_dataframe = pd.DataFrame(lat_lon_map, columns=['Country', 'latitude', 'longitude'])

# DataFrame - Overall to Number of players
overall_df = df['Overall'].value_counts().reset_index()
overall_df.columns = ['Overall', 'Count']
overall_df = overall_df.set_index('Overall')

# DataFrame - Potential to Number of Players
potential_df = df['Potential'].value_counts().reset_index()
potential_df.columns = ['Potential', 'Count']
potential_df = potential_df.set_index('Potential')

# data cleaning - dropping columns
df.drop(['ID', 'Photo', 'Flag', 'Club Logo', 'Special', 'Real Face'], axis=1, inplace=True)


# data cleaning - changing type
def value_and_wage_conversion(value):
    out = value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))
    elif 'K' in value:
        out = float(out.replace('K', ''))
    return float(out)


df['Value'] = df['Value'].apply(lambda x: value_and_wage_conversion(x))
df['Wage'] = df['Wage'].apply(lambda x: value_and_wage_conversion(x))

# checkbox - to view DF
is_check = st.checkbox("See Dataframe")
if is_check:
    st.write(df)

# Header
st.header("Few insights on data:")

# checkbox - to view map
show_map_is_check = st.checkbox("See Nations of players:")
if show_map_is_check:
    st.map(map_dataframe)

# checkbox - to see age distribution of players
age_is_check = st.checkbox("See age distribution of players:")
if age_is_check:
    sns.countplot(y='Age', data=df, palette='Set1')
    st.pyplot()

# checkbox - Number of players by Overall
overall_chart_is_check = st.checkbox("See No. of Players per Overall:")
if overall_chart_is_check:
    sns.lineplot(data=overall_df, x='Overall', y='Count')
    st.pyplot()

# checkbox - Number of players by Potential
potential_is_check = st.checkbox("See No. of Players per Potential:")
if potential_is_check:
    sns.lineplot(data=potential_df, x='Potential', y="Count")
    st.pyplot()

# checkbox - Preferred Foot
preferred_foot_is_check = st.checkbox("See Preferred Foot of players:")
if preferred_foot_is_check:
    sns.countplot('Preferred Foot', data=df)
    st.pyplot()

# checkbox - Work Rate
work_rate_is_check = st.checkbox("See Work Rate of players:")
if work_rate_is_check:
    sns.countplot(y='Work Rate', data=df)
    st.pyplot()

# checkbox - to view body type
body_type_is_check = st.checkbox("See body type of players:")
if body_type_is_check:
    sns.countplot('Body Type', data=df)
    st.pyplot()

# checkbox - Number of players by position
position_chart_is_check = st.checkbox("See No. of Players per position:")
if position_chart_is_check:
    sns.countplot(y='Position', data=df, palette="Set1")
    st.pyplot()

# checkbox - heatmap
heatmap_is_check = st.checkbox("See heatmap of Correlation between Attributes:")
if heatmap_is_check:
    sns.heatmap(df.corr(), vmin=0, vmax=1)
    st.pyplot()

# Header
st.header("Individual/ Multiple player stats:")

# sidebar - to select teams/ clubs
teams = st.sidebar.multiselect("Select Clubs:", df['Club'].unique())
# st.write("Clubs Selected: ", teams)

# sidebar - to select attributes
attributes = st.sidebar.multiselect("Select Attributes:", df.columns)
# st.write("Attributes Selected:", attributes)

# canvas - to view table of selected clubs
selected_club_data = df[(df['Club'].isin(teams))]
two_clubs_data = selected_club_data[attributes]

# checkbox - to view selected clubs
club_data_is_check = st.checkbox("Attributes of selected clubs:")
if club_data_is_check:
    st.write(two_clubs_data)

# sidebar - to select players
selected_players = st.sidebar.multiselect('Select players to compare:', two_clubs_data['Name'].unique())
# st.write("Players Selected:", selected_players)

# checkbox - to view table of selected players
player_data_is_check = st.checkbox("Data of selected players:")
if player_data_is_check:
    plot_data = two_clubs_data[(two_clubs_data['Name']).isin(selected_players)]
    st.write(plot_data)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Age", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Overall", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Potential", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Value", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Wage", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Preferred Foot", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Work Rate", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Body Type", y="Name", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Age", y="Overall", color="Name")
    )
    st.write(chart)
    chart = (
        alt.Chart(plot_data, width=670).mark_bar().encode(x="Potential", y="Overall", color="Name")
    )
    st.write(chart)
    sns.barplot(x="Overall", y="Potential", hue="Name", data=df)
    st.pyplot()
