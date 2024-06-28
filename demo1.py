import pandas as pd

xlsx_path = '/mnt/big_disk/gbw/projects/4_19/data/12315.1投诉信息部分脱敏.xlsx'

data = pd.read_excel(xlsx_path)

print(data.head())

# 读取xlsx文件
# try:
#     # 尝试读取文件
#     data = pd.read_excel(xlsx_path)
# except Exception as e:
#     # 如果读取失败，返回错误信息
#     error = str(e)

# 输出读取的数据或错误信息
# data if 'data' in locals() else error


# 筛选“类型”列为“投诉”的数据
complaints_df = data[data['类型'] == '投诉']

# 筛选“类型”列为“举报”的数据
reports_df = data[data['类型'] == '举报']

# 输出结果确认
print(complaints_df.head(), reports_df.head())

# 提取客体类别全称的第一项作为消费类型
complaints_df['消费类型'] = complaints_df['客体类别全称'].apply(lambda x: x.split('->')[0])

# 统计不同消费类型的数量
consumption_types_counts = complaints_df['消费类型'].value_counts()

print(consumption_types_counts)

# 提取问题类别全称的第二项作为投诉问题类别
complaints_df['投诉问题类别'] = complaints_df['问题类别全称'].apply(lambda x: x.split('->')[1] if '->' in x else x)

# 统计不同投诉问题类别的数量
complaint_categories_counts = complaints_df['投诉问题类别'].value_counts()

print(complaint_categories_counts)


# 按照消费类型、投诉问题类别和销售方式进行分组，计算每个组合的数量
classification_counts = complaints_df.groupby(['消费类型', '投诉问题类别', '销售方式']).size().reset_index(name='数量')

print(classification_counts)

# 按照消费类型和投诉问题类别进行分组，并计算消费金额的总和
consumption_amount_sums = complaints_df.groupby(['消费类型', '投诉问题类别'])['消费金额(单位:元)'].sum().reset_index(name='消费金额总和')

print(consumption_amount_sums)

# 将挽回经济损失的空值替换为0
complaints_df['挽回经济损失(单位:元)'].fillna(0, inplace=True)

# 按照消费类型和投诉问题类别进行分组，并计算挽回经济损失的总和
recovered_losses_sums = complaints_df.groupby(['消费类型', '投诉问题类别'])['挽回经济损失(单位:元)'].sum().reset_index(name='挽回经济损失总和')

print(recovered_losses_sums)

# 按照消费类型和投诉问题类别进行分组，并计算办理情况状态为已办结的个数
completed_cases_counts = complaints_df[complaints_df['办理情况状态'] == '已办结'].groupby(
    ['消费类型', '投诉问题类别']
).size().reset_index(name='已办结个数')

print(completed_cases_counts)


print(100*'*')

# 首先提取符合条件的行，即第一项为"商品（产品）"的行
filtered_data = data[data['客体类别全称'].str.startswith('商品（产品）')]

# 然后提取每行的第二项
data['客体第二项'] = filtered_data['客体类别全称'].apply(lambda x: x.split('->')[1] if len(x.split('->')) > 1 else None)


# data['客体第二项'] = data['客体类别全称'].apply(lambda x: x.split('->')[1] if len(x.split('->')) > 1 else None)

# 统计不同的第二项类别的数量
object_second_category_counts = data['客体第二项'].value_counts()

print(object_second_category_counts)

# 按照“客体第二项”和“销售方式”进行分组，统计每个分类下的数量
object_second_category_by_sales_mode = data.groupby(['客体第二项', '销售方式']).size().reset_index(name='数量')

print(object_second_category_by_sales_mode)


# 首先提取问题类别全称的第二项作为新的列
data['问题类别第二项'] = data['问题类别全称'].apply(lambda x: x.split('->')[1] if len(x.split('->')) > 1 else None)

# 按照“客体第二项”和“问题类别第二项”进行分组，统计每个分类下的数量
object_second_category_by_issue_type = data.groupby(['客体第二项', '问题类别第二项']).size().reset_index(name='数量')

print(object_second_category_by_issue_type)

# 计算每个“客体第二项”中办理情况状态为“已办结”的计数
completed_cases_by_object_second_category = data[data['办理情况状态'] == '已办结'].groupby('客体第二项').size().reset_index(name='已办结个数')

print(completed_cases_by_object_second_category)

# 计算每个“客体第二项”中消费金额(单位:元)的总和
sum_consumption_by_object_second_category = data.groupby('客体第二项')['消费金额(单位:元)'].sum().reset_index(name='消费金额总和')

print(sum_consumption_by_object_second_category)

# 先将挽回经济损失的空值替换为0，然后进行求和
data['挽回经济损失(单位:元)'].fillna(0, inplace=True)
sum_loss_recovery_by_object_second_category = data.groupby('客体第二项')['挽回经济损失(单位:元)'].sum().reset_index(name='挽回经济损失总和')

print(sum_loss_recovery_by_object_second_category)


print(100*'*')

# 首先提取符合条件的行，即第一项为"商品（产品）"的行
filtered_data = data[data['客体类别全称'].str.startswith('服务')]

# 然后提取每行的第二项
data['客体第二项'] = filtered_data['客体类别全称'].apply(lambda x: x.split('->')[1] if len(x.split('->')) > 1 else None)


# data['客体第二项'] = data['客体类别全称'].apply(lambda x: x.split('->')[1] if len(x.split('->')) > 1 else None)

