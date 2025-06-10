# Time calculator  

# converting second ~ into the following:

# Hours = time // 3600
# Minutes = (time % 3600) // 60
# Seconds = time % 60

def time_calc(sec):
    # convert to hours 
    hours = sec // 3600 # will return hours 

    # convert to minutes 
    minutes = (sec % 3600) // 60

    # convert to seconds 
    seconds = sec % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"
