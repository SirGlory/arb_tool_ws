import asyncio
import csv
import json

from updater_luno import Updater

L_API_KEY, L_API_SECRET = 'k2dmhxm8fxc3c', 'r-dpNkeG6YMWNYtDh1WBOGQKhe6yBMj9rCNP0QrlAuQ'

L_pair = 'XBTZAR'

vol_cond = 1.0      #  <--------- Set minimum volume condition
depth = 20          #  <--------- Also adjust depth, higher for greater volume condition
                    #             Recommended depth=20 for volume=1.0
class Lunows:

    def run(self):

        def print_it(consolidated_order_book): # was (consolidated_order_book,trades) <--see line 87 in luno_updater.py

        # Bid Calculations
            cum_value=0
            vol =0
            index_loc=0
            for i in range(0,depth):
                vol += float(consolidated_order_book["bids"][i][1])
                cum_value += float(consolidated_order_book["bids"][i][1])*float(consolidated_order_book["bids"][i][0])
                index_loc = i
                if vol > vol_cond:
                    break
            w_avg_price=cum_value/vol

        # Ask Calculations
            acum_value=0
            avol =0
            aindex_loc=0
            for x in range(0,depth):
                avol += float(consolidated_order_book["asks"][x][1])
                acum_value += float(consolidated_order_book["asks"][x][1])*float(consolidated_order_book["asks"][x][0])
                aindex_loc = x
                if avol > vol_cond:
                    break
            aw_avg_price=acum_value/avol

        # Text Output
            print("Connected to LUNO Websocket -> Receiving Data")

        # Data to be written
            luno_dict = {
                "wa_price": w_avg_price,
                "vol": vol,
                "cum_val": cum_value,
                "ord_pos": index_loc,
                "wa_price_a": aw_avg_price,
                "vol_a": avol,
                "cum_val_a": acum_value,
                "ord_pos_a": aindex_loc
            }

            with open("data\data_luno.json", "w") as outfile:
                json.dump(luno_dict, outfile)


    # Create Websocket
        updater = Updater(
            pair_code=L_pair,
            api_key=L_API_KEY,
            api_secret=L_API_SECRET,
            hooks=[print_it],
        )

    # Async Loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(updater.run())

if __name__ == '__main__':
    data_l = Lunows().run()
