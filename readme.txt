* Must have Python and virtualenv already installed *
_____________________________________________
FOR WINDOWS INSTRUCTIONS - Command Prompt CLI

___________________
Installation Steps:
    1: cd into_desired_folder				   	"Rnter created folder"
    2: git clone https://github.com/SirGlory/arb_tool_ws.git    "Clone from within the created folder"
    3: cd arb_tool_ws                                     	"Enter project folder"
    4: python -m virtualenv venv                          	"Create virtual environment"
    5: .\venv\Scripts\activate                           	"Activate virtual environment"
    6: pip install -r requirements.txt                   	"Install required packages"

__________
Run Steps:
*you need to run three scripts simultaneously in 3 CLIs, for an IDE such as PyCharm you can run all three from IDE*

  Script One
	1: Open command prompt				"Open one command prompt per script"
	2: cd into_project_folder			"Enter project folder"
	3: .\venv\Scripts\activate			"Activate virtual environment"
	4: python luno_ws.py 				"Run script to connect to LUNO Websocket"

  Script Two
	5: Open another command prompt			"Open one command prompt per script"
	6: cd into_project_folder			"Enter project folder"
	7: .\venv\Scripts\activate			"Activate virtual environment"
	8: python valr_ws.py 				"Run script to connect to VALR Websocket"

  Script Three
	9: Open another command prompt			"Open one command prompt per script"
	10: cd into_project_folder			"Enter project folder"
	11: .\venv\Scripts\activate			"Activate virtual environment"
	12: python app.py				"Run script to proccess data and display in Dash App"
	13: navigate to http://127.0.0.1:8050/		"View Dash app in browser"

________
TO STOP 
  close command prompts or hit "CTRL + C" or "CTRL + PAUSEBREAK"

_______________
Optional Tuning:
    -at the top of the valr_ws.py and luno_ws.py script:
	*Adjust vol_cond variable for desired minimum volume, default=1.0
	*Adjust depth for scan depth of orderbook, higher for greater vol_cond or illiquid markets, default=20

    -at the top of app.py
	*Adjust refresh_interval for faster or slower refresh rate in Dash app, default=100 (milliseconds)
	
______
TIPS
	- use TAB to autocomplete, eg "python l" + TAB --> becomes "python luno_ws.py" or "cd D" --> becomes "cd Desktop"
 
