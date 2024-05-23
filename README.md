# ClubDash

### Overview
ClubDash is a data visualization project focused on analyzing and comparing the performance of soccer players during the FIFA World Cup 2022. The project aims to provide insights into player dynamics, team strategies, and performance metrics through an interactive dashboard.

### Prerequisites
- Python 3.x
- Jupyter Notebook

### Environment Setup
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/iamvishalsehgal/ClubDash.git
   cd ClubDash
   ```

2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt  # Or pip3 install -r requirements.txt
   ```

### Running the Code
1. **Start Jupyter Notebook or your favorite code editor:**
   ```sh
   jupyter notebook   # Or any other code editor, We used VSCode
   ```
   Open `dash.ipynb` and run all cells to start the dashboard.

### Running Tests
Currently, there are no automated tests defined for this project. Testing can be done manually by verifying the functionality through the web interface.

### Dependencies
- Flask
- Dash
- Plotly
- pandas
- numpy

All dependencies are listed in the `requirements.txt` file and can be installed using the command provided above.

### Data Analysis and Visualization Tasks
1. **Player’s Performance Comparison:**
   - Compare players’ performance in World Cup matches against their club colleagues.

2. **Player’s per Team Comparison:**
   - Analyze players’ performance within their national teams.

3. **Similar Players per Club:**
   - Find similarities in playing styles among club players.

4. **Effect per Club:**
   - Evaluate how clubs perform in the World Cup based on their players’ performance.

### Implementation Details
- **Framework:** Dash (built on Flask and React)
- **Libraries:** dash-core-components, dash-html-components, Pandas, Plotly
- **Future Enhancements:**
  - Improve interactivity and aesthetics using Dash Bootstrap Components.
  - Add more datasets for comprehensive analysis.
  - Include automated testing and validation processes.


### Data Sources

1. **Match Data:**
   - File Used: `Matchdata.csv` (originally `data.csv`)
   - Source: [FIFA World Cup 2022 Match Data](https://www.kaggle.com/datasets/swaptr/fifa-world-cup-2022-match-data)

2. **Player Data:**
   - Files Used: `FIFA World Cup 2022 Player Data/player_stats.csv` and `FIFA World Cup 2022 Player Data/player_misc.csv`
   - Source: [FIFA World Cup 2022 Player Data](https://www.kaggle.com/datasets/swaptr/fifa-world-cup-2022-player-data)

3. **Group Data:**
   - Files Used: `Fifa_Worldcup_2022_Groups.csv` and `FIFA22_official_data.csv`
   - Source: [2022 FIFA World Cup Qatar Full Live Dataset](https://www.kaggle.com/datasets/muhammad4hmed/2022-fifa-worldcup-qatar-full-live-dataset?select=Players_Data_2022)


### Use Cases
- Soccer fans can explore player and team dynamics.
- Analysts can leverage predictive modeling to forecast player performance.

### Future Work
- Enhance visual appeal and interactivity.
- Incorporate additional datasets and predictive models.
- Develop a more robust testing framework.
- Make Dashboard Fast.

### Reflection
- The initial design allowed users to select views and compare players based on various attributes.
- User feedback led to the introduction of buttons for easier navigation and data comparison.

For more details, visit the [ClubDash GitHub repository](https://github.com/iamvishalsehgal/ClubDash/tree/main).