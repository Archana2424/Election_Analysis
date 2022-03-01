import datetime
now = datetime.datetime.now()
print(" the time right now is",now)
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