# 统计不同的第二项类别的数量
object_second_category_counts = data['客体第二项'].value_counts()

print(object_second_category_counts)

# 按照“客体第二项”和“销售方式”进行分组，统计每个分类下的数量
object_second_category_by_sales_mode = data.groupby(['客体第二项', '销售方式']).size().reset_index(name='数量')

print(object_second_category_by_sales_mode)


# 首先提取问题类别全称的第二项作为新的列
data['问题类别第二项'] = data['问题类别全称'].apply(lambda x: x.split('->')[1] if len(x.split('->')) > 1 else None)

# 按照“客体第二项”和“问题类别第二项”进行分组，统计每个分类下的数量
object_second_category_by_issue_type = data.groupby(['客体第二项', '问题类别第二项']).size().reset_index(name='数量')

print(object_second_category_by_issue_type)

# 计算每个“客体第二项”中办理情况状态为“已办结”的计数
completed_cases_by_object_second_category = data[data['办理情况状态'] == '已办结'].groupby('客体第二项').size().reset_index(name='已办结个数')

print(completed_cases_by_object_second_category)

# 计算每个“客体第二项”中消费金额(单位:元)的总和
sum_consumption_by_object_second_category = data.groupby('客体第二项')['消费金额(单位:元)'].sum().reset_index(name='消费金额总和')

print(sum_consumption_by_object_second_category)

# 先将挽回经济损失的空值替换为0，然后进行求和
data['挽回经济损失(单位:元)'].fillna(0, inplace=True)
sum_loss_recovery_by_object_second_category = data.groupby('客体第二项')['挽回经济损失(单位:元)'].sum().reset_index(name='挽回经济损失总和')

print(sum_loss_recovery_by_object_second_category)


print(100*'*')

# 提取问题类别全称的第二项作为举报问题类别
reports_df['举报问题类别'] = reports_df['问题类别全称'].apply(lambda x: x.split('->')[1] if '->' in x else x)

# 统计不同举报问题类别的数量
reports_categories_counts = reports_df['举报问题类别'].value_counts()

print(reports_categories_counts)


# 计算每个“举报问题类别”中状态为“已办结”的计数
reports_cases_by_object_second_category = reports_df[reports_df['初查受理状态'] == '立案'].groupby('举报问题类别').size().reset_index(name='立案个数')

print(reports_cases_by_object_second_category)

# 计算每个“举报问题类别”中消费金额(单位:元)的总和
sum_reports_df_by_object_second_category = reports_df.groupby('举报问题类别')['消费金额(单位:元)'].sum().reset_index(name='消费金额总和')

print(sum_reports_df_by_object_second_category)

# 计算每个“举报问题类别”中罚款金额(单位:元)的总和
reports_df['罚款金额(单位:元)'].fillna(0, inplace=True)

sum_fk_reports_df_by_object_second_category = reports_df.groupby('举报问题类别')['罚款金额(单位:元)'].sum().reset_index(name='罚款金额总和')

print(sum_fk_reports_df_by_object_second_category)

# 计算每个“举报问题类别”中没收金额(单位:元)的总和
reports_df['罚款金额(单位:元)'].fillna(0, inplace=True)

sum_ms_reports_df_by_object_second_category = reports_df.groupby('举报问题类别')['没收金额(单位:元)'].sum().reset_index(name='没收金额总和')

print(sum_ms_reports_df_by_object_second_category)

print(100*'*')
# 提取客体类别全称的第一项作为消费类型
complaints_df['消费类型'] = complaints_df['客体类别全称'].apply(lambda x: x.split('->')[0])

# 统计不同消费类型的数量
consumption_types_counts = complaints_df['消费类型'].value_counts()

print(consumption_types_counts)

# 计算每个“不同消费类型”中办理情况状态为“已办结”的计数
complaints_df_cases_by_object_second_category = complaints_df[complaints_df['办理情况状态'] == '已办结'].groupby('消费类型').size().reset_index(name='已办结个数')

print(complaints_df_cases_by_object_second_category)

# 计算每个“不同消费类型”中初查受理状态状态为“已受理”的计数
complaints_df_cases_by_object_second_category = complaints_df[complaints_df['初查受理状态'] == '已受理'].groupby('消费类型').size().reset_index(name='已受理个数')

print(complaints_df_cases_by_object_second_category)

# 计算每个“不同消费类型”中初查受理状态状态为“已受理”的计数
complaints_df_cases_by_object_second_category = complaints_df[complaints_df['初查受理状态'] == '已受理'].groupby('消费类型').size().reset_index(name='已受理个数')

print(complaints_df_cases_by_object_second_category)

# 按照消费类型和销售方式进行分组，计算每个组合的数量
classification_counts = complaints_df.groupby(['消费类型', '销售方式']).size().reset_index(name='数量')

print(classification_counts)

# 计算每个“消费类型”中消费金额(单位:元)的总和
sum_reports_df_by_object_second_category = complaints_df.groupby('消费类型')['消费金额(单位:元)'].sum().reset_index(name='消费金额总和')

print(sum_reports_df_by_object_second_category)


# 计算每个“消费类型”中挽回经济损失(单位:元)的总和
complaints_df['挽回经济损失(单位:元)'].fillna(0, inplace=True)
sum_reports_df_by_object_second_category = complaints_df.groupby('消费类型')['挽回经济损失(单位:元)'].sum().reset_index(name='挽回经济损失总和')

print(sum_reports_df_by_object_second_category)
