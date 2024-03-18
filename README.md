# StreamlitPandasXlookup
基于streamlit和pandas，实现xlookup功能


========================================aggrid==============================================
格式化展示
pip install aggrid 

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
options_builder = GridOptionsBuilder.from_dataframe(df)
options_builder.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True, wrapText=True, autoHeight=True)
options_builder.configure_column('col1',  pinned='left')
options_builder.configure_column('col2',  pinned='left')
grid_options = options_builder.build()
grid_return = AgGrid(df, grid_options, theme='blue')
======================================================================================
