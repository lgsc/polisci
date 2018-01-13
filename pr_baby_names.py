import utils
import pandas as pd



link_dict = {'2015':'https://www.ssa.gov/oact/babynames/territory/puertorico2015.html',
             '2014':'https://www.ssa.gov/oact/babynames/territory/puertorico2014.html',
             '2013':'https://www.ssa.gov/oact/babynames/territory/puertorico2013.html',
             '2012':'https://www.ssa.gov/oact/babynames/territory/puertorico2012.html',
             '2011':'https://www.ssa.gov/oact/babynames/territory/puertorico2011.html',
             '2010':'https://www.ssa.gov/oact/babynames/territory/puertorico2010.html',
             '2009':'https://www.ssa.gov/oact/babynames/territory/puertorico2009.html',
             '2008':'https://www.ssa.gov/oact/babynames/territory/puertorico2008.html',
             '2007':'https://www.ssa.gov/oact/babynames/territory/puertorico2007.html',
             '2006':'https://www.ssa.gov/oact/babynames/territory/puertorico2006.html',
             '2005':'https://www.ssa.gov/oact/babynames/territory/puertorico2005.html',
             '2004':'https://www.ssa.gov/oact/babynames/territory/puertorico2004.html',
             '2003':'https://www.ssa.gov/oact/babynames/territory/puertorico2003.html',
             '2002':'https://www.ssa.gov/oact/babynames/territory/puertorico2002.html',
             '2001':'https://www.ssa.gov/oact/babynames/territory/puertorico2001.html',
             '2000':'https://www.ssa.gov/oact/babynames/territory/puertorico2000.html',
             '1999':'https://www.ssa.gov/oact/babynames/territory/puertorico1999.html',
             '1998':'https://www.ssa.gov/oact/babynames/territory/puertorico1998.html'}

"""
# This code is for seeing what the data looks like
data = utils.get_souptable("https://www.ssa.gov/oact/babynames/territory/puertorico2015.html")
df = pd.DataFrame(list(data.items()), columns=['data_id', 'data_point'])
df['data_id'] = df['data_id'].astype(int)
df = df.sort('data_id')
df = df[2:]
#print(df)
#data_point = data['3']
#print(data_point)
"""

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
    #data_frame['year'] = '2015'
    return data_frame

def girls_data_frame(data):
    col_rank = create_data_column(2,data,5)
    girl_names = create_data_column(5,data,5)
    num_born = create_data_column(6,data,5)
    data_frame = pd.DataFrame(list(map(list, zip(col_rank,girl_names,num_born))))
    data_frame.columns = ['year_rank', 'name','num_born']
    data_frame['sex'] = 'F'
    #data_frame['year'] = '2015'
    return data_frame

def pr_name_data(link_dict):
    final_data = pd.DataFrame()
    for year in link_dict:
        data = utils.get_souptable(link_dict[year])
        gender_frames = [boys_data_frame(data), girls_data_frame(data)]
        combined_year_data = pd.concat(gender_frames)
        combined_year_data['year'] = year
        almost_done_frames = [combined_year_data, final_data]
        final_data = pd.concat(almost_done_frames)
    return final_data


data = pr_name_data(link_dict)
data.to_csv("/Users/gsanchez/Desktop/pr_top_names.csv")

print(data)
