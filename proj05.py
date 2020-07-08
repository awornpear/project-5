import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    valid = False
    while not valid: 
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        year_input = 'year' + str(year_str) + '.txt'
        if int(year_str) >= 1990 and int(year_str) <= 2015:
            
            try:
                fp = open(year_input)
                valid = True
            except FileNotFoundError:
                print("Error. Invalid File name.")
            except ValueError:
                print('Error. invalid year.')
            
        else: 
            print('error')
    return fp, int(year_str)

        
def read_file(fp):
    '''You fill in the doc string'''
    
    output_lst = []
    
    fp.readline()
    fp.readline()
    
    for line in fp:
        line = line.strip()
        line = line.replace(',', '')
        line_lst = line.split()
        for i in range(len(line_lst)):
            if '-' not in line_lst[i] and 'and' not in line_lst[i]:
                if 'over' in line_lst[i]:
                    line_lst[i] = float('inf')
                else:
                    line_lst[i] = float(line_lst[i])
        output_lst.append(line_lst)
    return output_lst
                
def find_average(data_lst):
    '''You fill in the doc string'''
    total_sal = 0
    total_people = 0
    
    for row in data_lst:
        total_sal += float(row[6])
        total_people += float(row[3])
        
    avg = total_sal/total_people
    
    return avg
    
def find_median(data_lst):
    '''You fill in the doc string'''
    
    median_income = 0
    close_to_50 = 100
    
    for i in range(100):
        temp_val = get_range(data_lst, i)
        if abs(temp_val[1] - 50) < close_to_50:         
            close_to_50 = abs(temp_val[1] - 50)
            median_income = temp_val[2]
            
    return median_income
        
def get_range(data_lst, percent):
    '''You fill in the doc string'''
    for row in data_lst:
        if row[5] >= percent:
            return ((row[0], row[2]), row[5], row[7])

def get_percent(data_lst,salary):
    '''You fill in the doc string'''
    
    for row in data_lst:
        
        if salary >= row[0] and salary <= row[2]:
            return ((row[0],row[2]), row[5])
    

def main():
    fp, year = open_file()
    data_lst = read_file(fp)
    fp.close()
    
    avg = find_average(data_lst)
    median = find_median(data_lst)
    # Insert code here to determine year, average, and median
    print("For the year {:4d}:".format(year))
    print("The average income was ${:<13,.2f}".format(avg))
    print("The median income was ${:<13,.2f}".format(median))
    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        # determine x_vals, a list of floats -- use the lowest 40 income ranges
        # determine y_vales, a list of floats of the same length as x_vals
        # do_plot(x_vals,y_vals,year)
        x_vals = []
        y_vals = []
        for i in range(40):
            x_vals.append(data_lst[i][0])
            y_vals.append(data_lst[i][5])
            do_plot(x_vals, y_vals, year)
    x= 0
   
    while x == 0:
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
        if choice.lower() == 'r':
            percent = float(input('Enter a percent: '))
            if percent <= 100 and percent > 0:
                range_func = get_range(data_lst, percent)[0][0]
                print('{:4.2f}% of incomes are below ${:<13,.2f}'.format(percent, range_func))
            else:
                print("income error")
        elif choice.lower() == 'p':
            salary = input('Enter an income: ')
            if not salary.isdigit():
                print('Salary error')
            elif float(salary) > 0:
                salary = float(salary)
                percent_func = get_percent(data_lst, salary)[1]
                print("An income of ${:<13.2f} is in the top {:4.2f}% of incomes".format(salary, percent_func))
            else:
                print("Error")
        elif choice == '':
            x = 1
        else:
            print("Error")
if __name__ == "__main__":
    main()