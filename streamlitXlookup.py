# #streamlitXlookup
# #streamlitXlookup 2024/03/06通过测试

import streamlit as st
import pandas as pd
import base64
from io import BytesIO

def vlookup_auto_merge(df_left, df_right, how='left', default_value="Not Found"):
    """
    实现自动检测主键列并合并两个表
    """
    try:
        merged_df = pd.merge(df_left, df_right, how=how)
        return merged_df.fillna(default_value)
    except KeyError:
        return pd.DataFrame({"Error": ["无法自动检测主键列，请手动选择主键列"]})

def download_button(df, filename, button_text='Download XLSX'):
    """
    创建一个下载按钮
    """
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    b64 = base64.b64encode(excel_buffer.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">{button_text}</a>'
    return href

def main():
    st.title('Streamlit VLOOKUP Demo')

    # 上传左侧和右侧的 Excel 文件
    uploaded_file_left = st.sidebar.file_uploader("上传左侧 Excel 文件(左表)", type=["xlsx"])
    uploaded_file_right = st.sidebar.file_uploader("上传右侧 Excel 文件(右表)", type=["xlsx"])

    # 用户选择合并参数
    merge_options = ['left', 'right', 'outer', 'inner']
    merge_option = st.sidebar.selectbox("选择合并参数:", merge_options)

    if uploaded_file_left is not None and uploaded_file_right is not None:
        # 用户选择左侧和右侧 Excel 文件的 sheet 页
        sheet_left = st.sidebar.selectbox("选择左侧 Excel 的 sheet 页:", pd.ExcelFile(uploaded_file_left).sheet_names)
        sheet_right = st.sidebar.selectbox("选择右侧 Excel 的 sheet 页:", pd.ExcelFile(uploaded_file_right).sheet_names)

        # 读取左侧和右侧的 Excel 文件的指定 sheet 页
        df_left = pd.read_excel(uploaded_file_left, sheet_name=sheet_left)
        df_right = pd.read_excel(uploaded_file_right, sheet_name=sheet_right)

        # 显示上传的左侧和右侧数据
        st.subheader("左侧数据:")
        st.dataframe(df_left)

        st.subheader("右侧数据:")
        st.dataframe(df_right)

        # 执行 VLOOKUP 自动合并
        merged_result = vlookup_auto_merge(df_left, df_right, how=merge_option)

        # 显示合并后的结果
        st.subheader("合并后的结果:")
        st.dataframe(merged_result)
        

        # 添加下载按钮
        st.markdown(download_button(merged_result, "merged_result"), unsafe_allow_html=True)

if __name__ == "__main__":
    main()


# =============================================================================
# import streamlit as st
# import pandas as pd
# import base64
# from io import BytesIO

# def vlookup_auto_merge(df_left, df_right, how='left', default_value="Not Found"):
#     """
#     实现自动检测主键列并合并两个表
#     """
#     try:
#         merged_df = pd.merge(df_left, df_right, how=how)
#         return merged_df.fillna(default_value)
#     except KeyError:
#         return pd.DataFrame({"Error": ["无法自动检测主键列，请手动选择主键列"]})

# def download_button(df, filename, button_text='Download XLSX'):
#     """
#     创建一个下载按钮
#     """
#     excel_buffer = BytesIO()
#     df.to_excel(excel_buffer, index=False)
#     excel_buffer.seek(0)
#     b64 = base64.b64encode(excel_buffer.read()).decode()
#     href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">{button_text}</a>'
#     return href

# def main():
#     st.title('Streamlit VLOOKUP Demo')

#     # 上传左侧和右侧的 Excel 文件
#     uploaded_file_left = st.file_uploader("上传左侧 Excel 文件", type=["xlsx"])
#     uploaded_file_right = st.file_uploader("上传右侧 Excel 文件", type=["xlsx"])

#     # 用户选择合并参数
#     merge_options = ['left', 'right', 'outer', 'inner']
#     merge_option = st.selectbox("选择合并参数:", merge_options)

#     if uploaded_file_left is not None and uploaded_file_right is not None:
#         # 用户选择左侧和右侧 Excel 文件的 sheet 页
#         sheet_left = st.selectbox("选择左侧 Excel 的 sheet 页:", pd.ExcelFile(uploaded_file_left).sheet_names)
#         sheet_right = st.selectbox("选择右侧 Excel 的 sheet 页:", pd.ExcelFile(uploaded_file_right).sheet_names)

#         # 读取左侧和右侧的 Excel 文件的指定 sheet 页
#         df_left = pd.read_excel(uploaded_file_left, sheet_name=sheet_left)
#         df_right = pd.read_excel(uploaded_file_right, sheet_name=sheet_right)
#         left_column1, right_column1 = st.columns(2)

#         # 显示上传的左侧和右侧数据
#         with left_column1:
#             st.subheader("左侧数据:")
#             st.write(df_left)

#         with right_column1:
#             st.subheader("右侧数据:")
#             st.write(df_right)

#         # 执行 VLOOKUP 自动合并
#         merged_result = vlookup_auto_merge(df_left, df_right, how=merge_option)

#         # 显示合并后的结果
#         st.subheader("合并后的结果:")

#         # 使用 st.beta_columns 分割布局
#         left_column, right_column = st.columns(2)
        
#         with left_column:
#             st.subheader("左侧表:")
#             st.write(df_left)

#         with right_column:
#             st.subheader("右侧表:")
#             st.write(df_right)

#         st.subheader("合并后的表:")
#         st.write(merged_result)

#         # 添加下载按钮
#         st.markdown(download_button(merged_result, "merged_result"), unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()

# # ==============================================================================================


