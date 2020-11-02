date = input('Enter the date in format dd,mm,yyyy: ')
exam_date = date.split(",")

print('The examination will start from : ' + '/'.join(exam_date))