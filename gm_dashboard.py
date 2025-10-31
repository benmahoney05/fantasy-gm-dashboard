import streamlit as st
from espn_api.football import League

# === CONFIG ===
LEAGUE_ID = 1140335890
YEAR = 2025
ESPN_S2 = 'AECnuIYBeFQqolXg04Yjv1LdgCNlsZd7eFpB5XbOHK6c2vVnl2wkF%2FrPBxyHwrwz2SylNBCD%2Bxyz9IWCBmkCl77pjwBi7JhDe%2BJC7LANrLnpftPmDbVTyyAnm4oWHkfYHQvxlqULZxORj%2B2dCNri9DWRNBlWMblY6cd1DLovOA6Pm7K4jg3OBLYJAe4A8ECiIJluFyXFhF1fDOEpEOrEcugFdoxGhB61hPxTwd8htbbNXtqUyrlKOZ5vZ1bgP5DLk%2BoiHkzXTV5bQBER2EBw5PC8AscT2xHXQN3F4mlNFjPReA%3D%3D'
SWID = '{102CE65F-359E-43A8-A1E4-404A7152B940}'

# === CONNECT TO LEAGUE ===
league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
teams = league.teams

st.set_page_config(page_title="AI GM Dashboard", layout="wide")
st.title("🧠 AI GM Control Panel")

# === SIDEBAR CONTROLS ===
st.sidebar.header("Move Player Between Teams")

team_names = [team.team_name for team in teams]
team_dict = {team.team_name: team for team in teams}

source_team_name = st.sidebar.selectbox("From Team", team_names)
target_team_name = st.sidebar.selectbox("To Team", team_names)

source_team = team_dict[source_team_name]
target_team = team_dict[target_team_name]

player_names = [player.name for player in source_team.roster]
selected_player_name = st.sidebar.selectbox("Player to Move", player_names)

if st.sidebar.button("Move Player"):
    player_obj = next(p for p in source_team.roster if p.name == selected_player_name)
    source_team.roster.remove(player_obj)
    target_team.roster.append(player_obj)
    st.sidebar.success(f"Moved {selected_player_name} from {source_team_name} to {target_team_name}")

# === DISPLAY TEAM ROSTERS ===
st.subheader("📋 Team Rosters")
cols = st.columns(len(teams))

for i, team in enumerate(teams):
    with cols[i]:
        st.markdown(f"### {team.team_name}")
        for player in team.roster:
            st.write(player.name)
