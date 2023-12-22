

import streamlit as st
from mplsoccer.pitch import VerticalPitch
import matplotlib.pyplot as plt


ratings={	"players":
    [
    {
	"Player": "Luke Shaw",
	"Position": "LB",
	"Mins": 1396,
	"Tackles": 1.1,
	"Inter": 0.8,
	"Fouls": 1.1,
	"Clear": 2.1,
	"Rating": 6.80,
	"Goals": 0,
	"Assists": 2,
	"KeyP": 1.3,
	"ThrB": 0.1,
	},
    {
	"Player": "Eberechi Eze",
	"Position": "CAM",
	"Mins": 886,
	"Rating": 7.28,
	"Goals": 2,
	"Assists": 3,
	"KeyP": 2,
	"ThrB": 0.3,
	},
	{
	"Player": "Fikayo Tomori",
	"Position": "LCB",
	"Mins": 1907,
    "Tackles": 2,
	"Inter": 1.3,
	"Fouls": 1,
	"Clear": 2.5,
	"Rating": 6.86,
	"Goals": 0,
	"Assists": 0,
	"KeyP": 0.1,
	"ThrB": 0,
    },
    {
	"Player": "Jude Bellingham",
	"Position": "LCM",
	"Mins": 2468,
	"Tackles": 2,
	"Inter": 1,
	"Fouls": 1,
	"Clear": 0.3,
	"Rating": 7.87,
	"Goals": 19,
	"Assists": 7,
	"KeyP": 1.7,
	"ThrB": 0.3,
	},
    {
	"Player": "Rico Lewis",
	"Position": "RB",
	"Mins": 980,
	"Tackles": 0.8,
	"Inter": 0.4,
	"Fouls": 0.6,
	"Clear": 0.3,
	"Rating": 6.55,
	"Goals": 1,
	"Assists": 2,
	"KeyP": 1.1,
	"ThrB": 0.2,
    },
    {
	"Player": "James Maddison",
	"Position": "CAM",
	"Mins": 1149,
	"Rating": 7.43,
	"Goals": 3,
	"Assists": 5,
	"KeyP": 2.6,
	"ThrB": 0.3,
    },
    {
	"Player": "Mason Mount",
	"Position": "CAM",
	"Mins": 814,
	"Rating": 6.4,
	"Goals": 0,
	"Assists": 1,
	"KeyP": 0.6,
	"ThrB": 0.1,
    },
    {
	"Player": "Kieran Trippier",
	"Position": "RB",
	"Mins": 2484,
	"Tackles": 1.6,
	"Inter": 0.7,
	"Fouls": 0.9,
	"Clear": 1.7,
	"Rating": 6.95,
	"Goals": 0,
	"Assists": 8,
	"KeyP": 1.9,
	"ThrB": 0.1,
	"Saves": 0
    },
    {
	"Player": "Declan Rice",
	"Position": "CDM",
	"Mins": 3085,
	"Tackles": 1.6,
	"Inter": 1.4,
	"Fouls": 0.6,
	"Clear": 1.2,
	"Rating": 6.90,
	"Goals": 4,
	"Assists": 2,
	"KeyP": 2,
	"ThrB": 0.1,
    },
    {
	"Player": "Ben Chilwell",
	"Position": "LB",
	"Mins": 608,
	"Tackles": 1,
	"Inter": 0.6,
	"Fouls": 1,
	"Clear": 0.6,
	"Rating": 6.69,
	"Goals": 0,
	"Assists": 1,
	"KeyP": 1.4,
	"ThrB": 0,
    },
    {
	"Player": "Cole Palmer",
	"Position": "RCM",
	"Mins": 1434,
	"Tackles": 0.7,
	"Inter": 0.5,
	"Fouls": 0.6,
	"Clear": 0.4,
	"Rating": 6.98,
	"Goals": 9,
	"Assists": 5,
	"KeyP": 1.4,
	"ThrB": 0.4,
    },
    {
	"Player": "Jordan Henderson",
	"Position": "CDM",
	"Mins": 379,
	"Tackles": 1,
	"Inter": 0.4,
	"Fouls": 0.1,
	"Clear": 0.1,
	"Rating": 6.87,
	"Goals": 1,
	"Assists": 2,
	"KeyP": 0.9,
	"ThrB": 0.1,
    },
    {
	"Player": "Trent Alexander-Arnold",
	"Position": "RB",
	"Mins": 1856,
	"Tackles": 1.2,
	"Inter": 1,
	"Fouls": 0.2,
	"Clear": 1.2,
	"Rating": 7.28,
	"Goals": 3,
	"Assists": 6,
	"KeyP": 2.2,
	"ThrB": 0.4,
    },
    {
	"Player": "Kyle-Walker",
	"Position": "RB",
	"Mins": 2889,
	"Tackles": 1,
	"Inter": 0.8,
	"Fouls": 0.7,
	"Clear": 1,
	"Rating": 6.75,
	"Goals": 1,
	"Assists": 2,
	"KeyP": 0.7,
	"ThrB": 0.1,
    },
    {
	"Player": "John Stones",
	"Position": "RCB",
	"Mins": 1384,
	"Tackles": 0.3,
	"Inter": 0.4,
	"Fouls": 0.4,
	"Clear": 1.2,
	"Rating": 7.10,
	"Goals": 0,
	"Assists": 0,
	"KeyP": 0.2,
	"ThrB": 0,
    },
    {
	"Player": "Jordan Pickford",
	"Position": "GK",
	"Mins": 3091,
	"Saves": 69,
	"GA": 20,
	"Clean": 7,
	"Rating": 6.75,
    },
    {
	"Player": "Nick Pope",
	"Position": "GK",
	"Mins": 1200,
	"Saves": 69,
	"GA": 17,
	"Clean": 9,
	"Rating": 6.72,
    },
    {
	"Player": "Ollie Watkins",
	"Position": "ST",
	"Mins":1596,
	"Rating": 7.2,
	"Goals": 12,
	"Assists": 6,
	"KeyP": 1.5,
	"ThrB": 0.1,
	},
	{
	"Player": "Harry Kane",
	"Position": "ST",
	"Mins": 2773,
	"Rating": 7.85,
	"Goals": 35,
	"Assists": 13,
	"KeyP": 1.1,
	"ThrB": 0.5,
	},
	{
	"Player": "Bukayo Saka",
	"Position": "RW",
	"Mins": 385,
	"Rating": 7.59,
	"Goals": 15,
	"Assists": 13,
	"KeyP": 2.1,
	"ThrB": 0.1,
	},
	{
	"Player": "Marc Guehi",
	"Position": "RCB",
	"Mins": 1870,
	"Tackles": 1.3,
	"Inter": 0.8,
	"Fouls": 0.5,
	"Clear": 3.3,
	"Rating": 6.66,
	},
	{
	"Player": "Kalvin Phillips",
	"Position": "CDM",
	"Mins": 543,
	"Tackles": 0.7,
	"Inter": 0.4,
	"Fouls": 1.5,
	"Clear": 0.5,
	"Rating": 6.33,
	"Goals": 2,
	"Assists": 1,
	"KeyP": 0.1,
	"ThrB": 0.0,
	},
	{
	"Player": "Conor Gallagher",
	"Position": "RCM",
	"Mins": 1739,
	"Tackles": 2.2,
	"Inter": 1.2,
	"Fouls": 1.3,
	"Clear": 0.4,
	"Rating": 6.95,
	"Goals": 0,
	"Assists": 4,
	"KeyP": 1.1,
	"ThrB": 0.2,
	"Saves": 0
	},
	{
	"Player": "Marcus Rashford",
	"Position": "LW",
	"Mins": 1847,
	"Rating": 6.46,
	"Goals": 7,
	"Assists": 3,
	"KeyP": 0.8,
	"ThrB": 0,
	},
	{
	"Player": "Callum Wilson",
	"Position": "ST",
	"Mins": 267,
	"Rating": 6.62,
	"Goals": 9,
	"Assists": 2,
	},
    {
	"Player": "Phil Foden",
	"Position": "RCM",
	"Mins": 2569,
    "Rating": 7.12,
	"Goals": 9,
	"Assists": 8,
	"KeyP": 1.7,
	"ThrB": 0.3,
	"Saves": 0
	},
    {
	"Player": "Harry Maguire",
	"Position": "LCB",
	"Mins": 2476,
	"Tackles": 0.9,
	"Inter": 0.9,
	"Fouls": 1.2,
	"Clear": 2.8,
	"Rating": 6.95,
	"Goals": 1,
	"Assists": 2,
	},
    {
	"Player": "Reece James",
	"Position": "RB",
	"Mins": 457,
	"Tackles": 1.6,
	"Inter": 1.2,
	"Fouls": 0.8,
	"Clear": 1.4,
	"Rating":6.57,
	"Goals": 0,
	"Assists": 1,
	"KeyP": 0.8,
	"ThrB": 0.2,
	}
    ]
}
def get_filtered_lineup(formation):
    lineup = sorted(ratings["players"], key=lambda x: (
        x.get("Rating", 0),
        x.get("Mins", 0),
        x.get("Goals", 0),
        x.get("Assists", 0),
        x.get("KeyP", 0),
        x.get("ThrB", 0),
        x.get("Tackles", 0),
        x.get("Inter", 0),
        x.get("Clear", 0),
        x.get("Saves", 0)
    ), reverse=True)

    positions = {
        "4-3-3": {
            "GK": (45, 10),
            "LB": (85, 30),
            "LCB": (65, 23),
            "RCB": (35, 23),
            "RB": (10, 30),
            "LCM": (70, 60),
            "CDM": (55, 40),
            "RCM": (30, 60),
            "LW": (80, 67.5),
            "ST": (45, 75),
            "RW": (15, 67.5)
        },
        "4-4-2": {
            "GK": (45, 10),
            "LB": (85, 27),
            "LCB": (65, 23),
            "RCB": (35, 23),
            "RB": (10, 27),
            "LCM": (70, 60),
            "CDM1": (65, 40),
            "CDM2": (35, 40),
            "RCM": (20, 60),
            "ST1": (30, 75),
            "ST2": (60, 75)
        },
        "4-2-3-1": {
            "GK": (45, 10),
            "LB": (85, 27),
            "LCB": (65, 23),
            "RCB": (35, 23),
            "RB": (10, 27),
            "CDM1": (65, 40),
            "CDM2": (35, 40),
            "LCM": (70, 60),
            "RCM": (20, 60),
            "CAM": (45, 67.5),
            "ST": (45, 75)
        },
        "3-4-3": {
            "GK": (45, 10),
            "LB": (85, 47.5),
            "LCB": (75, 35),
            "RCB2": (52, 33),
            "RCB1": (30, 35),
            "RB": (15, 47.5),
            "CDM": (35, 60),
            "LCM": (65, 60),
            "LW": (80, 75),
            "ST": (45, 85),
            "RW": (15, 75)
        },
        "3-4-2-1": {
            "GK": (45, 10),
            "LB": (85, 47.5),
            "LCB": (75, 35),
            "RCB2": (52, 33),
            "RCB1": (30, 35),
            "RB": (15, 47.5),
            "CDM": (35, 60),
            "LCM": (65, 60),
            "CAM": (70, 75),
            "RCM": (20, 75),
            "ST": (45, 85),
		}    
    }

    filtered_lineup = {position: [] for position in positions[formation]}

    if formation == "4-4-2":
        for position, coordinates in positions[formation].items():
            if position == "ST1" and len([player["Player"] for player in lineup if player["Position"] == "ST"]) >= 1:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "ST"][0])
            elif position == "ST2" and len([player["Player"] for player in lineup if player["Position"] == "ST"]) >= 2:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "ST"][1])
            elif position == "CDM1" and len([player["Player"] for player in lineup if player["Position"] == "CDM"]) >= 1:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "CDM"][0])
            elif position == "CDM2" and len([player["Player"] for player in lineup if player["Position"] == "CDM"]) >= 2:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "CDM"][1])
    elif formation == "4-2-3-1":
        for position, coordinates in positions[formation].items():
            if position == "CDM1" and len([player["Player"] for player in lineup if player["Position"] == "CDM"]) >= 1:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "CDM"][0])
            elif position == "CDM2" and len([player["Player"] for player in lineup if player["Position"] == "CDM"]) >= 2:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "CDM"][1])
    elif formation == "3-4-3":
        for position, coordinates in positions[formation].items():
            if position == "RCB1" and len([player["Player"] for player in lineup if player["Position"] == "RCB"]) >= 1:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "RCB"][0])
            elif position == "RCB2" and len([player["Player"] for player in lineup if player["Position"] == "RCB"]) >= 2:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "RCB"][1])
    elif formation == "3-4-2-1":
        for position, coordinates in positions[formation].items():
            if position == "RCB1" and len([player["Player"] for player in lineup if player["Position"] == "RCB"]) >= 1:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "RCB"][0])
            elif position == "RCB2" and len([player["Player"] for player in lineup if player["Position"] == "RCB"]) >= 2:
                filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == "RCB"][1])
                    
        

    for position, coordinates in positions[formation].items():
        if len([player["Player"] for player in lineup if player["Position"] == position]) >= 1:
            filtered_lineup[position].append([player["Player"] for player in lineup if player["Position"] == position][:1][0])

    return filtered_lineup, positions

