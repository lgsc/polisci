import utils
import pandas as pd




data = utils.get_souptable("https://www.ssa.gov/oact/babynames/territory/puertorico2015.html")

df = pd.DataFrame(list(data.items()), columns=['data_id', 'data_point'])
df['data_id'] = df['data_id'].astype(int)
df = df.sort('data_id')
df = df[2:]
#print(df)
#data_point = data['3']
#print(data_point)

def create_data_column(start_num,data_dict,increment):
    column_list = list()
    while start_num < 502:
        key = str(start_num)
        column_list.append(data_dict[key])
        #print(start_num)
        start_num += increment
    return column_list

def boys_data_frame(data):
    col_rank = create_data_column(2,data,5)
    boy_names = create_data_column(3,data,5)
    num_born = create_data_column(4,data,5)
    data_frame = pd.DataFrame(list(map(list, zip(col_rank,boy_names,num_born))))
    data_frame.columns = ['year_rank', 'name','num_born']
    data_frame['sex'] = 'M'
    data_frame['year'] = '2015'
    return data_frame

new_df = boys_data_frame(data)
print(new_df)
