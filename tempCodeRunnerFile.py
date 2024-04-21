    # Getting the current UTC time
    utc_now = datetime.utcnow()

    # Converting UTC time to local time, for example, America/New_York
    local_timezone = pytz.timezone('America/New_York')
    local_now = utc_now.replace(tzinfo=pytz.utc).astimezone(local_timezone)

    # Print both UTC and local times
    print("UTC time:", utc_now.isoformat() + 'Z')
    print("Local time:", local_now.isoformat())
        
