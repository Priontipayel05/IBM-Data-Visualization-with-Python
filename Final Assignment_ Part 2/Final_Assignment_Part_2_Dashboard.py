
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# ============================================================
# LOAD DATA
# ============================================================

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

df = pd.read_csv(DATA_URL)

# Clean column names
df.columns = df.columns.str.strip()

if 'unemployment_rate' not in df.columns and 'Unemployment_Rate' in df.columns:
    df.rename(
        columns={'Unemployment_Rate': 'unemployment_rate'},
        inplace=True
    )

# ============================================================
# CREATE DASH APPLICATION
# ============================================================

app = dash.Dash(__name__)

app.title = "Automobile Sales Statistics Dashboard"

# Get available years
year_list = sorted(df['Year'].unique())

# ============================================================
# DASHBOARD LAYOUT
# ============================================================

app.layout = html.Div([

    # Dashboard heading
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={
            'textAlign': 'center',
            'font-size': '24px'
        }
    ),

    html.Br(),

    # Dropdown section
    html.Div([

        # Statistics dropdown
        html.Div([
            html.Label("Select Statistics:"),

            dcc.Dropdown(
                id='dropdown-statistics',

                options=[
                    {
                        'label': 'Yearly Statistics',
                        'value': 'Yearly Statistics'
                    },
                    {
                        'label': 'Recession Period Statistics',
                        'value': 'Recession Period Statistics'
                    }
                ],

                value='Yearly Statistics',

                placeholder='Select a report type'
            )

        ], style={
            'width': '48%',
            'display': 'inline-block'
        }),

        # Year dropdown
        html.Div([
            html.Label("Select Year:"),

            dcc.Dropdown(
                id='select-year',

                options=[
                    {
                        'label': str(year),
                        'value': year
                    }
                    for year in year_list
                ],

                value=year_list[-1],

                placeholder='Select a year'
            )

        ], style={
            'width': '48%',
            'display': 'inline-block',
            'margin-left': '2%'
        })

    ]),

    html.Br(),

    # Output graphs
    html.Div(
        id='output-container',
        style={
            'display': 'flex',
            'flexWrap': 'wrap'
        }
    )

])


# ============================================================
# CALLBACK 1
# Enable / Disable Year Dropdown
# ============================================================

@app.callback(
    Output(
        component_id='select-year',
        component_property='disabled'
    ),

    Input(
        component_id='dropdown-statistics',
        component_property='value'
    )
)

def update_input_container(selected_statistics):

    if selected_statistics == 'Yearly Statistics':
        return False

    else:
        return True


# ============================================================
# CALLBACK 2
# UPDATE DASHBOARD GRAPHS
# ============================================================

@app.callback(
    Output(
        component_id='output-container',
        component_property='children'
    ),

    [
        Input(
            component_id='dropdown-statistics',
            component_property='value'
        ),

        Input(
            component_id='select-year',
            component_property='value'
        )
    ]
)

def update_output_container(
    selected_statistics,
    selected_year
):

    # ========================================================
    # RECESSION PERIOD STATISTICS
    # ========================================================

    if selected_statistics == 'Recession Period Statistics':

        recession_data = df[
            df['Recession'] == 1
        ]

        # ----------------------------------------------------
        # GRAPH 1
        # Automobile Sales during Recession
        # ----------------------------------------------------

        sales_by_year = (
            recession_data
            .groupby('Year')['Automobile_Sales']
            .mean()
            .reset_index()
        )

        fig1 = px.line(
            sales_by_year,
            x='Year',
            y='Automobile_Sales',
            title='Automobile Sales during Recession'
        )

        # ----------------------------------------------------
        # GRAPH 2
        # Average Automobile Sales by Vehicle Type
        # ----------------------------------------------------

        vehicle_sales = (
            recession_data
            .groupby('Vehicle_Type')['Automobile_Sales']
            .mean()
            .reset_index()
        )

        fig2 = px.bar(
            vehicle_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title='Average Automobile Sales by Vehicle Type'
        )

        # ----------------------------------------------------
        # GRAPH 3
        # Advertising Expenditure by Vehicle Type
        # ----------------------------------------------------

        advertising_data = (
            recession_data
            .groupby('Vehicle_Type')['Advertising_Expenditure']
            .sum()
            .reset_index()
        )

        fig3 = px.pie(
            advertising_data,
            names='Vehicle_Type',
            values='Advertising_Expenditure',
            title='Advertising Expenditure by Vehicle Type'
        )

        # ----------------------------------------------------
        # GRAPH 4
        # Unemployment Rate Effect
        # ----------------------------------------------------

        unemployment_data = recession_data.sort_values(
            'unemployment_rate'
        )

        fig4 = px.line(
            unemployment_data,
            x='unemployment_rate',
            y='Automobile_Sales',
            color='Vehicle_Type',
            title='Effect of Unemployment Rate on Vehicle Type and Sales'
        )

    # ========================================================
    # YEARLY STATISTICS
    # ========================================================

    else:

        yearly_data = df[
            df['Year'] == selected_year
        ]

        # ----------------------------------------------------
        # GRAPH 1
        # Monthly Automobile Sales
        # ----------------------------------------------------

        monthly_sales = (
            yearly_data
            .groupby('Month')['Automobile_Sales']
            .mean()
            .reset_index()
        )

        fig1 = px.line(
            monthly_sales,
            x='Month',
            y='Automobile_Sales',
            title=f'Automobile Sales for Year {selected_year}'
        )

        # ----------------------------------------------------
        # GRAPH 2
        # Vehicle Type Sales
        # ----------------------------------------------------

        vehicle_sales = (
            yearly_data
            .groupby('Vehicle_Type')['Automobile_Sales']
            .mean()
            .reset_index()
        )

        fig2 = px.bar(
            vehicle_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title=f'Average Automobile Sales by Vehicle Type - {selected_year}'
        )

        # ----------------------------------------------------
        # GRAPH 3
        # Advertising Expenditure
        # ----------------------------------------------------

        advertising_data = (
            yearly_data
            .groupby('Vehicle_Type')['Advertising_Expenditure']
            .sum()
            .reset_index()
        )

        fig3 = px.pie(
            advertising_data,
            names='Vehicle_Type',
            values='Advertising_Expenditure',
            title=f'Advertising Expenditure by Vehicle Type - {selected_year}'
        )

        # ----------------------------------------------------
        # GRAPH 4
        # Unemployment Rate vs Sales
        # ----------------------------------------------------

        fig4 = px.scatter(
            yearly_data,
            x='unemployment_rate',
            y='Automobile_Sales',
            color='Vehicle_Type',
            title=f'Unemployment Rate vs Automobile Sales - {selected_year}'
        )

    # ========================================================
    # RETURN FOUR GRAPHS
    # ========================================================

    return [

        dcc.Graph(
            figure=fig1,
            style={'width': '49%'}
        ),

        dcc.Graph(
            figure=fig2,
            style={'width': '49%'}
        ),

        dcc.Graph(
            figure=fig3,
            style={'width': '49%'}
        ),

        dcc.Graph(
            figure=fig4,
            style={'width': '49%'}
        )

    ]


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == '__main__':
    app.run(debug=True)
