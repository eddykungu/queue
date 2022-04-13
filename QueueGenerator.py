from dataclasses import dataclass
from typing import List
import LinearCon
import CombinedLinearCon
import xlsxwriter


@dataclass
class CustomerData:
    inter_arrival_time: int
    service_time: int
    
@dataclass
class ProcessedCustomerData:
    customer: int
    inter_arrival_time: int
    arrival_time: int
    service_time: int
    time_service_begins: int
    waiting_time:int
    time_service_ends: int
    time_customer_spent: int
    idle_time: int
    
    
    
def generateCustomerData():
    lcm = LinearCon.LinearCon()
    clcm = CombinedLinearCon.CLCM()
    data:List[CustomerData] = []
    
    for i in range(10):
        data.append(CustomerData(int(lcm.next()*10), int(clcm.next()*7)))
    return data

def process_data():
    data:List[ProcessedCustomerData] = []
    customers = generateCustomerData()
    
    i= 1
    previous_time_service_end= 0
    arrival_time=0
    for item in customers:
        inter_arrival_time= item.inter_arrival_time
        inter_arrival_time = 0 if i==1 else inter_arrival_time
        arrival_time += inter_arrival_time
        time_service_begins= arrival_time if previous_time_service_end< arrival_time else previous_time_service_end
        waiting_time= time_service_begins-arrival_time
        service_time =  item.service_time
        time_service_ends=service_time + time_service_begins
        time_customer_spent= time_service_ends-arrival_time
        difference=arrival_time - previous_time_service_end
        idle_time= 0 if difference < 0 else difference
        previous_time_service_end = time_service_ends
        data.append(ProcessedCustomerData(i,
                                              inter_arrival_time,
                                              arrival_time,
                                              service_time,
                                              time_service_begins,
                                              waiting_time,
                                              time_service_ends,
                                              time_customer_spent,
                                              idle_time))
        print('iteration {0}'.format(i))
        i+=1
        
    return data
    
    
data = process_data()
book = xlsxwriter.Workbook("Queue.xlsx")
sheet = book.add_worksheet()
sheet.write(0,0,"Customer")
sheet.write(0,1,"Inter Arrival Time")
sheet.write(0,2,"Arrival Time")
sheet.write(0,3,"Service Time")
sheet.write(0,4, "Time Service Begins")
sheet.write(0,5, "Waiting Time")
sheet.write(0,6, "Time Service Ends")
sheet.write(0,7, "Time Customer Spent")
sheet.write(0,8, "Idle Time")

i = 1
for item in data:
    sheet.write(i, 0, item.customer)
    sheet.write(i, 1, item.inter_arrival_time)
    sheet.write(i, 2, item.arrival_time)
    sheet.write(i, 3, item.service_time)
    sheet.write(i, 4, item.time_service_begins)
    sheet.write(i, 5, item.waiting_time)
    sheet.write(i, 6, item.time_service_ends)
    sheet.write(i, 7, item.time_customer_spent)
    sheet.write(i, 8, item.idle_time)
    i += 1
    
    
book.close()