import streamlit as st
from mplsoccer.pitch import VerticalPitch
import matplotlib.pyplot as plt

# ... (your existing code)

def main():
    st.title("England Euros 2024 line-up")

    pitch = VerticalPitch(pitch_type='opta', pitch_color='white', line_color='black')

    formation = st.selectbox("Select Formation", ["4-3-3", "4-4-2", "4-2-3-1", "3-4-3", "3-4-2-1"])

    lineup, positions = get_filtered_lineup(formation)

    player_out_options = ["Reset"] + [player for position, players in lineup.items() for player in players]
    player_out = st.selectbox("Player Out", player_out_options)

    player_in_options = ["Reset"] + [player["Player"] for player in sorted(ratings["players"], key=lambda x: x["Rating"], reverse=True)]
    player_in = st.selectbox("Player In", player_in_options)

    if player_out != "Reset" and player_in != "Reset":
        for position, players in lineup.items():
            if player_out in players:
                players.remove(player_out)
                players.append(player_in)

    fig, ax = plt.subplots(figsize=(10, 7))
    pitch.draw(ax=ax)

    for position, coordinates in positions[formation].items():
        player_names = lineup[position]
        for player_name in player_names:
            ax.text(coordinates[0], coordinates[1], player_name, ha='center', va='center', fontsize=8, color='black')

    st.pyplot(fig)
    st.sidebar.subheader("Entire Squad")

    for player in sorted(ratings["players"], key=lambda x: x["Rating"], reverse=True):
        st.sidebar.write(f"{player['Player']} - {player['Position']}")

if __name__ == "__main__":
    main()
