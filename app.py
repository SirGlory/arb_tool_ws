import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


refresh_interval = 100 # 1000 milliseconds = 1 second       <--------- Set Time Interval, currently 0.1s

def getData1():
    f = open('data\data_luno.json',)
    data = json.load(f)
    return data

def getData2():
    f2 = open('data\data_valr.json',)
    data2 = json.load(f2)
    return data2


# Launch App_____________________________________________________
app = dash.Dash()
server = app.server

# App Layout_____________________________________________________
app.layout = html.Div([
            # Arbitrage Stats
                html.H3("Arbitrage Stats", style={'text-align': 'center'}),
                html.Div([
                    html.Hr(),
                    html.H5("LUNO Order Book", style={'text-align': 'left'}),
                    html.Pre(
                        id='luno-stats',
                        children='Opportunity = R {} or {}% on: btc for total= R'
                    ),
                    html.Hr(),
                    html.H5("VALR Order Book", style={'text-align': 'left'}),
                    html.Pre(
                        id='valr-stats',
                        children='Opportunity = R {} or {}% on: btc for total= R'
                    ),
                    html.Hr(),
                    html.H5("Arbitrage Opportunity", style={'text-align': 'left'}),
                    html.Pre(
                        id='arb-opp',
                        children='Opportunity = R {} or {}% on: btc for total= R'
                    ),
                    dcc.Interval(
                        id='interval-component',
                        interval=refresh_interval,
                        n_intervals=0
                    ),
                ]),
    ],style={'backgroundColor':'white','margin': 10})

@app.callback(Output('luno-stats', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    data_l = getData1()
    return 'Bids: Weighted Avg Price= R {} at Volume= {} BTC for Total= R {}\n' \
           'Asks: Weighted Avg Price= R {} at Volume= {} BTC for Total= R {}'.format(int(data_l['wa_price']),
                                                                        data_l['vol'].__round__(3),
                                                                        int(data_l['cum_val']),
                                                                        int(data_l['wa_price_a']),
                                                                        data_l['vol_a'].__round__(3),
                                                                        int(data_l['cum_val_a']),)
@app.callback(Output('valr-stats', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout2(n):
    data_v = getData2()
    return 'Bids: Weighted Avg Price= R {} at Volume= {} BTC for Total= R {}\n' \
           'Asks: Weighted Avg Price= R {} at Volume= {} BTC for Total= R {}'.format(int(data_v['wa_price']),
                                                                        data_v['vol'].__round__(3),
                                                                        int(data_v['cum_val']),
                                                                        int(data_v['wa_price_a']),
                                                                        data_v['vol_a'].__round__(3),
                                                                        int(data_v['cum_val_a']),)
@app.callback(Output('arb-opp', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout3(n):
    data_l = getData1()
    data_v = getData2()

    wa_delta_lavb = data_v['wa_price'] - data_l['wa_price_a']
    wa_delta_valb = data_l['wa_price'] - data_v['wa_price_a']
    max_vol_lavb = min(data_v['vol'],data_l['vol_a'])
    max_vol_valb = min(data_l['vol'],data_v['vol_a'])
    arb_opp = max(wa_delta_lavb,wa_delta_valb)
    arb_opp_vol = 0
    arb_direct = ""
    if arb_opp == wa_delta_lavb:
        arb_opp_vol = max_vol_lavb
        arb_direct = "LUNO Ask --> VALR Bid"
    else:
        arb_opp_vol = max_vol_valb
        arb_direct = "VALR Ask --> LUNO Bid"
    arb_opp_value = arb_opp_vol*arb_opp
    arb_status_p = ""
    arb_status_v = ""
    if arb_opp <=0:
        arb_status_p = "UNAVAILABLE"
    else:
        arb_status_p = "GOOD"

    if arb_opp_vol <=1.0:
        arb_status_v = "UNAVAILABLE"
    else:
        arb_status_v = "GOOD"

    return 'Luno Ask to Valr Bid = R {} at Max Volume= {}\n' \
           'Valr Ask to Luno Bid = R {} at Max Volume= {}\n' \
           '**************\n' \
           'Arb Opp Direction: {}\n'\
           'Arb Opp Delta = R {}\n'\
           'Arb Opp Volume = {} BTC\n' \
           'Arb Opp Value = R {}\n' \
           '**************\n' \
           'Arb Status: Price Condition = {} | Volume Condition = {}'.format(int(wa_delta_lavb),max_vol_lavb.__round__(3),
                                                int(wa_delta_valb),max_vol_valb.__round__(3),
                                arb_direct,int(arb_opp),arb_opp_vol.__round__(3),int(arb_opp_value),arb_status_p,arb_status_v)


if __name__ == '__main__':
    app.run_server()