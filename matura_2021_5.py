import re, numpy, matplotlib.pyplot as plt

def year_average(data_record):
    average=0
    suma=0
    for i in range (4,16):
        suma+=data_record[i]
    average=suma/12
    average=round(average,2)    
    return average

def prepare_data(filename):
    file=open(filename,'r')
    data=file.readlines()
    file.close()
    #print(data)

    data_list=[]
    for element in data:
        elem=element.rstrip("\n")
        data_list.append(elem)
    data_list.pop(0)
    #print(data_list)
    return data_list





#lista nr klienta, srednie zuzycie na jedna osobe
def get_average_list(data_list,data_reg):
    average_list=[]
    for i in range (len(data_list)):
        suma=0
        srednia=0
        liczba_osob=0
        data_exp=data_reg.search(data_list[i])
        for i in range(4,16):
            suma+=int(data_exp.group(i))
            liczba_osob=int(data_exp.group(2).lstrip('0'))
            srednia=suma/liczba_osob
            srednia=round(srednia,2)
        average_list.append([data_exp.group(1),srednia])
    
    my_array=numpy.array(average_list)
    my_array=my_array[my_array[:,1].argsort()]
    my_array=my_array[-10::]
    my_array=my_array[::-1]
    print(my_array)
    return my_array


def get_district_list(data_list,data_reg):
    districts={}
    for i in range (len(data_list)):
        suma=0
        district=''
        data_exp=data_reg.search(data_list[i])
        for i in range(4,16):
            suma+=int(data_exp.group(i))
            district=data_exp.group(3)
        if(district in districts.keys()):
            districts.update({district:districts.get(district)+suma})  
        else:
            districts.update({district:suma})
    print(districts)
    return districts

def get_district_monthly_list(data_list,data_reg):
    district_codes=[]
    for i in range(len(data_list)):
        data_exp=data_reg.search(data_list[i])
        district_codes.append(data_exp.group(3))
    district_codes=set(district_codes)
    district_codes=list(district_codes)
    print(district_codes)

    districts_monthly=[]
    for code in district_codes:
        districts_monthly.append([code,0,0,0,0,0,0,0,0,0,0,0,0])
    #print(districts_monthly)
    for element in districts_monthly:
        for i in range(len(data_list)):
            data_exp=data_reg.search(data_list[i])
            if(data_exp.group(3)==element[0]):
                for i in range(1,13):
                    element[i]+=int(data_exp.group(i+3))
    print(districts_monthly)
    districts_min_max=[]
    for element in districts_monthly:
        districts_min_max.append([element[0],min(element[1:13]),max(element[1:13])])
    print(districts_min_max)
    return districts_monthly
def get_year_month_list(districts_monthly):
    water_yearly_by_month=[2019,0,0,0,0,0,0,0,0,0,0,0,0]
    for element in districts_monthly:
        for i in range (1,13):
            water_yearly_by_month[i]+=element[i]

    print(water_yearly_by_month)
    return water_yearly_by_month

def prognose_water_needed(water_yearly_by_month):
    water_yearly_by_month=[water_yearly_by_month]
    for i in range (1,12):
        water_yearly_by_month.append([2019+i,
        int((1.01*water_yearly_by_month[i-1][1])),
        int((1.01*water_yearly_by_month[i-1][2])),
        int((1.01*water_yearly_by_month[i-1][3])),
        int((1.01*water_yearly_by_month[i-1][4])),
        int((1.01*water_yearly_by_month[i-1][5])),
        int((1.01*water_yearly_by_month[i-1][6])),
        int((1.01*water_yearly_by_month[i-1][7])),
        int((1.01*water_yearly_by_month[i-1][8])),
        int((1.01*water_yearly_by_month[i-1][9])),
        int((1.01*water_yearly_by_month[i-1][10])),
        int((1.01*water_yearly_by_month[i-1][11])),
        int((1.01*water_yearly_by_month[i-1][12])),
        ])
    print(water_yearly_by_month)
    
    return water_yearly_by_month

def plot_water(water_needed):
    x=[]
    for i in range(1,13):
        x.append(i)
    y=water_needed[1:13]
    
    plt.plot(x,y)
    plt.show()

    return 0


data_list=prepare_data('wodociagi.txt')
data_reg=re.compile(r'(\d\d\d\d\d)(\d\d)(\D\D\D);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*);(\d*)')

my_array=get_average_list(data_list,data_reg)
districts_dict=get_district_list(data_list,data_reg)
districts_monthly=get_district_monthly_list(data_list,data_reg)
water_yearly_by_month=get_year_month_list(districts_monthly)
prognosed_water=prognose_water_needed(water_yearly_by_month)
plot_water(prognosed_water[11])
