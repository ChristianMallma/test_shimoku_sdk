import shimoku_api_python as Shimoku
import pandas as pd

from dotenv import load_dotenv
from os import getenv

# Load variables
load_dotenv()

API_TOKEN = getenv('API_TOKEN')
UNIVERSE_ID = getenv('UNIVERSE_ID')
WORKSPACE_ID = getenv('WORKSPACE_ID')

# Instance a Shimoku client
sh_client = Shimoku.Client(
    access_token=API_TOKEN,
    universe_id=UNIVERSE_ID,
    verbosity='INFO',  # DEBUG, WARNING
    async_execution=True
)

# To activate async execution
sh_client.activate_async_execution()

# Clean workspace
# sh_client.workspaces.delete_all_workspace_menu_paths(uuid=WORKSPACE_ID)
# sh_client.workspaces.delete_all_workspace_boards(uuid=WORKSPACE_ID)

# Initializing
sh_client.set_workspace(uuid=WORKSPACE_ID)
sh_client.set_board('Test Shimoku SDK')

# Menu path
sh_client.set_menu_path('Showcase')
sh_client.plt.clear_menu_path()

# Loading iris data set
df_iris = pd.read_csv('ds/iris.csv')

# Columns rename
df_iris.rename({'sepal.length': 'Sepal_length',
                'sepal.width': 'Sepal_width',
                'petal.length': 'Petal_length',
                'petal.width': 'Petal_width',
                'variety': 'Species'},
               axis=1,
               inplace=True)

# Show df
print(df_iris.head(5))


# # To reuse data sets
sh_client.reuse_data_sets()

# Sharing data
sh_client.plt.set_shared_data(
    dfs={'data': df_iris}
)

# # Set HTML title
sh_client.plt.html(html='<h1>Testing the Shimoku SDK using the Iris dataset</h1>', order=0)

# Show graph
# Bar graphic
sh_client.plt.set_tabs_index(tabs_index=('Tabs Group', 'Bar'), order=0)
sh_client.plt.bar(data=df_iris,
                  order=0,
                  x='Species',
                  y=['Sepal_width'],
                  x_axis_name='Species',
                  y_axis_name='Sepal Width',
                  title='Sepal Width by Species')

# Line graphic
sh_client.plt.change_current_tab('Line')
sh_client.plt.line(data=df_iris,
                   order=0,
                   x='Species',
                   y=['Sepal_width'],
                   x_axis_name='Species',
                   y_axis_name='Sepal Width',
                   title='Sepal Width by Species',
                   rows_size=2,
                   cols_size=12)

sh_client.run()
